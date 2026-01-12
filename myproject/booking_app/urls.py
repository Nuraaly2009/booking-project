from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (
    UserProfileListAPIView,UserProfileDetailAPIView,
    RoomListAPIView,
    RoomDetailSerializer,
    ReviewCreateAPIView,ReviewEditAPIView,
    BookingViewSet, CityListAPIView, CityDetailAPIView, HotelListAPIView, HotelDetailAPIView, RoomDetailAPIView,
    HotelViewSet, RoomCreateViewSet,RegisterView, LoginView, LogoutView
)

# Router
router = SimpleRouter()
router.register(r'bookings', BookingViewSet),
router.register(r'hotel_create', HotelViewSet),
router.register(r'room_create', RoomCreateViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('city/', CityListAPIView.as_view(), name='city_list'),
    path('city/<int:pk>/', CityDetailAPIView.as_view(), name='city_detail'),
    path('hotels/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotels/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('rooms/', RoomListAPIView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', RoomDetailAPIView.as_view(), name='room_detail'),
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('reviews/', ReviewCreateAPIView.as_view(), name='create_review'),
    path('reviews/<int:pk>/', ReviewEditAPIView.as_view(), name='edit_review'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')

]