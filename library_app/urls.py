from django.urls import path
from .views import BookFormView, BookListView   


urlpatterns = [
   path('', BookListView.as_view(), name='list_book'),
   path('agregar/', BookFormView.as_view(), name="add_book"),
]
