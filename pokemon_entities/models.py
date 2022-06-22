from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True)

    def __str__(self):
        return f'Покемон {self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField(null=True, verbose_name='Lat')
    lon = models.FloatField(null=True, verbose_name='Lon')
    appears_at = models.DateTimeField(null=True, verbose_name='Appears at')
    disappears_at = models.DateTimeField(null=True, verbose_name='Disappears at')

    def __str__(self):
        return f'{self.pokemon} latitude {self.Lat},  longtitude {self.Lon}'
    