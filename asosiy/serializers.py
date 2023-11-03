from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *



class SuvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suv
        fields = "__all__"

    def validate_litr(self, qiymat):
        if qiymat > "19":
            return qiymat
        raise ValidationError("Bunday kotta litrda suv sotilmaydi")


class MijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = "__all__"

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"

class HaydovchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Haydovchi
        fields =  "__all__"


class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = "__all__"

    def validate_qarz(self, qiymat):
        qiymat = Buyurtma.mijoz__qarz
        if qiymat < 500000:
            return f"Qarzingiz {qiymat}"
        raise ValidationError("Qarzingiz juda ko'p, buyurtma qilolmaysiz")
