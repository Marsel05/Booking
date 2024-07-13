from django.contrib.auth.urls import path
from .views import *

urlpatterns = [


    path('userprofile/', UserProfileViewSets.as_view({'get': "list", 'post': 'create'}), name='userprofile_list'),
    path('userprofile/<int:pk>/', UserProfileViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': 'destroy'}), name='userprofile_detail'),

    path('book/', BookViewSets.as_view({'get': "list", 'post': 'create'}), name='book_list'),
    path('book/<int:pk>/',
         BookViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': 'destroy'}),
         name='book_detail'),

    path('member/', MemberViewSets.as_view({'get': "list", 'post': 'create'}), name='member_list'),
    path('member/<int:pk>/', MemberViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': 'destroy'}), name='member_detail'),

    path('loan/', LoanViewSets.as_view({'get': "list", 'post': 'create'}), name='loan_list'),
    path('loan/<int:pk>/', LoanViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': 'destroy'}), name='loan_detail'),

    path('fine/', FineViewSets.as_view({'get': "list", 'post': 'create'}), name='fine_list'),
    path('fine/<int:pk>/', FineViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': 'destroy'}), name='fine_detail'),

    path('reservation/', ReservationViewSets.as_view({'get': "list", 'post': 'create'}), name='reservation_list'),
    path('reservation/<int:pk>/', ReservationViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': 'destroy'}), name='reservation_detail'),
]