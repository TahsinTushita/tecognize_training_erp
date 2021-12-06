from django.conf.urls import url
from training_backend import views

urlpatterns = [
    url(r"^api/instructors$", views.instructor_list),
    url(r"^api/instructors/(?P<pk>[a-zA-Z0-9_]+)$", views.instructor_detail),
    url(r"^api/instructors/count/total$", views.instructor_count),
]
