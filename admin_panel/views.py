from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Author
from .forms import AuthorForm

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

class BookView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/book/book.html'

# Author
# class AuthorView(LoginRequiredMixin, TemplateView):
#     template_name = 'dashboard/author/author.html'

class AuthorListView(ListView):
    model = Author
    template_name = 'dashboard/author/author.html'
    context_object_name = 'authors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_form'] = AuthorForm()  
        return context

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('author')  

    def form_valid(self, form):
        print("form validation")
        # Optionally, you can log or modify the form data before saving.
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("Form is invalid:", form.errors)  # Print errors if form is invalid
        return super().form_invalid(form)

    
