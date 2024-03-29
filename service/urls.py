from django.urls import path
from service import views


urlpatterns = [
  path('', views.CargoListView.as_view(), name='cargo_list'),
  path('cargo/<int:pk>/', views.CargoDetailViews.as_view(), name='cargo_detail'),
  path('addcargo/', views.CargoCreateView.as_view(), name='cargo_create'),
  path('deletecargo/<int:pk>/', views.CargoDeleteView.as_view(), name='cargo_delete'),
  path('updatecargo/<int:pk>/', views.CargoUpdateView.as_view(), name='cargo_update'),
  path('carlist/', views.CarListView.as_view(), name='car_list'),
  path('car/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
  path('addcar/', views.CarCreateView.as_view(), name='car_create'),
  path('carupdate/<int:pk>/', views.CarUpdateView.as_view(), name='car_update'),
  path('deletecar/<int:pk>/', views.CarDeleteView.as_view(), name='car_delete'),

]