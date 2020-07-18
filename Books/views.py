from django.shortcuts import render, redirect
from .models import User , Book , BookStationRelation , Order , categories
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import BookForm, BookStationRelationForm
#from .forms import ProfileForm
#from .models import Profile
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from random import shuffle
# Create your views here.




def homepage(request):
    if request.user.is_authenticated:
        Books_For_Recomended = Book.objects.all().order_by('?')[:20]
        categories_array = [tup[0] for tup in categories]
        shuffle(categories_array)
        categories_books_relation_array = []
        for category in categories_array: 
            categories_books_relation_array.append(Book.objects.filter(gener=category))
        return render(request , "Books/index.html", { 'User_Name' : User.username , 'Books_For_Recomended' : Books_For_Recomended , 'categories' : categories_array , 'books' : categories_books_relation_array })
    else: 
        return redirect("login_page")

def login_page(request): 
    if request.method == 'GET':   
        return render(request , "Books/login.html", {'login_form' : AuthenticationForm()})
    else:
        user = authenticate(request, username= request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'Books/login.html', { 'login_form': AuthenticationForm() , 'errMsg' : 'User is not exsists, or password is incorrect'})
        else:
            login(request, user)
            return redirect('homepage')

def register(request):
    if request.method == 'GET':
        return render(request, 'Books/register.html', {'user_form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username= request.POST['username'], password=request.POST['password1'])
                user.save() 
                login(request, user)
                return redirect('homepage')
            except IntegrityError:
                return render(request, 'Books/register.html', {'user_form': UserCreationForm(),
                                                                     "errMsg": "User exists. Choose a different one"})
        else:
            return render(request, 'Books/register.html', {'user_form': UserCreationForm(),
                                                                 "errMsg": "Password didn't match"})


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login_page')

def add_book(request):
    if request.method == 'GET':
        return render(request, 'Books/addbook.html', {'station_form' : BookStationRelationForm() , 'book_form' : BookForm() })

"""

def register(request):
    if request.method == 'GET':
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
            return render(request , "Books/register.html" , { 'user_form':user_form , 'profile_form': profile_form } )
    else:
        if request.POST['password1'] == request.POST['password2']:
            #profile_form = ProfileForm(request.POST['userName'], request.POST['firstname'], request.POST['lastname'], request.POST['email'], request.POST['password1'], request['image'])
            #profile_form = ProfileForm.Meta.model.objects.create(user= User.objects.create_user(username= request.POST['userName'],firstName= request.POST['firstname'],lastName= request.POST['lastname'],email= request.POST['email'],password= request.POST['password1']))
            try:
                user_form = UserForm(request.POST, instance=request.user)
                profile_form = ProfileForm(request.POST, instance=request.user.profile)
                #user = User.objects.create_user()
                if user_form.is_valid() and profile_form.is_valid():
                    user_form.save()
                    profile_form.save()
                    new_user = authenticate(username=profile_form.cleaned_data['userName'], password=profile_form.cleaned_data['password1'],)
                    login(request, new_user)
                    return redirect("/login_page/")
                return render(request, "Books/register.html" , {'profile_form': profile_form , 'errMsg' : "Here!!!!!"})
            except IntegrityError:
                return render(request , "Books/register.html" , {'profile_form': profile_form , 'errMsg': profile_form.userName + profile_form.password1 + profile_form.email + profile_form.image.url})
        else:
            return render(request, "Books/register.html" , {'profile_form': profile_form , 'errMsg' : "Password did not match"})
"""