from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import CustomUser, Staff
from accounts.forms import AddStudentForm, StaffUpdateForm, CreateUserForm
from courses.models import Course

class Home(LoginRequiredMixin, TemplateView):
    template_name = "accounts/home.html"


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('accounts:home')
        else:
            context = {
                'form': self.form_class
            }
            return render(request, self.template_name, context)


class LogoutView(LoginRequiredMixin, FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    # login_url = reverse_lazy('accounts:login')
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('accounts:login')


class AddStaff(LoginRequiredMixin, CreateView):
    form_class = CreateUserForm
    template_name = "accounts/add_staff.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES)

        if form.is_valid():

            address = form.cleaned_data['address']
            profile_image = form.cleaned_data['profile_image']
            user = form.save(commit=False)
            user.user_type = 2
            user.save()
            staff = Staff.objects.get(admin=user)
            staff.address = address
            staff.profile_image = profile_image
            staff.save()
            messages.success(self.request, 'Successfully Staff Added', extra_tags='alert alert-success')
            return redirect('accounts:manage_staff')
        else:
            context ={
                'form': self.form_class
            }
            return render(request, self.template_name, context)



    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Successfully Staff Added', extra_tags='alert alert-success')
        return redirect('accounts:manage_staff')








class ManageStaff(LoginRequiredMixin, ListView):
    model = Staff
    template_name = 'accounts/manage_staff.html'
    context_object_name = 'staff_list'


class StaffUpdate(LoginRequiredMixin, UpdateView):
    model = Staff
    form_class = StaffUpdateForm
    template_name = "accounts/staff_edit.html"

    def post(self, request, *args, **kwargs):
        staff = get_object_or_404(Staff, pk=self.kwargs['pk'])
        form = self.form_class(data=request.POST, files=request.FILES, instance=staff)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            address = form.cleaned_data['address']
            profile_image = form.cleaned_data['profile_image']

            try:
                user = CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    user_type=2
                )
                user.staff.address = address
                user.staff.profile_image = profile_image
                user.save()
                print(user)
                return redirect('accounts:manage_staff')

            except:
                return redirect('accounts:staff_edit')

class AddStudent(LoginRequiredMixin, FormView):
    form_class = AddStudentForm
    template_name = "accounts/add_student.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            course = form.cleaned_data['course']
            session_start = form.cleaned_data['session_start']
            session_end = form.cleaned_data['session_end']
            profile_image = form.cleaned_data['profile_image']

            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                user_type=3
            )
            user.student.gender = gender
            course_obj = Course.objects.get(course_name=course)
            user.student.course=course_obj
            user.student.address = address
            user.student.session_start = session_start
            user.student.session_end = session_end
            user.student.profile_image = profile_image
            user.save()
            print(user)
            messages.success(request, 'Successfully Added', extra_tags='alert alert-success')
            return redirect(reverse('accounts:add_student'))

        else:
            messages.error(request, 'Failed to add student', extra_tags='alert alert-danger')
            context = {
                'form': self.form_class
            }
            return render(request, self.template_name, context)
