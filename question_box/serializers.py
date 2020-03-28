from rest_framework import serializers

from question_box.models import QuestionAnswerPair


class QuestionAnswerPairSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswerPair
        fields = ('id', 'question', 'answer')