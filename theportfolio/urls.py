from django.urls import path
from . import views
from .views import HomeView, PostsListView, SinglePostDetailView, EditPostView, CreatePostView, RemovePostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('posts/', PostsListView.as_view(), name="post_list"),
    path('posts/<int:pk>/', SinglePostDetailView.as_view(), name="post_single"),
    path('create_post/', CreatePostView.as_view(), name="create_post"),
    path('editar/posts', EditPostView.as_view(), name="edit_post"),
    path('excluir/<int:pk>', RemovePostView.as_view(), name="remove_post"),
]
