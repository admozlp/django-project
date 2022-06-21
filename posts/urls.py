from django.urls import path
from .views import  *

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('detail/<int:pk>/<slug:slug>',PostView.as_view(),name='detail'),
    path('post-update/<int:pk>/<slug:slug>',PostUpdateView.as_view(),name='post_update'),
    path('post-delete/<int:pk>/<slug:slug>',PostDeleteView.as_view(),name='post_delete'),
    path('category/<int:pk>/<slug:slug>',CategoryDetail.as_view(),name='category_detail'),
    path('tag/<int:pk>/<slug:slug>',TagDetail.as_view(),name='tag_detail'),
    path('post-create',CreatePostView.as_view(),name='create_post'),
    path('search/',SearchView.as_view(),name="search")
]