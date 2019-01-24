from django.urls import path

from . import views


urlpatterns = [
    path('usecase/create/', views.create_usecase, name="usecase-create"),
    path('usecase/list/',views.home,name='usecase-list'),
    path('usecase/scenarios/<int:usecase_id>/', views.manage_Scenarios, name="scenario-create"),

]
