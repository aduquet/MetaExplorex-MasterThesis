from rest_framework import serializers

class ChartDataSerializer(serializers.Serializer):
    labels = serializers.ListField()
    data = serializers.ListField()
    total_data_points = serializers.IntegerField(allow_null=True)