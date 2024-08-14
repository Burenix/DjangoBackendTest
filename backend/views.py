from rest_framework.viewsets import ModelViewSet

from backend.models import *
from backend.serializers import PeopleSerializer


# Create your views here.
class PeopleList(ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer