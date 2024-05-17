from django.urls import path
from webapp.views import HomeView, TagView, TagCreateView, TagUpdateView, TagDeleteView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tag/<int:pk>/', TagView.as_view(), name='detail'),
    path('tag/create/', TagCreateView.as_view(), name='create'),
    path('tag/<int:pk>/update/', TagUpdateView.as_view(), name='update'),
    path('tag/<int:pk>/delete/', TagDeleteView.as_view(), name='delete'),
]
