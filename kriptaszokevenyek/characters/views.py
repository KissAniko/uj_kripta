from django.http import JsonResponse

from .models import PlayerCharacter, EnemyCharacter                                #
from .serializers import PlayerCharacterSerializer, EnemyCharacterSerializer       #

def getAllPlayer(request):
    players = PlayerCharacter.objects.all()

    ser = PlayerCharacterSerializer(players, many=True)

    return JsonResponse(ser.data,  safe=False)


def getPlayer(request, id):
    actualCharacter = PlayerCharacter.objects.get(id=id)

    serializedCharacter = PlayerCharacterSerializer(actualCharacter, many=False)
    
    return JsonResponse(serializedCharacter.data)

def getAllEnemies(request):                                             # 
    enemies = EnemyCharacter.objects.all()
    ser = EnemyCharacterSerializer(enemies, many=True)
    return JsonResponse (ser.data, safe = False)

def getEnemy(request, pk):  #  request = azt tárolja, h mik voltak a körülmények, mikor beírtuk az URL-t
# request.post ---> ?
    enemy = EnemyCharacter.objects.get(id=pk)           # 1 db szörnyet akarunk
    ser = EnemyCharacterSerializer(enemy, many = False)
    return JsonResponse(ser.data)






 # t = [{"name" = "Béla"}]  --> t[0].name   many = True
 # t =  {"name" = "Béla"}   --> t[0].name   many = False
