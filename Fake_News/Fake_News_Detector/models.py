from django.db import models

# Create your models here.
class Article(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Article #{self.pk}"