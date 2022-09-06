
import email
from time import time
from turtle import title
from django.urls import reverse

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=200)
    creation_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    def __str__(self):
        return self.title

    def get_absolute_ulr(self):
        return reverse("comment_pk", kwargs= {"pk": self.pk})
           

    def coments(self):
        instance = self
        qs = Coment.objects.filter.instace_filter(instance)
        return qs 
    
    def get_content_type(self):
        content_type = ContentType.objects.get_for_model(Article)
        return content_type

class Advertising(models.Model):
    company = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

class CommentManager(models.Manager):
    def instance_filter(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id)
        
        return qs

class Coment(models.Model):
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    text = models.TextField(verbose_name="comentario")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    objects = CommentManager()
    
    def get_absolute_url(self):
        return reverse("comment_id", kwargs={"pk": self.pk})


    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']