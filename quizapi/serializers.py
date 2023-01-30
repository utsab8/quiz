from rest_framework import serializers
from quizapp.models import Quiz

class QuizApiSerializer(serializers.ModelSerializer):

	class Meta:
		model = Quiz
		fields = '__all__'