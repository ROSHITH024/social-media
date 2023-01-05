from django.shortcuts import render,redirect
from api.models import User
from api.models import Post,Comment,Follower,UserProfile
from socialweb.form import *
from django.views.generic import View,TemplateView,CreateView,FormView,ListView,UpdateView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

# Create your views here.

def signin_required(fn):
    def wraper(request,*args,**kw):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session")
            return redirect("sign-in")
        else:
            return fn(request,*args,**kw)
    return wraper

decs=[signin_required,never_cache]

class RegistrationForm(CreateView):
    template_name="register.html"
    form_class=UserRegistration
    model=User
    success_url=reverse_lazy("sign-in")


class UserLoginForm(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kw):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            # print(f"user={usr}")
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                return render(request,"login.html",{"form":form})

@method_decorator(decs,name="dispatch")
class IndexView(ListView):
    template_name="index.html"
    model=Post
    context_object_name="posts"
    def get_queryset(self):
        return Post.objects.all().order_by("-created_date")

def sign_out_view(request,*args,**kw):
    logout(request)
    return redirect("sign-in")

@method_decorator(decs,name="dispatch")
class PostFormView(CreateView):
    template_name="post.html"
    form_class=PostForm
    success_url=reverse_lazy("home")
    model=Post

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

decs
def add_comments(request,*args,**kwargs):
    id=kwargs.get("id")
    pos=Post.objects.get(id=id)
    cmt=request.POST.get("comment")
    
    Comment.objects.create(post=pos,comment=cmt,user=request.user)
    messages.success(request,"your comment adedd successfully")
    return redirect("home")

decs
def like_posts(request,*args,**kwargs):
    id=kwargs.get("id")
    pos=Post.objects.get(id=id)
    if pos.like.contains(request.user):
        pos.like.remove(request.user)

    else:
        pos.like.add(request.user)
    return redirect("home")

@method_decorator(decs,name="dispatch")
class ProfileView(ListView):
    template_name="profile.html"
    model=User
    context_object_name="users"
    def get_queryset(self):
        return User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["uposts"] = Post.objects.filter(user=self.request.user)
        return context



class ListPeopleView(ListView):
    template_name="peoples.html"
    model = User
    context_object_name = 'people'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["followings"] = Follower.objects.filter(followers=self.request.user)
        context["posts"] = Post.objects.all().order_by('-created_date')
        return context
    

    def get_queryset(self):
        return User.objects.exclude(username=self.request.user)
 

def add_follower(request, *args, **kwargs):
    id = kwargs.get('id')
    usr = User.objects.get(id=id)
    if not Follower.objects.filter(user=usr, followers=request.user):
        Follower.objects.create(user=usr, followers=request.user)
    else:
        Follower.objects.get(user=usr, followers=request.user).delete()
    return redirect("people")

def comment_delete(request,*args,**kw):
    id=kw.get("id")
    Comment.objects.get(id=id).delete()
    return redirect("home")

def post_delete(request,*args,**kw):
    id=kw.get("id")
    Post.objects.get(id=id).delete()
    return redirect("profile")

class EditprofileView(UpdateView):
    template_name="update.html"
    form_class=ProUpdateForm
    model=User
    pk_url_kwarg="id"
    success_url=reverse_lazy("profile")



# class ProfileUpdateView(CreateView):
#     template_name="update.html"
#     form_class=ProUpdateForm
#     model=User
#     success_url=reverse_lazy("profile")

#     def form_valid(self, form):
#         form.instance.user=self.request.user
#         return super().form_valid(form)


# def userpost(request,*args,**kw):
#     pos=Post.objects.filter(user=request.user)
#     return pos
