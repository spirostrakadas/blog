from django.shortcuts import render,get_object_or_404,redirect
from.models import Post,Profile,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, login, authenticate,logout
from django.contrib import messages
from .forms import PostForm,CommentForm,Profileform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth


# Create your views here.
User = get_user_model()



def index(request):
    user_object=User.objects.get(username=request.user)
    user_profile=Profile.objects.get(user=user_object)
    post=Post.objects.all()
    return render(request,'index.html',{'post':post,'user_profile':user_profile})



def detail(request,pk):
    post=get_object_or_404(Post,id=pk)
    comments=post.comments.all()                                #related_name=comments   specifies the name of the reverse relation.
    form=CommentForm()
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid:
            comment=form.save(commit=False)
            comment.user=request.user
            comment.post=post
            comment.save()
            return redirect('detail',pk)
        else:
            form=CommentForm()   

    return render(request,'detail.html',{'post':post,'comments':comments,'form':form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            # create a Profile instance for the new user
            profile = Profile.objects.create(user=user) # in settings.py AUTH_USER_MODEL='auth.User'
            profile.save()                              # need to specify the AUTH_USER_MODEL setting to tell Django which model to use as the user model for authentication.  
            # log the user in
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
    
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_msg = 'Invalid username or password.'
    else:
        error_msg = ''
    return render(request, 'signin.html', {'error_msg': error_msg})

@login_required(login_url='signin')
def log_out(request):
    auth.logout(request)
    return redirect('signin')

#def logout(request):
   # user=get_user_model()
   # user=User.objects.get(pk=request.user.pk)
   # logout(request)
   # return redirect('home')
    

@login_required
def newPost(request): #in the template when i build the form i also need method='post' and !!!!enctype="multipart/form-data"!!!
    form=PostForm()
    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user=request.user.username
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})



@login_required
def delete(request,pk):
    post=get_object_or_404(Post,id=pk,)
    post.delete()
    return redirect('home')

def MyProfile(request,pk):
    user=get_user_model()                             #define first wich is the user so i can take the profile
    user=User.objects.get(pk=request.user.pk)
    profile=Profile.objects.get(user=user)
    posts = Post.objects.filter(user=user.username)
    
    if request.method == 'POST':
        form = Profileform(request.POST, request.FILES, instance=profile)  
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('home')
    else:
        form = Profileform(instance=profile)
    

    return render(request,'myprofile.html',{'profile':profile,'posts': posts})
