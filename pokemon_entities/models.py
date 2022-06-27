from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, null=True)
    title_jp = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True)
    description = models.TextField(null=True, verbose_name='Описание')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField(null=True, verbose_name='Lat')
    lon = models.FloatField(null=True, verbose_name='Lon')
    appears_at = models.DateTimeField(null=True, verbose_name='Appears at')
    disappears_at = models.DateTimeField(null=True, verbose_name='Disappears at')
    level = models.IntegerField(null=True, verbose_name='Level')
    health = models.IntegerField(null=True, verbose_name='Health')
    attack = models.IntegerField(null=True, verbose_name='Attack')
    defence = models.IntegerField(null=True, verbose_name='Defence')
    stamina = models.IntegerField(null=True, verbose_name='Stamina')

    def __str__(self):
        return f'{self.pokemon}'
