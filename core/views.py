from django.shortcuts import render,get_object_or_404,redirect
from.models import Post,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib import messages


# Create your views here.
User = get_user_model()



def index(request):
    user_object=User.objects.get(username=request.user)
    user_profile=Profile.objects.get(user=user_object)
    post=Post.objects.all()
    return render(request,'index.html',{'post':post,'user_profile':user_profile})



def detail(request,pk):
    post=get_object_or_404(Post,id=pk)
    return render(request,'detail.html',{'post':post})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            # create a Profile instance for the new user
            profile = Profile(user=user)
            profile.save()
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
