from django.urls import path
from .views import BookmarkListView

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkListView.as_view(), name='add'),
    path('detail/<int:pk>', BookmarkListView.as_view(), name='detail'),
    path('update/<int:pk>', BookmarkListView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkListView.as_view(), name='delete'),
]