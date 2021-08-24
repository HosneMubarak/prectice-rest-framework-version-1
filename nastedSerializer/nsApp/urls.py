from django.urls import path
from .views import *
urlpatterns = [
    path('book', BookListView.as_view()),
    path('book/<int:pk>', BookDetails.as_view()),
    path('author', AuthorListView.as_view()),
    path('book/<int:pk>', AuthorDetails.as_view()),
]
