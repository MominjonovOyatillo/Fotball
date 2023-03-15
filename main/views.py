from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from datetime import datetime

@api_view(["GET"])
def get_info(request):
    info = Info.objects.last()
    info_ser = InfoSerializer(info)
    social_medias = SocialMedia.objects.all()
    social_media_ser = SocialMediaSerializer(social_medias, many=True)
    data = {
        "data": info_ser.data,
        "social_media": social_media_ser.data
    }
    return Response(data)


@api_view(["GET"])
def get_media(request):
    medias = Media.objects.all()
    medias_ser = MediaSerializer(medias, many=True)
    media_matches = MediaMatch.objects.all()
    media_matches_ser = MediaMatchSerializer(media_matches, many=True)
    data = {
        "data": medias_ser.data,
        "media_matches": media_matches_ser.data
    }
    return Response(data)


@api_view(["GET"])
def get_news(request):
    news = News.objects.all()
    news_ser = NewsSerializer(news, many=True)
    data = {
        "data": news_ser.data
    }
    return Response(data)

@api_view(["GET"])
def get_shop(request):
    products = Shop.objects.all()
    product_ser = ShopSerializer(products, many=True)
    data = {
        "data": product_ser.data
    }
    return Response(data)


@api_view(["GET"])
def get_statistics(request):
    matches = Match.objects.all()
    match_ser = MatchSerializer(matches, many=True)
    data = {
        "match": match_ser.data,
    }
    return Response(data)

@api_view(["GET"])
def get_player(reuqest):
    players = Player.objects.all()
    player_ser = PlayerSerializer(players, many=True)
    data = {
        "data": player_ser.data
    }
    return Response(data)

@api_view(["GET"])
def get_academy(request):
    academy = Academy.objects.last()
    academy_ser = AcademySerializer(academy)
    data = {
        "data": academy_ser.data
    }
    return Response(data)
