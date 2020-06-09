from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, DetailView, ListView, UpdateView

from accounts.models import CustomUser
from courses.forms import AddCourseForm
from courses.models import Subject


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


class AddSubject(LoginRequiredMixin, CreateView):
    model = Subject
    fields = ('course', 'subject_name', 'staff')
    template_name = 'courses/add_subject.html'
    success_url = reverse_lazy('courses:manage_subject')

class SubjectDetail(LoginRequiredMixin, DetailView):
    model = Subject
    template_name = 'courses/subject_detail.html'
    context_object_name = "subject"

class ManageSubject(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'courses/manage_subject.html'
    context_object_name = 'subjects'

class SubjectUpdate(LoginRequiredMixin, UpdateView):
    model = Subject
    fields = ('course', 'subject_name', 'staff')
    template_name = 'courses/add_subject.html'
    success_url = reverse_lazy('courses:manage_subject')