from django.urls import path

from Ride import views

urlpatterns = [
    # login
    path('myrides/', views.myrides, name='myrides'),
    path('setting/', views.setting, name='setting'),
    path('request_ride/', views.request_ride, name='request_ride'),
    path('edit_account/',views.edit_account,name='edit_account'),
    path('edit_driver/',views.edit_driver,name='edit_driver'),

    path('ride_detail/<uuid:pk>',views.ride_detail, name='ride_detail'),
    path('ride_detail/edit/<uuid:pk>',views.edit_detail, name='edit_detail'),
    path('search_ride/',views.search_ride,name='search_ride'),
    path('search_ride/driver/',views.search_ride_driver, name='search_ride_driver'),
    path('search_ride/sharer/',views.search_ride_sharer, name='search_ride_sharer'),
]
