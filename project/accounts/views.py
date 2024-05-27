from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from . import models
from .decorators import has_to_be_teacher

# Create your views here.
def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        


        new_user = User.objects.create_user(username, '', password)
        new_user.save()

        messages.success(request, "Account created successfully, you can login now.")

        return redirect("accounts:signup")

    return render(request, 'accounts/signup_login.html')



def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # user = User.objects.get(username=username)

        if user is not None:
            login(request, user)

            messages.success(request, "Login successful.")
            return redirect("accounts:home")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("accounts:signup")
            
        # if user:
        #     if user.check_password(password):
        #         return redirect("home")
    return render(request, 'accounts/signup_login.html')



def logout_view(request):
    logout(request)
    messages.success(request, "Logout successful.")
    return redirect("accounts:login")

def home(request):
    return render(request, "accounts/home.html")


@login_required
def change_password(request):
    if request.method == "POST":
        user = request.user

        old_password = request.POST['o_password']
        new_password = request.POST['password']
        confirm_password = request.POST['c_password']

        if new_password == confirm_password:
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()

                messages.success(request, "Password changed successfully.")
                return redirect("accounts:home")
        else:
            messages.warning(request, "New password and confirm password did not match.")
            return redirect("accounts:home")


        # if user.check_password(old_password):
        #     if new_password == confirm_password:
        #         user.set_password(new_password)
        #         user.save()
        #         messages.success(request, "Password changed successfully.")
        #         return redirect("accounts:home")
        #     else:
        #         messages.error(request, "New password and confirm password did not match.")
        #         return redirect("accounts:change_password")
        # else:
        #     messages.error(request, "Old password did not match.")
        #     return redirect("accounts:change_password")



@permission_required('accounts.view_product', raise_exception=True)
def view_products(request):
    products = models.Product.objects.values_list('name', flat=True)
    
    return HttpResponse(f"View products: {products}")



@has_to_be_teacher
def only_for_teachers(request):
    return HttpResponse("Only for teachers")