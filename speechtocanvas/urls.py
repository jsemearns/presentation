from django.conf.urls import patterns, include, url

from django.contrib import admin
from speechtocanvas import views

admin.autodiscover()

urlpatterns = patterns(
    "",
    # Examples:
    # url(r'^$', 'jscanvas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r"^admin/", include(admin.site.urls)),
    # url(r"^$", views.HomePageView.as_view(), name="home"),
    # url(r"^snake/", views.SnakeTemplateView.as_view(), name="snake"),
    # url(r"^tetris/", views.TetrisTemplateView.as_view(), name="tetris"),
)
