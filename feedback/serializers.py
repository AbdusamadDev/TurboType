from rest_framework import serializers
from feedback.models import Feedback





class FeedbackSerializer(serializers.ModelSerialiser):
    model = Feedback
    fields = '__all__'