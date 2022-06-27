from django.db import models


class Pokemon(models.Model):
    """Тип покемона"""
    title = models.CharField(max_length=200)
    title_en = models.CharField(
        max_length=200,
        null=True)
    title_jp = models.CharField(
        max_length=200,
        null=True)
    image = models.ImageField(null=True)
    description = models.TextField(
        null=True,
        verbose_name='Описание')

    previous_evolution = models.ForeignKey(
        'self',
        verbose_name='Из кого эволюционирует',
        null=True,
        blank=True,
        related_name='next_evolutions',
        on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    """Экземляр покемона"""
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField(
        null=True,
        verbose_name='Широта')
    lon = models.FloatField(
        null=True,
        verbose_name='Долгота')
    appears_at = models.DateTimeField(
        null=True,
        verbose_name='Появляется с')
    disappears_at = models.DateTimeField(
        null=True,
        verbose_name='Исчезает с')
    level = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Уровень')
    health = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Здоровье')
    attack = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Аттака')
    defence = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Защита')
    stamina = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Выносливость')

    def __str__(self):
        return f'{self.pokemon}'
