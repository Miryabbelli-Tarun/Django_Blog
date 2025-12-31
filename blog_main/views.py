
from django.shortcuts import redirect, render
from assignments.models import About
from blog_main.forms import RegisterForm
from blogs.models import Blog, Category
from django.contrib.auth.models import User


def home(request):
    # categories=Category.objects.all()
    featured_posts=Blog.objects.filter(is_featured=True,status='Published')
    posts=Blog.objects.filter(is_featured=False,status='Published')
    try:
        about=About.objects.get()
    except:
        about=None
    context={
        # 'categories':categories,
        'featured_posts':featured_posts,
        'posts':posts,
        'about':about,
    }
    return render(request,'home.html',context)

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            user=User(**form.cleaned_data)
            user.save()
            return redirect('register')
    form=RegisterForm()
    context={
        'form':form,
    }
    return render(request,'register.html',context)