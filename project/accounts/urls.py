from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('',views.home, name='home'), 

    path('change_password', views.change_password, name='change_password'),


    path('view_products/', views.view_products, name='view_products'),

    path('only_for_teachers/', views.only_for_teachers, name='only_for_teachers'),
]