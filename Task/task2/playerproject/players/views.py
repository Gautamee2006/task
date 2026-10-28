from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Player
from .serializers import PlayerSerializer


# Create Player
@api_view(['POST'])
def create_player(request):
    serializer = PlayerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Player created successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get All Players
@api_view(['GET'])
def get_players(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)


# Update Player
@api_view(['PUT'])
def update_player(request, id):
    try:
        player = Player.objects.get(id=id)
    except Player.DoesNotExist:
        return Response({"error": "Player not found"}, status=404)

    serializer = PlayerSerializer(player, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Player updated successfully"})

    return Response(serializer.errors, status=400)


# Delete Player
@api_view(['DELETE'])
def delete_player(request, id):
    try:
        player = Player.objects.get(id=id)
    except Player.DoesNotExist:
        return Response({"error": "Player not found"}, status=404)

    player.delete()
    return Response({"message": "Player deleted successfully"})