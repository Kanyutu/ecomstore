from django.conf.urls.defaults import *
from ecomstore import settings
import os
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from bookmarks.views import *
from bookmarks.feeds import *
from blog.views import create
admin.autodiscover()

site_media = os.path.join(
  os.path.dirname(__file__), 'site_media'
)

feeds = {
  'recent': RecentBookmarks,
  'user': UserBookmarks
}
urlpatterns = patterns('',
    # Example:
    # (r'^ecomstore/', include('ecomstore.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'^', include('ecomstore.catalog.urls')),
    (r'^cart/', include('cart.urls')),
    (r'^checkout/', include('checkout.urls')),
    (r'^accounts/', include('accounts.urls')),
    (r'^accounts/', include('django.contrib.auth.urls')),
    (r'^search/', include('search.urls')),
    (r'^billing/', include('billing.urls')),
    (r'^', include('marketing.urls')),
	# Browsing bookmarks
	url(r'^main_page/$', main_page),
	(r'^popular/$', popular_page),
	(r'^user/(\w+)/$', user_page),
	(r'^tag/([^\s]+)/$', tag_page),
	(r'^tag/$', tag_cloud_page),
	(r'^search/$', search_page),
	(r'^bookmark/(\d+)/$', bookmark_page),

	# Session management
	(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', logout_page),
	(r'^register/$', register_page),
	(r'^register/success/$', direct_to_template,
	{'template': 'registration/register_success.html'}),

	# Account management
	(r'^save/$', bookmark_save_page),
	(r'^vote/$', bookmark_vote_page),

	# Site media
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
	{'document_root': site_media}),

	# Ajax
	(r'^ajax/tag/autocomplete/$', ajax_tag_autocomplete),

	# Comments
	url(r'^comments/',
	include('django.contrib.comments.urls')),

	# Admin interface
	(r'^admin/(.*)', admin.site.urls),

	# Feeds
	(r'^feeds/(?P<url>.*)/$',
	'django.contrib.syndication.views.feed',
	{'feed_dict': feeds}),

	# Friends
	(r'^friends/(\w+)/$', friends_page),
	(r'^friend/add/$', friend_add),
	(r'^friend/invite/$', friend_invite),
	(r'^friend/accept/(\w+)/$', friend_accept),
    (r'^new/$',create),
    (r'^avatar/', include('avatar.urls')),

	)

	
	

if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root' : os.path.join(settings.CURRENT_PATH, 'static') }),
)

handler404 = 'ecomstore.views.file_not_found_404'
#handler500 = 'ecomstore.views.server_error_500'
