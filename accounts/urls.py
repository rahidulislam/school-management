from django.urls import  path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('add_staff/', views.StaffAdd.as_view(), name='add_staff'),
    path('manage_staff/', views.ManageStaff.as_view(), name='manage_staff'),
    path('staff_edit/<int:pk>/', views.StaffUpdate.as_view(), name='staff_edit'),
    path('add_student/', views.StudentAdd.as_view(), name='add_student'),
]