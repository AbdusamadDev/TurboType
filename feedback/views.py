from rest_framework.views import APIView
from rest_framework.response import Response
#from django.http import HttpResponse

# Create your views here.


class FeedbackAPIView(APIView):
    def get(self,request):
        return Response({"msg":"FeedbackAPIView"})  