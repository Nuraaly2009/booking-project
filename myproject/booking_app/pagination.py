from rest_framework.pagination import PageNumberPagination


class RoomPagination(PageNumberPagination):
    page_size = 4

class HotelPagination(PageNumberPagination):
    page_size = 4
