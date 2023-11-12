from django.urls import path#path describes what a url looks like
from . import views

#path() params are path(the path in the url, view function code to respond to requests, name of the path)
urlpatterns = [#list of urls that app will recognize
    path('', views.place_list, name='place_list'),#represents a request. '' is the homepage, use place_list function from views to handle requests to homepage.
    path('about', views.about, name='about'),
    path('visited', views.places_visited, name='places_visited'),
    path('place/<int:place_pk>/was_visited/', views.place_was_visited, name='place_was_visited'),#place_pk is a stand in for a variable name which is an int
    path('place/<int:place_pk>', views.place_details, name='place_details'),#using <> stand-ins is called capturing
    path('place/<int:place_pk>/delete', views.delete_place, name="delete_place")#each url must be unique, as in '/delete' makes is unique
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:#running local  development server? static routes on local computer defined in settings used
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


