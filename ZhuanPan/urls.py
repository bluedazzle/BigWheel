from django.conf.urls import patterns, include, url
from ZhuanPan import views
from lucky import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lucky.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^verify$', views.verify),
    url(r'^index$', views.index),
    url(r'^first$', views.first),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.CSS_DIR}),
    url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.IMG_DIR}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.JS_DIR}),
)
