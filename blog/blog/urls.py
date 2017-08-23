from django.conf.urls import include, url
from django.contrib import admin
from posts.views import home, create, detail, user_contacts


urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name="home"),
    url(r'^create/$', create, name="create"),
    url(r'^google-contacts/$', user_contacts, name="google-contacts"),
    url(r'^(?P<pk>[\d]+)/$', detail, name='detail'),
    url(r'^accounts/', include('allauth.urls')),
]
