from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        new_habit = Habit.objects.create(**validated_data)
        # check usual habit
        if new_habit.is_pleasant is False:
            if not new_habit.award:
                raise serializers.ValidationError("Usual habit must has award!")

            return new_habit
        # check pleasant habit
        else:
            if new_habit.award is not None:
                raise serializers.ValidationError("Pleasant habit can not has award!")

    class Meta:
        model = Habit
        fields = "__all__"
