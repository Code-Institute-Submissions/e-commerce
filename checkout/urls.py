from django.conf.urls import url
from .views import checkout, view_order


urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^orders/(\d+)', view_order, name='show_order_details')
]


