from django.urls import reverse_lazy
from django.views import generic
from .forms import BookForm
from .models import Book



# Create your views here.
class BookFormView(generic.FormView):
    template_name = "library_app/add_book.html" 
    form_class = BookForm 
    success_url = reverse_lazy('add_book')
    
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class BookListView(generic.ListView):
    model = Book
    template_name = "library_app/list_book.html"
    context_object_name = 'books'



        


