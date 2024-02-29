from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View

from .models import Item, Category, User
from .forms import ItemForm


# Create your views here.


def explore(request):
    return render(request, "explore.html")


def details(request):
    return render(request, "details.html")


def author(request):
    return render(request, "author.html")


def item_list(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'details.html', {'item': item})


class CreateItemView(LoginRequiredMixin, View):

    def get(self, request):
        form = ItemForm()
        return render(request, 'create.html', {"form": form})

    def post(self, request):
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = Item.objects.create(
                name=form.cleaned_data['name'],
                image=form.cleaned_data['image'],
                author=form.cleaned_data['author'],
                avatar=form.cleaned_data['avatar'],
                body=form.cleaned_data['body'],
                price=form.cleaned_data['price'],

                category=form.cleaned_data['category'],

            )
            item.category.set(form.cleaned_data['category'])
            item.author.set(form.cleaned_data['author'])
            item.save()

            return redirect('liberity:home')
        else:
            form = ItemForm(request.POST)
            return render(request, 'create.html', {'form': form})
