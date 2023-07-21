from django.urls import path

# Local
from .views import GameView,GameListView, about, MainView


urlpatterns = [
    path('', MainView.as_view()),
    path('about/', about),
    path('shop/<int:game_id>/',GameView.as_view()),
    path('shop/', GameListView.as_view()),
]
