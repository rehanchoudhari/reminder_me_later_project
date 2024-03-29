from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReminderSerializer




@api_view(['POST'])
def create_reminder_message(request):
    if request.method == 'POST':
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message: Reminder Saved Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
