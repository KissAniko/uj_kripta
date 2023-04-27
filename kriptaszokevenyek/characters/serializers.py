from rest_framework import serializers
from .models import PlayerCharacter, EnemyCharacter

class PlayerCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerCharacter
        fields = '__all__'

class EnemyCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnemyCharacter
        fields = ['name', 'description']    # fields = mezők .. a nevét és a leírást akarjuk megnézni (name, descript)
                                            # a models.py-ban és itt meg kell egyezzenek a nevek 
                                            # a py-ban figyelni kell a bekezdéseket és szóközöket
    
        fields = '__all__'                  # ezzel a sorral visszaadjuk az összes adatot

        # kiszedünk egy ellenséget
        # táblázatba kiszedjük az ellenségeket