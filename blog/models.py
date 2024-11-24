from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class PostLikes(models.Model):
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_liked = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

class PostComments(models.Model):
    post_commented = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
