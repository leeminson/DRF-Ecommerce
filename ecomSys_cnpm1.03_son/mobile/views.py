from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from mobile.models import Mobile
from mobile.serializer import MobileSerializer
class MobileView(APIView):  

    def get(self, request, id=None):  
        if id is not None:
            result = Mobile.objects.get(id=id)  
            serializers = MobileSerializer(result)  
            return Response({'success': 'success', "mobile":serializers.data}, status=200)  
        else:
            result = Mobile.objects.all()  
            serializers = MobileSerializer(result, many=True)  
            return Response({'status': 'success', "mobile":serializers.data}, status=200)  