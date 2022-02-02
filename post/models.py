from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from datetime import datetime

from slugger import AutoSlugField

# Create your models here.



class Post(models.Model):
    STATUS_CHOICES = (
        ('Published', 'Published'),
        ('Draft', 'Draft'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    body = models.TextField()

    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Draft')

    published = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(default=datetime.now, blank=True)
    updated = models.DateTimeField(auto_now=True)

    image = models.ImageField(upload_to='images/',blank=False)


    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True)


# kwargs={'slug': self.slug},  args=[self.slug]

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    body = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.body

    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)
 