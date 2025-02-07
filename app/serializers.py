from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    category = SerializerMethodField()

    class Meta:
        model = Product
        fields = "id name description price category created_at updated_at".split()

    def get_category(self, obj):
        return obj.category.name