from django.shortcuts import render
from django.views.generic import ListView, DetailView #CreateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CustomUser, Recipe
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CategoryCreateView(CreateView):
    template_name = 'recipe/new_category.html'


class SearchView(ListView):
    model = Recipe
    template_name = 'recipe/search_results.html'
    context_object_name = 'recipe_list'
    # queryset = Recipe.objects.filter(name__icontains='vada')

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            recipe_list = Recipe.objects.filter(Q(name__icontains=query) | Q(categories__name__icontains=query))
            return recipe_list 
        else:
  	        query = ""

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe/recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe/recipe_detail.html'
    # context_object_name = 'recipe'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipe/recipe_new.html'
    fields = ['name', 'author', 'image', 'ingredients', 'instructions', 'categories',]
    def get_success_url(self):
        return reverse("home")

class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = 'recipe/recipe_edit.html'
    fields = ['name', 'author', 'image', 'ingredients', 'instructions', 'categories',]

class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe 
    template_name = 'recipe/recipe_delete.html'
    success_url = reverse_lazy('home')
