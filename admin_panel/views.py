from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import Author
from .forms import AuthorForm
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

class AuthorListView(ListView):
    model = Author
    template_name = 'dashboard/author/author.html'
    context_object_name = 'authors'
    queryset = Author.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_form'] = AuthorForm()  
        context['edit_form'] = AuthorForm() 
        return context

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('author')  

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
    
class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('author')  # Redirect after successful edit

    def get(self, request, *args, **kwargs):
        # Check if it's an AJAX request
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Fetch the author object for AJAX requests
            author = get_object_or_404(Author, uuid=self.kwargs['uuid'])
            
            # Prepare the data to send as JSON
            response_data = {
                'uuid': author.uuid,
                'name': author.name,
                'dob': author.dob,
                'country': author.country.name if author.country else None,  # Handle None case
                'image': author.image.url if author.image else None,
            }
            return JsonResponse(response_data)
        
        # For non-AJAX requests, continue with normal handling
        return super().get(request, *args, **kwargs)


    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'message': 'Author updated successfully!'})
        return response

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'errors': form.errors}, status=400)
        return super().form_invalid(form)
    
class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author')  

    def get_success_url(self):
        messages.error(self.request, "Author deleted successfully!")
        return super().get_success_url()


    

    
