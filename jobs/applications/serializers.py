from rest_framework import serializers
from applications.models import Jobs , Applications

class ApplicantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Applications
        fields = "__all__"


class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = "__all__"

