from rest_framework import serializers
from market_search.models import Items, Categories, Stores


class ItemsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Categories.objects.all(), slug_field='title')
    store = serializers.SlugRelatedField(queryset=Stores.objects.all(), slug_field='title')

    class Meta:

        model = Items
        fields = ['item_pic',
                  'item_name',
                  'in_stock',
                  'link',
                  'price',
                  'category',
                  'store']

    def create(self, validated_data):
        item, created = Items.objects.update_or_create(
            item_name=validated_data.get('item_name', None),
            defaults=validated_data
        )
        return item
