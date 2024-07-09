from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username'], name='unique_username')
        ]

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='journal_users',
        related_query_name='journal_user'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='journal_users',
        related_query_name='journal_user'
    )

class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name

class JournalEntry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journal_entries')

    def __str__(self):
        return self.title