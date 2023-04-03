from django.shortcuts import render,get_object_or_404
from.models import Post,User,Profile


# Create your views here.
def index(request):
    user_object=User.objects.get(username=request.user.username)
    user_profile=Profile.objects.get(user=user_object)
    post=Post.objects.all()
    return render(request,'index.html',{'post':post,'user_profile':user_profile})



def detail(request,pk):
    post=get_object_or_404(Post,id=pk)
    return render(request,'detail.html',{'post':post})
