from rest_framework import serializers


class Database:
    def __init__(self, item_pic, item_name, link, price, in_stock):
        self.item_pic = item_pic
        self.item_name = item_name
        self.link = link
        self.price = price
        self.in_stock = in_stock


class DatabaseSerializer(serializers.Serializer):
    item_pic = serializers.CharField()
    item_name = serializers.CharField(max_length=255)
    link = serializers.URLField()
    price = serializers.IntegerField(min_value=0)
    in_stock = serializers.BooleanField()


# def validate(date):
#     serializer = DatabaseSerializer(data=date)
#     serializer.is_valid(raise_exception=True)
