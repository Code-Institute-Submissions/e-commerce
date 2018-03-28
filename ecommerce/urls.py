
from django.conf.urls import url, include
from django.contrib import admin
from products.views import all_products
from products.views import search_products
from accounts import urls as urls_accounts
from products import urls as urls_products
from reviews import urls as urls_reviews
from checkout import urls as urls_checkout
from cart import urls as urls_cart
from django.views import static
from django.views.static import serve
from django.conf import settings



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_products, name='home'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^search/', search_products, name='search'),
    url(r'^products/', include(urls_products)),
    url(r'^reviews/', include(urls_reviews)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^cart/', include(urls_cart)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]

