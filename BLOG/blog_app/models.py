from django.db import models

class blog_posts(models.Model):
    title=models.CharField(max_length=150)
    desc=models.TextField()