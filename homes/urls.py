from django.conf.urls import url
from django.views.generic import TemplateView
from homes.views import HomeDetail

urlpatterns = [

    url(r'^property-listing/', TemplateView.as_view
        (template_name='property-listing.html'), name='list'),
    url(r'^single-property-listing/', TemplateView.as_view
        (template_name='single-property-listing.html'), name='detail'),
    url(r'^user-account/', TemplateView.as_view
        (template_name='user-overview.html'), name='profile'),
    url(r'^user-overview/', TemplateView.as_view
        (template_name='user-account.html'), name='account'),
    url(r'^(?P<home_id>[0-9]+)/', HomeDetail.as_view(), name="home_detail"),

]
