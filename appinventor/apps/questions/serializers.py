# _*_ coding: utf-8 _*_
# @Time     : 9:15
# @Author   : Amir
# @Site     : 
# @File     : serializers.py
# @Software : PyCharm

from rest_framework import serializers
from questions.models import Questions


class GetQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = "__all__"


class PostQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ("name", "label_1", "label_2", "label_3", "label_4", "label_5", "question_desc")
