from django.conf.urls import url

from . import views

urlpatterns = [  # "agon_ratings.views",
    url(r"^(?P<content_type_id>\d+)/(?P<object_id>\d+)/rate/$", views.rate, name="agon_ratings_rate"),
]
