from django.urls import path
from .views import FormClass, ListClass
from . import views

urlpatterns = [
    # path(route, view, kwargs=None, name=None)
    path('form/', FormClass.as_view(), name='form'),
    path('list/', ListClass.as_view(), name='list'),
    path("article/<int:pk>/edit/",views.edit,name="edit"),
]