from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.decorators import api_view

class ContentsAPIView(APIView):
    def get(self,request):
     return Response({"msg":"ContentsAPIView"})

@api_view(["GET"])
def home(request):
    return Response({"HI": "Hello Home"}, status=200)    

