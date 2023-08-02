from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit
from users.views import IsOwnerOrReadOnly
from habits.serializers.habit import HabitSerializer
from habits.permissions import IsOwner


class HabitListView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        search_owners = []
        owners = Habit.objects.filter()
        # find and filter users habits
        for find_owner in owners:
            print(find_owner)
            if find_owner.is_public is True:
                search_owners.append(find_owner)
            else:
                if find_owner.owner == user:
                    search_owners.append(find_owner)
        return search_owners



class HabitDetailView(generics.RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitCreateView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()


class HabitUpdateView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitDeleteView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]
