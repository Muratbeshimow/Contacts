from django.urls import path

from . import views

urlpatterns = [
    path('create/', view=views.create, name="create"),
    path('update/', view=views.update, name="update"),
    path('delete/', view=views.delete, name="delete"),
    path('', view=views.home, name="home"),
]
