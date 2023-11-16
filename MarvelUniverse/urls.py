from django.urls import path
from .views.homepage import HomePageView
from .views.see_all import AllCharactersView, AllComicsView, AllSeriesView


app_name = "MarvelUniverse"
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('characters/', AllCharactersView.as_view(), name="characters"),
    path('comics/', AllComicsView.as_view(), name="comics"),
    path('series/', AllSeriesView.as_view(), name="series"),          
]