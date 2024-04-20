from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs' ),
    path('<int:blog_id>/', views.detail, name='detail'),
    
] 

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)