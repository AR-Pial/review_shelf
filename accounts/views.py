from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views import View  
from .forms import UserRegistrationForm
from .models import CustomUserModel
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import Group

class CustomLoginView(View):  
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'user_pages/home.html')
        return render(request, 'accounts/login.html', {'form': form})
    

class UserRegistrationView(CreateView):
    model = CustomUserModel
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])  # Hash the password
        user.save()

        # Create or get the 'User' group
        user_group, created = Group.objects.get_or_create(name='User')
        user.groups.add(user_group)  # Add the user to the 'User' group

        return super().form_valid(form)
