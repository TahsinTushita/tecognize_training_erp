from django.conf.urls import url
from training_backend import views

urlpatterns = [
    url(r"^api/instructors$", views.instructor_list),
    url(r"^api/instructors/(?P<pk>[a-zA-Z0-9_]+)$", views.instructor_detail),
    url(r"^api/instructors-count$", views.instructor_count),
    url(r"^api/users$", views.user_list),
    url(r"^api/users/(?P<pk>[a-zA-Z0-9_]+)$", views.user_detail),
    url(r"^api/users-count$", views.user_count),
    url(r"^api/categories$", views.category_list),
    url(r"^api/categories/(?P<pk>[a-zA-Z0-9_]+)$", views.category_detail),
    url(r"^api/categories-count$", views.category_count),
    url(r"^api/courses$", views.course_list),
    url(r"^api/courses/(?P<pk>[a-zA-Z0-9_]+)$", views.course_detail),
    url(r"^api/courses-count$", views.course_count),
    url(r"^api/batches$", views.batch_list),
    url(r"^api/batches/(?P<pk>[a-zA-Z0-9_]+)$", views.batch_detail),
    url(r"^api/batches-count$", views.batch_count),
    url(r"^api/retail-customers$", views.retail_customer_list),
    url(r"^api/retail-customers/(?P<pk>[a-zA-Z0-9_]+)$", views.retail_customer_detail),
    url(r"^api/retail-customers-count$", views.retail_customer_count),
    url(r"^api/corporate-customers$", views.corporate_customer_list),
    url(
        r"^api/corporate-customers/(?P<pk>[a-zA-Z0-9_]+)$",
        views.corporate_customer_detail,
    ),
    url(r"^api/corporate-customers-count$", views.corporate_customer_count),
]
