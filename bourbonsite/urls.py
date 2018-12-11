from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.bourbon_list, name='bourbon_list'),
    url(r'^bourbon/(?P<BourbonID>\w+)$', views.bourbon_detail, name='bourbon_detail'),
    url(r'^bourbon/(?P<BourbonID>\w+)/add_review$', views.add_review, name='add_review'),
    url(r'^reviews$', views.review_list, name='review_list'),
    url(r'^reviews/(?P<RatingID>\d+)$', views.review_detail, name='review_detail'),
    url(r'^reviews/user/$', views.user_review_list, name='user_review_list'),
    url(r'^reviews/user/(?P<username>\w+)$', views.user_review_list, name='user_review_list'),
    url(r'^recommendations$', views.user_recommendations, name='user_recommendations'),

]