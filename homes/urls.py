from django.conf.urls import url
from django.views.generic import TemplateView
from homes.views import HomeDetail, HomeSearchListView

urlpatterns = [

    url(r'^property-listing/', HomeSearchListView.as_view
        (template_name='property-listing.html'), name='list'),
    url(r'^user-account/', TemplateView.as_view
        (template_name='user-overview.html'), name='profile'),
    url(r'^(?P<home_id>[0-9]+)/', HomeDetail.as_view(), name="detail"),

]
