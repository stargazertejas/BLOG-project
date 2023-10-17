from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import sign_up_form ,login_form,post_form
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import time
from .models import blog_posts
from django.contrib.auth.models import Group

# for home page
def homepage(request):
    posts=blog_posts.objects.all()
    return render (request,'blog/homepage.html',{'posts':posts})

# for about page
def aboutpage(request):
    return render (request,'blog/about.html')

# for contact page
def contactpage(request):
    return render (request,'blog/contact.html')

# for dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts=blog_posts.objects.all()
        user=request.user
        fullname=user.get_full_name()
        gps=user.groups.all()
        return render (request,'blog/dashboard.html',{'posts':posts,'fullname':fullname,'groups':gps})
    else:
        return HttpResponseRedirect('login')

# for logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# for signUp
def user_signup(request):
    if request.method== "POST":
        form=sign_up_form(request.POST)
        if form.is_valid:
            user=form.save()
            messages.success(request,'Congratulations on becoming an Author !')
            group=Group.objects.get(name='Author')
            user.groups.add(group)
            # time.sleep(3)
            return HttpResponseRedirect('login')
        else:
            form=sign_up_form()
    else:
        form=sign_up_form()
    return render(request,'blog/signup.html',{'form':form})


# for user_login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method== "POST":
            form=login_form(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"You're Logged in !")
                    # return HttpResponseRedirect('dashboard')
                else:
                    form=login_form()
            else:
                form=login_form()
        else:
            form=login_form()
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('dashboard')
    

# adds new post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form=post_form(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                form=blog_posts(title=title,desc=desc)
                form.save()
                return redirect("dashboard")
        else:
            form=post_form()
        return render(request,'blog/addpost.html',{'form':form})
    else:
        return redirect('login')

# update post
def update_post(request, id):
    if request.user.is_authenticated:
        pi= blog_posts.objects.get(pk=id)
        if request.method == "POST":
            form=post_form(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:   
            form=post_form(instance=pi)
        return render(request,'blog/updatepost.html',{'form':form,'post':pi})
    else:
        return redirect('login')


# delete post
def delete(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi=blog_posts.objects.get(pk=id)
            pi.delete()
            return redirect('dashboard')
    else:
        return redirect('login')