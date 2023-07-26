from django.shortcuts import render,get_object_or_404,redirect
from .models import Movies,Movies2,Registration
from .forms import SignupForm


# Create your views here.
def index(request):
    m = Movies.objects.all()
    print(m)
    return render(request,'index.html',{'m':m})


def upcoming(request):
    m1 = Movies2.objects.all()
    return render(request,'upcoming.html',{'m1':m1})

def updetails(request,pk):
    d1 =  get_object_or_404(Movies2,id=pk)

    print("hello upcoming")
    return render(request,'updetails.html',{'d1':d1})


def about(request):
    return render(request,'Untitled-1.html')

def detailsmovie(request,pk):
    d=get_object_or_404(Movies,id=pk)
    return render(request,'details.html',{'d':d})


#signup section
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('booked')
    else:
        form = SignupForm()
    
    return render(request,'signup.html',{'form':form})

def booked(request):
    return render(request,'booked.html')

def login(request):
    # if request.method == 'POST':
    #     form = LoginForm(request.POST)
    # else:
    #     form = LoginForm()
    return render(request,'login.html')

