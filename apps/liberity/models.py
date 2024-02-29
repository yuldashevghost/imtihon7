from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE
from apps.users.models import AbstractModel, User
from apps.users.utils import avatar_path


# Create your models here.
class Category(AbstractModel):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Item(AbstractModel):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to=avatar_path, default='image')
    author = models.ForeignKey(User, on_delete=CASCADE, related_name='items')
    avatar = models.ImageField(upload_to=avatar_path, default='avatar')
    body = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=CASCADE)

    def __str__(self):
        return self.name