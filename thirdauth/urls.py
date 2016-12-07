from django.conf.urls import include,url
from django.contrib import admin
from . import views
admin.autodiscover()
urlpatterns=[
        url(r'^admin/',admin.site.urls),
    url(r'^editprofile/$', views.update_profile, name="login"),
    url(r'^login/$', views.form_login, name="login"),
    url(r'^logout/$', views.form_logout, name="logout"),
    url(r'^register/$', views.signup, name="signup"),
		url(r'^', include('django.contrib.auth.urls', namespace='auth')),
		url(r'^', include('social.apps.django_app.urls', namespace='social')),
        url(r'^',views.home,name='home'),

        ]
