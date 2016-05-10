
from django.conf.urls import include, url
from web import views

urlpatterns = [
    url(r'^$', 'web.views.index'),
]
