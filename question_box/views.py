from rest_framework import generics

from question_box.models import QuestionAnswerPair
from question_box.serializers import QuestionAnswerPairSerializer


class QuestionAnswerPairList(generics.ListAPIView):
    queryset = QuestionAnswerPair.objects.all()
    serializer_class = QuestionAnswerPairSerializer
