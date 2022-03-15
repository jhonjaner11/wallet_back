from rest_framework.response import Response
from .serializers import RewardSerializer, transactionSerializer
from rest_framework.views import APIView
from rest_framework import status

from . models import transaction, reward


class rewardList(APIView):
    def get(self, request):
        list = reward.objects.all()
        serializer = RewardSerializer(list, many=True)
        return Response (serializer.data)


class transactionList(APIView):
    def get(self, request):
        list = transaction.objects.all()
        serializer = transactionSerializer(list, many=True)
        return Response (serializer.data)
