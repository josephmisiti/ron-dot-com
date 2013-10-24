from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 	'apps.static.views.index', name='index'),
    url(r'^portfolio', 	'apps.static.views.portfolio', name='portfolio'),
    url(r'^videos', 	'apps.static.views.videos', name='videos'),
    url(r'^contact', 	'apps.static.views.contact', name='contact'),

    url(r'^rostam-one', 		'apps.static.views.portfolio_one', name='portfolio-one'),
    url(r'^robert', 			'apps.static.views.portfolio_two', name='portfolio-two'),
    url(r'^rostam-two', 		'apps.static.views.portfolio_three', name='portfolio-three'),
    url(r'^rostam-three', 		'apps.static.views.portfolio_four', name='portfolio-four'),
    url(r'^joey', 				'apps.static.views.portfolio_five', name='portfolio-five'),



)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
    )