from rest_framework import generics, permissions
from .models import JournalEntry, Category, User
from .serializers import JournalEntrySerializer, CategorySerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from datetime import datetime, timedelta

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class JournalEntryListCreateView(generics.ListCreateAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class JournalEntryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class SummaryView(generics.ListAPIView):
    serializer_class = JournalEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        period = self.request.query_params.get('period', 'daily')
        today = datetime.today()
        if period == 'daily':
            start_date = today - timedelta(days=1)
        elif period == 'weekly':
            start_date = today - timedelta(days=7)
        elif period == 'monthly':
            start_date = today - timedelta(days=30)
        else:
            start_date = today - timedelta(days=1)
        
        return JournalEntry.objects.filter(user=self.request.user, date__gte=start_date)
