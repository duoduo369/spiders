from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spider_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('douban.urls')),
    url(r'^authenticate$', views.Login.as_view()),
    url(r'^logout$', views.Logout.as_view()),
    url(r'^user$', views.UserDetail.as_view()),
    url(r'^register$', views.Register.as_view()),
    url(r'^test_view$', views.TestApi.as_view()),
)
