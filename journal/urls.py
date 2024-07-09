from django.urls import path
from .views import (
    UserCreateView,
    UserLoginView,
    JournalEntryListCreateView,
    JournalEntryRetrieveUpdateDestroyView,
    CategoryListCreateView,
    CategoryRetrieveUpdateDestroyView,
    SummaryView
)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-create'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('entries/', JournalEntryListCreateView.as_view(), name='entry-list-create'),
    path('entries/<int:pk>/', JournalEntryRetrieveUpdateDestroyView.as_view(), name='entry-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
    path('summary/', SummaryView.as_view(), name='summary'),
]
