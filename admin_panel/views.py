from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import Author,Genre,Type
from .forms import AuthorForm,GenreForm,TypeForm
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

class BookView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/book/book.html'

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     # Add success message
    #     messages.success(self.request, "Author created successfully!")
    #     return response
    
    # def form_invalid(self, form):
    #     # When form is invalid, add an error message and pass the form to the context
    #     messages.error(self.request, "There was an error with your form submission.")
    #     return super().get_success_url()

# Author
# class AuthorView(LoginRequiredMixin, TemplateView):
#     template_name = 'dashboard/author/author.html'

class AuthorListView(LoginRequiredMixin, ListView):
    model = Author
    template_name = 'dashboard/author/author.html'
    context_object_name = 'authors'
    # queryset = Author.objects.all().order_by('-created_at')
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Author.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_form'] = AuthorForm()  
        context['edit_form'] = AuthorForm() 
        return context

class AuthorCreateView(LoginRequiredMixin,CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('author')  
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Author Created successfully!")
        # Add success message
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Check if the request is an AJAX request
            return JsonResponse({'message': 'Author created successfully!'})
        return response

    def form_invalid(self, form):
        # Handle form errors
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'errors': form.errors}, status=400)
        return super().form_invalid(form)
    
class AuthorUpdateView(LoginRequiredMixin,UpdateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('author')  
    login_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        # Fetch the author object using the UUID from the URL
        return get_object_or_404(Author, uuid=self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        # Check if it's an AJAX request
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Fetch the author object for AJAX requests
            author = get_object_or_404(Author, uuid=self.kwargs['pk'])
            
            # Prepare the data to send as JSON
            response_data = {
                'uuid': author.uuid,
                'name': author.name,
                'dob': author.dob,
                'bio': author.bio,
                'country': author.country.code if author.country else None,  # Handle None case
                'image': author.image.url if author.image else None,
            }
            return JsonResponse(response_data)
        
        # For non-AJAX requests, continue with normal handling
        return super().get(request, *args, **kwargs)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.warning(self.request, "Author Updated successfully!")
        # Add success message
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Check if the request is an AJAX request
            return JsonResponse({'message': 'Author created successfully!'})
        return response

    def form_invalid(self, form):
        # Handle form errors
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'errors': form.errors}, status=400)
        return super().form_invalid(form)
    
class AuthorDeleteView(LoginRequiredMixin,DeleteView):
    model = Author
    success_url = reverse_lazy('author')  
    login_url = reverse_lazy('login')

    def get_success_url(self):
        messages.error(self.request, "Author deleted successfully!")
        return super().get_success_url()

# Genre
class GenreListView(LoginRequiredMixin,ListView):
    model = Genre
    template_name = 'dashboard/genre/genre_list.html'
    context_object_name = 'genres'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Genre.objects.all().order_by('-created_at')

class GenreCreateView(LoginRequiredMixin,CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'dashboard/genre/genre_form.html'
    success_url = reverse_lazy('genre_list')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Genre created successfully!")
        return super().form_valid(form)

class GenreUpdateView(LoginRequiredMixin,UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'dashboard/genre/genre_form.html'
    success_url = reverse_lazy('genre_list')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.warning(self.request, "Genre updated successfully!")
        return super().form_valid(form)

class GenreDeleteView(LoginRequiredMixin, DeleteView):
    model = Genre
    template_name = 'dashboard/genre/genre_confirm_delete.html'
    success_url = reverse_lazy('genre_list')
    login_url = reverse_lazy('login')

    def get_success_url(self):
        messages.error(self.request, "Genre deleted successfully!")
        return super().get_success_url()

# Type
class TypeListView(LoginRequiredMixin,ListView):
    model = Type
    template_name = 'dashboard/type/type_list.html'
    context_object_name = 'types'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Type.objects.all().order_by('-created_at')

class TypeCreateView(LoginRequiredMixin,CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'dashboard/type/form.html'
    success_url = reverse_lazy('type_list')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Type created successfully!")
        return super().form_valid(form)

class TypeUpdateView(LoginRequiredMixin,UpdateView):
    model = Type
    form_class = TypeForm
    template_name = 'dashboard/type/form.html'
    success_url = reverse_lazy('type_list')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.warning(self.request, "Type updated successfully!")
        return super().form_valid(form)

class TypeDeleteView(LoginRequiredMixin, DeleteView):
    model = Type
    template_name = 'dashboard/type/confirm_delete.html'
    success_url = reverse_lazy('type_list')
    login_url = reverse_lazy('login')

    def get_success_url(self):
        messages.error(self.request, "Type deleted successfully!")
        return super().get_success_url()
    
