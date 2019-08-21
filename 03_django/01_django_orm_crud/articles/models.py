from django.db import models

# Create your models here.

class Article(models.Model):
  # id = models.AutoField(primary_key=True) # 요건 안 써도 됨
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}번글 - {self.title} : {self.content}'
