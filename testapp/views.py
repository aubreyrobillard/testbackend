from .models import Test
from .serializers import TestSerializer
from rest_framework import permissions
from rest_framework import viewsets

# Create your views here.
class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permissions_classes = [permissions.AllowAny]
