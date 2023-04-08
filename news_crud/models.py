import uuid
from django.db import models
from news.settings import MEDIA_ROOT
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class NewsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    author = models.ForeignKey(UserModel, related_name='news', on_delete=models.CASCADE)
    source = models.TextField()
    image = models.ImageField(upload_to=f"uploads", null=True)
    date = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    user_updated = models.ForeignKey(UserModel, related_name='updated_news', on_delete=models.CASCADE)
    
    class Meta:
        db_table = "news"
        ordering = ['-date_created']

        def __str__(self) -> str:
            return f"{self.author} : {self.name}"