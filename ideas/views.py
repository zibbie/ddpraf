from django.shortcuts import render
from .models import Idea, Vote
from rest_framework import viewsets, generics
from .serializer import IdeaSerializer, VoteSerializer
from ideas import models




# Create your views here.

class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class IdeaList(generics.ListCreateAPIView):
    queryset = models.Idea.objects.all()
    serializer_class = IdeaSerializer

class VoteList(generics.ListCreateAPIView):
    queryset = models.Vote.objects.all()
    serializer_class = VoteSerializer

class IdeaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Idea.objects.all()
    serializer_class = IdeaSerializer

class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vote.objects.all()
    serializer_class = VoteSerializer

    