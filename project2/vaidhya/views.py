from django.shortcuts import render,redirect

from .forms import ConsultaionForm, UserCreationForm,UserLoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    context={
        'var' : 'this is sent'
    }
    return render(request,'about.html',context)
def calculator(request):
    return render(request,'calculator.html')

def contact(request):
    return render(request,'contact.html')

def cart(request):
    return render(request,'cart.html')

def products(request):
    return render(request,'products.html')

def consult(request):
    if request.method == 'POST':
        form = ConsultaionForm(request.POST)
        if form.is_valid():
            form.save()
            form = ConsultaionForm()
            return redirect("consult_success")
    else:
        form = ConsultaionForm()
    return render(request,'consult.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  # Redirect to your desired page after login
            else:
                messages.error(request, "Invalid email or password.")
                return redirect('login')  # Redirect back to login page

    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def consult_success(request):
    return render(request,'consult_success.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserCreationForm()
            return redirect("home")

    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})