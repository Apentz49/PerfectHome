from django.conf.urls import url
from homes.views import HomeDetail, HomeSearchListView

urlpatterns = [

    url(r'^property-listing/$', HomeSearchListView.as_view
        (template_name='property-listing.html'), name='list'),
    url(r'^property-listing/(?P<home_id>[0-9]+)/like', 'homes.views.home_like',
        name='likes'),
    url(r'^property-listing/(?P<home_id>[0-9]+)/dislike',
        'homes.views.home_dislike', name='dislikes'),
    url(r'^user-account/(?P<user_id>[0-9]+)', 'homes.views.profile_view',
        name='profile'),
    url(r'^likes/(?P<user_id>[0-9]+)',
        'homes.views.profile_view_likes', name='userlikes'),
    url(r'^dislikes/(?P<user_id>[0-9]+)', 'homes.views.profile_view_dislikes',
        name='userdislikes'),
    url(r'^(?P<home_id>[0-9]+)/', HomeDetail.as_view(), name="detail"),

]
