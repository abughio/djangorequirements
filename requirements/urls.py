from django.urls import path

from . import views


urlpatterns = [
    path('usecase/create/', views.create_usecase, name="usecase-create"),

]
