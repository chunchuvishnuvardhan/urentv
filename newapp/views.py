from math import ceil

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import Createuserform, contactform, feedbackform,ProductForm
from .models import Product, Orders,User
import json
from django.http import Http404

# Create your views here.



def signup(request):
       form=Createuserform()
       if request.method=="POST":
          form = Createuserform(request.POST)
          if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')


            messages.success(request, user + "Your Account Was Created Successfully")
            return redirect("loginpage")
       return render(request,"newapp/signup.html",{'form':form})


def loginpage(request):

      if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("homepage")
        else:
            messages.info(request,'Username or Password is incorrect')

      return render(request,"newapp/login.html")
def logoutpage(request):
    logout(request)
    return redirect("loginpage")






@login_required(login_url="loginpage")
def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request,"business/index.html",params)




def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.itemname.lower()   or query in item.category.lower() or query in item.itemowner.lower() or query in item.adress  :
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<3:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'business/search.html', params)
@login_required(login_url="loginpage")

def feedback(request):
    if request.method=="POST":
        form4=feedbackform(request.POST)
        if form4.is_valid():
            form4.save()
            name=form4.cleaned_data.get('name')
            messages.success(request,"Thank You "+ name +" For Giving Your Valuable Feedback")
            return redirect('feedback')

    else:
        form4=feedbackform()

    return render(request,"business/commentpage.html")

@login_required(login_url="loginpage")

def checkout(request):
    if request.method=="POST":
        items_json=request.POST.get('itemsJson','')
        name= request.POST.get('name','')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2= request.POST.get('address2','')
        city = request.POST.get('city', '')
        state= request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order=Orders(items_json=items_json,name=name,email=email,address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,phone=phone)
        order.save()
        thank= True
        id=order.order_id
        return render(request,"business/checkout.html",{'thank':thank,'id':id})

    return render(request,"business/checkout.html")


@login_required(login_url="loginpage")

def contactpage(request):
    if request.method=="POST":
        form2=contactform(request.POST)
        if form2.is_valid:
            form2.save()
            name=form2.cleaned_data.get('name')
            messages.success(request, "Thank You " + name+" We Will Contact You Soon")
            return redirect("contactpage")

    else:
        form2=contactform()

    return render(request,"business/contactpage.html",{'form2':form2})



def itempage(request):
    users=User.objects.all()
    print({'users':users})
    user= request.user
    print(user)
    if request.method=="POST":
         form1=ProductForm(request.POST,request.FILES)
         print('im inside')
         if form1.is_valid():
           instance=form1.save(commit=False)
           instance.user=request.user
           instance.save()
           itemowner=form1.cleaned_data.get('itemowner')
           category=form1.cleaned_data.get('category')
           messages.info(request, "Congratulations " +itemowner+" You Have Successfully Entered Your " +category +" with  deatils"+id)
           return redirect("itempage")
         else:
          print("There was error")
    else:
        form1=Product()
        print("form is not valid")

    return render(request,"business/urcam.html",{'form1':form1})



@login_required(login_url="loginpage")

def prodview(request,myid):

    prod = Product.objects.filter(id=myid)
    #fetch the product using id
    return render(request,"business/prodview.html",{'prod':prod[0]})

@login_required(login_url="loginpage")
def myitems(request):
    current_user=request.user
    ##url=("https://www.google.com/maps/embed/v1/MODE?key=&parameters")
    pros=Product.objects.filter(user=request.user)
    return render(request,"business/myitems.html",{'pros':pros})

@login_required(login_url="loginpage")

def aboutus(request):
    return render(request,"business/aboutus.html")

@login_required(login_url="loginpage")

def edit(request,id):
    pro=Product.objects.get(id=id)
    return render(request,'business/edit.html',{'pro':pro})

@login_required(login_url="loginpage")

def update(request,id):
    pro=Product.objects.get(id=id)
    current_user = request.user
    form1=ProductForm(request.POST,request.FILES,instance=pro)
    if form1.is_valid():
        instance=form1.save(commit=False)
        instance.user=request.user
        instance.save()
        return redirect("/myitems")
    return render(request,'business/edit.html',{'pro':pro,'user':current_user})

@login_required(login_url="loginpage")
def destroy(request,id):
    pro=Product.objects.get(id=id)
    pro.delete()
    return redirect("/myitems")
    return render(request,"business/edit.html")




#
#def itempage(request):
#    users=User.objects.all()
 #   print({'users':users})
  #  user= request.user
   # print(user)
    # if request.method=="POST":
    #   print("im inside function")
    # #   category= request.POST.get('category')
        # itemname= request.POST.get('itemname')
        # itemrentperday= request.POST.get('itemrentperday')
    #  itemowner=request.POST.get('itemowner')
    #    itemcolour=request.POST.get('itemcolour')
    #   itempic=request.POST.get('itempic')
    #   whatsappno=request.POST.get('whatsappno')
    #   whatsappno2=request.POST.get('whatsappno2')
    #   email=request.POST.get('email')
    #   adress=request.POST.get('adress')
    #   desc=request.POST.get('desc')
    #   user=request.POST.get('user')
    #
    #   form1=Product({'category':category,'itemname':itemname,'itemrentperday':itemrentperday,'itemowner':itemowner,'itemcolour':itemcolour,'itempic':itempic,'whatsappno':
    #                  whatsappno,'whatsappno2':whatsappno2,'email':email,'adress':adress,'desc':desc,'user':user})
    #   form1.save()
    #   id=form1.product_id
#   print(id)
        #