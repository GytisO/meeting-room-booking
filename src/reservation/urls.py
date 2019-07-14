from django.urls import path
from .views import reservation_create_view, reservation_detail_view, reservation_list_view, reservation_update_view, reservation_delete_view


urlpatterns = [
    path('', reservation_list_view, name='reservation-list'),
    path('<int:r_number>/', reservation_detail_view, name='reservation-details'),
    path('<int:r_number>/update/',
         reservation_update_view, name='reservation-update'),
    path('<int:r_number>/delete/',
         reservation_delete_view, name='reservation-delete'),
    path('create/', reservation_create_view, name='reservation-create'),
]
