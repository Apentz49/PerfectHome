from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from homes.views import HomeList

urlpatterns = [

    url(r'^register', 'homes.views.create_user', name='user_reg'),
    url(r'^login', auth_views.login, {'extra_context': {'next': '/'}},
        name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^homes/', include('homes.urls')),
    url(r'^$', HomeList.as_view(), name='index'),
]
