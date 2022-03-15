from rest_framework import serializers

from .models import reward, transaction



class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = reward
        fields = '__all__'

class transactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields = '__all__'