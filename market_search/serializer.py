from rest_framework import serializers
from market_search.models import Items


class ItemsSerializer(serializers.Serializer):
    item_name = serializers.CharField(max_length=255)
    link = serializers.URLField()

    def create(self, validated_data):
        return Items.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.item_name = validated_data.get('item_name', instance.item_name)
        instance.link = validated_data.get('link', instance.link)
        instance.save()
        return instance
