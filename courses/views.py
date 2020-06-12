from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, DetailView, ListView, UpdateView, DeleteView

from accounts.models import CustomUser
from courses.forms import AddCourseForm
from courses.models import Subject, Course


class AddCoruse(LoginRequiredMixin, FormView):
    form_class = AddCourseForm
    template_name = 'courses/add_course.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course Added Successfully")
            return redirect('courses:add_course')
        else:
            messages.error(request, 'Failed to add course')
            return redirect('courses:add_course')

class ManageCourse(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'courses/manage_course.html'
    context_object_name = 'course_list'

class CourseUpdate(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ('course_name',)
    template_name = 'courses/course_edit.html'
    success_url = reverse_lazy('courses:manage_course')


class CourseDetail(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'courses/course_detail.html'

class CourseDelete(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'courses/course_delete.html'
    success_url = reverse_lazy('courses:manage_course')


class AddSubject(LoginRequiredMixin, CreateView):
    model = Subject
    fields = ('course', 'subject_name', 'staff')
    template_name = 'courses/add_subject.html'
    success_url = reverse_lazy('courses:manage_subject')

class SubjectDetail(LoginRequiredMixin, DetailView):
    model = Subject
    template_name = 'courses/subject_detail.html'
    context_object_name = 'subject'

class ManageSubject(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'courses/manage_subject.html'
    context_object_name = 'subjects'

class SubjectUpdate(LoginRequiredMixin, UpdateView):
    model = Subject
    fields = ('course', 'subject_name', 'staff')
    template_name = 'courses/edit_subject.html'
    success_url = reverse_lazy('courses:manage_subject')

class SubjectDelete(LoginRequiredMixin, DeleteView):
    model = Subject
    template_name = 'courses/subject_delete.html'
    success_url = reverse_lazy('courses:manage_subject')
