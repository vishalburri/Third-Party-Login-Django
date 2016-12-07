from django.conf.urls import include,url
from django.contrib import admin
from . import views
admin.autodiscover()
urlpatterns=[
		url(r'^', include('django.contrib.auth.urls', namespace='auth')),
		url(r'^', include('social.apps.django_app.urls', namespace='social')),
        url(r'^',views.home,name='home'),
        url(r'^admin/',admin.site.urls),
        ]
