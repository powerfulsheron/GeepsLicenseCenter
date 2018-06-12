from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^licenseCenter$', views.formulaire, name='formulaire'),
    url(r'^versions/(?P<id>[-\w]+)/getReleaseListByLogiciel/',views.getReleaseListByLogiciel),
]