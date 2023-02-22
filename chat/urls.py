from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login",views.login,name="login"),
    path("<str:room_name>/", views.room, name="room"),
    path('start_chat/<str:username>',views.startchat,name="start_chat")
]