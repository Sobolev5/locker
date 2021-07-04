from django.conf.urls import url

from encrypt import views

urlpatterns = [
    url(r"^$", views.add_record, name="add_record"),
    url(r"^(?P<uuid>[a-zA-Z0-9_-]{22})/$", views.view_record, name="view_record"),
    url(r"^delete/(?P<uuid>[a-zA-Z0-9_-]{22})/(?P<md5_key>[A-Za-z0-9]{32})/$", views.delete_record, name="delete_record"),
]
