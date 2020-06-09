from django.urls import path
from courses import  views

app_name = 'courses'
urlpatterns = [
    path('add_course/', views.AddCoruse.as_view(), name='add_course'),
    path('add_subject/', views.AddSubject.as_view(), name='add_subject'),
    path('subject_detail/<int:pk>/', views.SubjectDetail.as_view, name='subject_detail'),
    path('manage_subject/', views.ManageSubject.as_view(), name='manage_subject'),
    path('subject_edit/<int:pk>/', views.SubjectUpdate.as_view, name='subject_edit'),
]