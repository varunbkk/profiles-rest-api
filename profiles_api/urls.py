from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views



router = DefaultRouter()

router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

""" Don't need to specify base_name because this is based on a ModelViewSet"""
router.register('profile', views.UserProfileViewSet)


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
