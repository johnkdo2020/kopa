from django.urls import path
from rest_framework import routers

from tours.apis.review_apis import ReviewAPIView
from tours.apis.place_apis import PlaceAPIView, PlaceDetailAPIView, PlaceCreateAPIView, PlaceDeleteAPIView
from tours.views import tourAPI

urlpatterns = [
    path('', tourAPI),
    path('places/', PlaceAPIView.as_view()),
    path('places/create/', PlaceCreateAPIView.as_view()),
    path('places/<int:pk>/', PlaceDetailAPIView.as_view()),
    path('places/<int:pk>/delete/', PlaceDeleteAPIView.as_view()),
]

router = routers.SimpleRouter()
router.register('review', ReviewAPIView)

urlpatterns += router.urls
