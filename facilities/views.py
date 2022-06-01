from django.shortcuts import render
from facilities.models import Facilities
# Create your views here.

def index(request):
    data = Facilities.objects.filter().all()
    from School_Management import settings
    media_url = settings.MEDIA_URL
    return render(request, 'facilities_index.html', {'data': data, 'media_url': media_url})



from rest_framework.generics import ListAPIView
from .serializers import FacilitiesSerilaizer
from rest_framework.response import Response
class IndexApi(ListAPIView):
    permission_classes = []
    def get(self,request):
        data_val = Facilities.objects.filter().all()
        data_val = FacilitiesSerilaizer(data_val, many=True).data
        return Response(data_val)