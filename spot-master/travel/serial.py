from rest_framework import serializers
from .models import SpotInfo,CommentTag
class SOPTSeriailzer(serializers.ModelSerializer):
    class Meta:
        model =SpotInfo
        fields = "__all__"
        depth=1

class tagsSeriailzer(serializers.ModelSerializer):
    class Meta:
        model =CommentTag
        fields = "__all__"
        depth=1