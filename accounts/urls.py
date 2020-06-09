from django.urls import  path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('add_staff/', views.AddStaff.as_view(), name='add_staff'),
    path('add_student/', views.AddStudent.as_view(), name='add_student'),
]