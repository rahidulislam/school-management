# from django.contrib import messages
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import authenticate, login, logout
# from django.urls import reverse, reverse_lazy
# from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.mixins import LoginRequiredMixin
# from accounts.models import User, Staff, Student
# from accounts.forms import StaffUpdateForm, StudentAddForm, StudentUpdateForm, StaffAddForm
# from courses.models import Course
#
# class Home(LoginRequiredMixin, TemplateView):
#     template_name = "accounts/home.html"
#
#
# class LoginView(FormView):
#     form_class = AuthenticationForm
#     template_name = 'accounts/login.html'
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(data=request.POST)
#
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#                 login(request, user)
#                 return redirect('accounts:home')
#         else:
#             context = {
#                 'form': self.form_class
#             }
#             return render(request, self.template_name, context)
#
#
# class LogoutView(LoginRequiredMixin, FormView):
#     form_class = AuthenticationForm
#     template_name = 'accounts/login.html'
#
#     # login_url = reverse_lazy('accounts:login')
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect('accounts:login')
#
#
# class StaffAdd(LoginRequiredMixin, CreateView):
#     model = Staff
#     form_class = StaffAddForm
#     template_name = "accounts/add_staff.html"
#
#     def form_valid(self, form):
#         first_name = form.cleaned_data['first_name']
#         last_name = form.cleaned_data['last_name']
#         username = form.cleaned_data['username']
#         email = form.cleaned_data['email']
#         password = form.cleaned_data['password']
#         address = form.cleaned_data['address']
#         profile_image = form.cleaned_data['profile_image']
#
#         try:
#             user = form.save(commit=False)
#             user.user_type = 2
#             user.save()
#             staff = Staff.objects.get(admin=user)
#             staff.address = address
#             staff.profile_image = profile_image
#             staff.save()
#             messages.success(self.request, 'Successfully Staff Added', extra_tags='alert alert-success')
#             return redirect('accounts:manage_staff')
#         except:
#             messages.error(self.request, 'Failed to add staff', extra_tags='alert alert-danger')
#
#
#
#
# class ManageStaff(LoginRequiredMixin, ListView):
#     model = Staff
#     template_name = 'accounts/manage_staff.html'
#     context_object_name = 'staff_list'
#
#
# class StaffUpdate(LoginRequiredMixin, UpdateView):
#     model = Staff
#     form_class = StaffUpdateForm
#     template_name = "accounts/staff_edit.html"
#     success_url = reverse_lazy('')
#     def get_initial(self):
#         initial = super(StaffUpdate, self).get_initial()
#         staff = get_object_or_404(Staff, pk=object.pk)
#         initial['first_name'] = staff.admin.first_name
#         initial['last_name'] = staff.admin.last_name
#         initial['username'] = staff.admin.username
#         initial['email'] = staff.admin.email
#         return initial
#
#
#
# class StudentAdd(LoginRequiredMixin, CreateView):
#     model = Student
#     form_class = StudentAddForm
#     template_name = "accounts/add_student.html"
#
#     def form_valid(self, form):
#         first_name = form.cleaned_data['first_name']
#         last_name = form.cleaned_data['last_name']
#         username = form.cleaned_data['username']
#         email = form.cleaned_data['email']
#         password = form.cleaned_data['password']
#         gender = form.cleaned_data['gender']
#         address = form.cleaned_data['address']
#         course = form.cleaned_data['course']
#         session_start = form.cleaned_data['session_start']
#         session_end = form.cleaned_data['session_end']
#         profile_image = form.cleaned_data['profile_image']
#
#         try:
#             user = CustomUser.objects.create_user(
#                 username=username,
#                 email=email,
#                 password=password,
#                 first_name=first_name,
#                 last_name=last_name,
#                 user_type=3
#             )
#             user.student.gender = gender
#             course_obj = Course.objects.get(course_name=course)
#             user.student.course = course_obj
#             user.student.address = address
#             user.student.session_start = session_start
#             user.student.session_end = session_end
#             user.student.profile_image = profile_image
#             user.save()
#             print(user)
#             messages.success(self.request, 'Successfully Added', extra_tags='alert alert-success')
#             return redirect(reverse('accounts:add_student'))
#
#         except:
#             messages.error(self.request, 'Failed to Add Student', extra_tags='alert alert-danger')
#             return redirect(reverse('accounts:add_student'))
#
# class ManageStudent(LoginRequiredMixin, ListView):
#     model = Student
#     template_name = "accounts/manage_student.html"
#     context_object_name = 'student_list'
#
# class StudentUpdate(LoginRequiredMixin, UpdateView):
#     model = Student
#     form_class = StudentUpdateForm
#     template_name = "accounts/student_edit.html"
#
#     def get_initial(self):
#         initial = super(StaffUpdate, self).get_initial()
#         student = get_object_or_404(Student, pk=object.pk)
#         initial['first_name'] = student.admin.first_name
#         initial['last_name'] = student.admin.last_name
#         initial['username'] = student.admin.username
#         initial['email'] = student.admin.email
#         return initial
#
#
#
