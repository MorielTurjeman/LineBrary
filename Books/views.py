from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import User , Book , BookStationRelation , Order , categories, Contributions, Wishlist, stations
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import BookForm, BookStationRelationForm
#from .forms import ProfileForm
#from .models import Profile
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from random import shuffle
import os
# Create your views here.


def homepage(request):
    if request.user.is_authenticated:
        Books_For_Recomended = Book.objects.all().order_by('?')[:20]
        categories_array = [tup[0] for tup in categories]
        shuffle(categories_array)
        categories_books_relation_array = {}
        for category in categories_array: 
            if len(Book.objects.filter(gener=category)) > 0:
                categories_books_relation_array[category] = Book.objects.filter(gener=category)
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
    else:
        if request.POST['bookname'] != "" and request.POST['author'] != "" and request.POST['description'] != "" and request.POST['language'] != "" and request.POST['page_count'] != 0:
            b = Book(ISBN13=random.randint(0 , 999999999)  , bookname= request.POST['bookname'] , author= request.POST['author'] , gener= request.POST['gener'] , page_count= request.POST['page_count'] , condition=request.POST['condition'], image=request.POST['image'], language= request.POST['language'], description= request.POST['description'] , cover_type= request.POST['cover_type'])
            b.imageURL = 'Books/Images/' +  b.image.url
            b.save()
            bsr = BookStationRelation(station=request.POST["station"], book= b)
            bsr.save()
            return redirect('homepage')
        else:
            return render(request, 'Books/addbook.html', {'station_form' : BookStationRelationForm() , 'book_form' : BookForm() , 'errMsg' : "An error occurred. The book isn't uploaded. Plese check the correctness." })


def user(request):
    if request.method == 'GET':
        orders = Order.objects.filter(user__username=request.user)
        contributions= Contributions.objects.filter(user__username=request.user)
        wishlist= Wishlist.objects.filter(user__username=request.user)
        return render(request,'Books/user.html',{'User_Name':request.user, "orders" : orders, 'contributions':contributions,}  )

# def loans(request):
#     if request.method=='GET':
#         bookstation=BookStationRelation.object.filter(Book.ISBN13=Book.ISBN13).delete()
#             return render(request, )

def linkBooks(request):
    if request.method == 'GET':
        BookStationRelation.objects.all().delete()
        books = Book.objects.all()
        for i in range(len(books)):
            r = BookStationRelation.objects.create(ISBN13=books[i], station=stations[i % len(stations)][0])
            r.save()

        return JsonResponse({})


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

def bookLocation(request):
    if request.method == 'GET':
        id = request.GET['isbn']
        rel = BookStationRelation.objects.filter(ISBN13__ISBN13=id)
        if (len(rel) > 0):
            return JsonResponse({'station': rel[0].station})
        else:
            return JsonResponse({})