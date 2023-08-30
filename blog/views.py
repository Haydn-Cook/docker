from datetime import datetime
from django.shortcuts import render,redirect
from .models import Blog_Post
from django.contrib.auth.models import User

def blog(request):
    blog_posts = Blog_Post.objects.all()
    return render(request, 'blog/blog.html', {'blog_posts': blog_posts})

def add_blog(request):
    if request.method == 'POST':
        user_id = request.POST.get('user')
        title =  request.POST.get('blog_title')
        body = request.POST.get('body')
        try:
            user = User.objects.get(id=user_id)
            
            new_blog = Blog_Post(user=user, blog_title=title, body=body, date=datetime.now())
            new_blog.save()
            
            return redirect('blog')
        except User.DoesNotExist:
            # Handle the case where the user with the provided ID does not exist
            pass
        
    return render(request, 'blog/add_blog.html')