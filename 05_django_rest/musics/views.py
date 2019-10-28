from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer, MusicDetailSerializer
from .models import Music, Artist, Comment


@api_view()
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True) # 단일 객체가 아니므로 many = True 값을 준다
    return Response(serializer.data)


@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk = music_pk)
    serializer = MusicDetailSerializer(music)
    return Response(serializer.data)


@api_view(['GET'])
def artist_list(request):
    artist = Artist.objects.all()
    serializer = ArtistSerializer(artist, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def artist_detail(request, artists_pk):
    artists = get_object_or_404(Artist, pk = artists_pk)
    serializer = ArtistDetailSerializer(artists)
    return Response(serializer.data)


@api_view(['POST'])
def comments_create(request, music_pk):
    serializer = CommentSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music_pk)
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def comments_update_and_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk = comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(data = request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': "Comment has been updated"})
    else:
        comment.delete()
        return Response({'message': "Comment has been deketed !"})