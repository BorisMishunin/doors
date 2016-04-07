
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from web_api import views

urlpatterns = [
    url(r'^goods/$', views.GoodsList.as_view()),
    url(r'^goods/(?P<pk>[0-9]+)$', views.GoodsDetail.as_view()),
    url(r'^goods_images/$', views.GoodsImagesList.as_view()),
    url(r'^goods_images/(?P<good_pk>[0-9]+)/$', views.GoodsImagesList.as_view()),
    url(r'^goods_images/image/(?P<pk>[0-9]+)/$', views.GoodsImagesDetail.as_view(), name='payments_transcript-detail'),
    url(r'^actions/$', views.ActionsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)