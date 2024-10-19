from django.urls import path
from . import views

urlpatterns = [
    path('blogs/',views.BlogListCreateView.as_view()),
    path('blogs/<int:pk>/',views.BlogDetailView.as_view()),
    path('blogs/<int:blog_id>/comments/',views.BlogCommentListView.as_view()),
    path('comments/',views.CommentCreateView.as_view()),
    path('profiles/',views.ProfileListView.as_view()),
    path('profiles/<int:pk>/',views.ProfileDetailView.as_view()),
]