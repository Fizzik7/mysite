from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.post_limit, name='post_limit'),
]
