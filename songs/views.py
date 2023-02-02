from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def songs_list(request):


    return Response('ok')



@api_view([''])
def song_detail(request):



    return Response('no')