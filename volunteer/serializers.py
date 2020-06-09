from rest_framework import serializers
from.models import IntroduceSpeaker


class IntroduceSpeakerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('full_name', 'email', 'phone_number', 'S_fullname', 'S_email', 'S_reason', 'S_idea',
                  'number', 'verb')
        model = IntroduceSpeaker

    def validate(self, attrs):
        if attrs.get('verb') != 'introduce' and attrs.get('verb') != 'be':
            raise serializers.ValidationError({'verb': 'this should be equal to <be> or <introduce>'})
        return super().validate(attrs)
