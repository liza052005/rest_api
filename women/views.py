from django.shortcuts import render
# from rest_framework import generics
# from .models import Women
# from .serializers import WomenSerializer
#
# class WomenApiView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#

from rest_framework.views import APIView
from rest_framework.response import Response

class WomenApiView(APIView):
    def get(self, request):
        return Response({'title':'hui'})