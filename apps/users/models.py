from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE

from .utils import avatar_path


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, AbstractModel):
    avatar = models.ImageField(upload_to=avatar_path, default='avatar.JPG')

    # @property
    # def post_count(self):
    #     return self.posts.count()