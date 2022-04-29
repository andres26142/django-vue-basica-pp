from rest_framework.viewsets import ModelViewSet

from alm.models import Cliente

from alm.serializers import ClienteSerializer


class ClienteViewSet (ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all().order_by('id')
    filterset_fields = ['estado', ]
    fields = '__all__'
