
from django.conf.urls import include, url
from web import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)$', TemplateView.as_view(template_name='web/good_card.html')),
    url(r'^$', 'web.views.index'),
]
