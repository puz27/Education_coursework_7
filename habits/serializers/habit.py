from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        new_habit = Habit.objects.create(**validated_data)

        return new_habit

    class Meta:
        model = Habit
        fields = "__all__"
