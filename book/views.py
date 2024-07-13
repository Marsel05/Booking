from rest_framework import viewsets, permissions
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class UserProfileViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers
    permission_classes = [permissions.IsAuthenticated]

class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = UserProfileSerializers
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'author', 'language']
    search_fields = ['book']

class MemberViewSets(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = UserProfileSerializers
    permission_classes = [permissions.IsAuthenticated]

class LoanViewSets(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = UserProfileSerializers
    permission_classes = [permissions.IsAuthenticated]

class FineViewSets(viewsets.ModelViewSet):
    queryset = Fine.objects.all()
    serializer_class = UserProfileSerializers
    permission_classes = [permissions.IsAuthenticated]

class ReservationViewSets(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = UserProfileSerializers
    permission_classes = [permissions.IsAuthenticated]
