from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True)

    def __str__(self):
        return f'Покемон {self.title}'


class PokemonEntity(models.Model):
    Lat = models.FloatField(null=True)
    Lon = models.FloatField(null=True)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pokemon} latitude {self.Lat},  longtitude {self.Lon}'
    