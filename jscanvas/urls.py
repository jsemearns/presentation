from django.conf.urls import patterns, include, url

from django.contrib import admin
from bangon import views

admin.autodiscover()

urlpatterns = patterns(
    "",
    # Examples:
    url(r"^justinadmin/", include(admin.site.urls)),
    url(r"^$", views.BangonHomePageView.as_view(), name="index"),
    url(
        r"^areas/(?P<city>[\w-]+)/$",
        views.BangonAreaTemplateView.as_view(),
        name="city_areas",
    ),
    url(
        r"^area_detail/(?P<area>[\w-]+)/$",
        views.BangonAreaDetailTemplateView.as_view(),
        name="area_detail",
    ),
)
