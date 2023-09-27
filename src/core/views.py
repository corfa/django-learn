from rest_framework import generics
from .models import Contact, Group,User
from .serializers import ContactSerializer, GroupSerializer, UserSerializer
from rest_framework import permissions
from rest_framework import viewsets


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Contact.objects.all()

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

