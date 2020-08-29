from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns =[
    path('',views.index,name="homepage"),
    path('signup/',views.signup,name="signup"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('logoutpage/',views.logoutpage,name="logoutpage"),
    path('contact/',views.contactpage,name="contactpage"),
    path('itempage/',views.itempage,name="itempage"),
    path('products/<int:myid>',views.prodview,name="prodview"),
    path('myitems/',views.myitems,name="myitems"),
    path('checkout/',views.checkout,name="checkout"),

    path('aboutus/',views.aboutus,name="aboutus"),

    path('search/',views.search,name="search"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.destroy),
    path('feedback/',views.feedback,name="feedback"),

    path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)