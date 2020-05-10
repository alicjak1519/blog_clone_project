from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about', views.AboutView.as_view(), name='about'),
    path('post/<str:pk>', views.PostDetailView, name='post_detail'),
    path('post/create', views.PostCreateView, name='post_create'),
    path('post/<str:pk>/edit', views.PostUpdateView, name='post_edit'),
    path('post/<str:pk>/delete', views.PostDeleteView, name='post_delete'),
    path('drafts', views.DraftListView, name='post_draft_list'),
    path('post/<str:pk>/comment', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<str:pk>/approve', views.comment_approve, name='comment_approve'),
    path('comment/<str:pk>/delete', views.comment_remove, name='comment_remove'),
    path('post/<str:pk>/publish', views.post_published, name='post_publish')
]
