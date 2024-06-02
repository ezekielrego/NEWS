from django.urls import path
from . import views
from .models import latestnews
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.index , name = "index.html"),
    path("index.html", views.index , name = "index.html"),
    path("contact.html", views.contact , name = "contact.html"),
    path("about.html", views.about , name = "about.html"),
    path("news-detail/<int:pk>",views.NewsDetail.as_view(), name = "news-detail"),
    path("act-detail/<int:pk>",views.activitydet.as_view(), name = "act-detail"),

  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)