from django.urls import path
# from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView, RecipeDeleteView
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView, RecipeDeleteView, SignUpView, SearchView
# app_name = 'recipes' 
urlpatterns = [
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path("recipe/<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("recipe/<int:pk>/edit/", RecipeUpdateView.as_view(), name="update_recipe"),
    path("recipe/<int:pk>/delete/", RecipeDeleteView.as_view(), name="delete_recipe"),
    path("recipe/new/", RecipeCreateView.as_view(), name="new_recipe"),
    path("home/", RecipeListView.as_view(), name="home"),
    path("search/", SearchView.as_view(), name="search_results"),
]
