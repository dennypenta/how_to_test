from rest_framework import serializers

from testing.resources import IS_TITLE_ERROR


class IsTItleValidator(object):
    message = IS_TITLE_ERROR

    def __call__(self, value):
        if not value.istitle():
            raise serializers.ValidationError(self.message)
