from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication


class ContactList(ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
    
    # def get(self):
    #     return Response({"msg": "GET"}) 


class ContactDetailView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)