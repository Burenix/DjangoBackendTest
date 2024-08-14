from django.urls import include, path

from rest_framework .routers import DefaultRouter

from backend.views import *

router = DefaultRouter()
router.register('test', PeopleList)

urlpatterns = [
    path('api/v1/', include(router.urls), name='people')
]