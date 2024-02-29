from django.contrib import admin

# Register your models here.
from apps.users.models import User
from apps.liberity.models import Category, Item
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

