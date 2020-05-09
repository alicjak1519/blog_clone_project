from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about', views.AboutView),
    path('post/<str:pk>', views.PostDetailView, name='post_detail'),
    path('post/create', views.PostCreateView, name='post_create'),
    path('post/<str:pk>/edit', views.PostUpdatePost, name='post_edit'),
    path('post/<str:pk>/delete', views.PostDeletePost, name='post_delete'),
    path('drafts', views.DraftListView, name='post_draft_list'),
]
