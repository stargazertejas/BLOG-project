from django.urls import path
from blog_app import views

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('aboutpage',views.aboutpage,name='aboutpage'),
    path('contactpage',views.contactpage,name='contactpage'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.user_logout,name='logout'),
    path('signup',views.user_signup,name='signup'),
    path('login',views.user_login,name='login'),
    path('addpost',views.add_post,name='addpost'),
    path('updatepost/<int:id>',views.update_post,name='updatepost'),
    path('delete/<int:id>',views.delete,name='delete')

]