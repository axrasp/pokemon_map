from django.db import models


class Pokemon(models.Model):
    """Тип покемона"""
    title = models.CharField(
        max_length=200,
        verbose_name='Название')
    title_en = models.CharField(
        max_length=200,
        verbose_name='Название (англ)',
        blank=True)
    title_jp = models.CharField(
        max_length=200,
        verbose_name='Названия (яп)',
        blank=True)
    image = models.ImageField(
        verbose_name='Изображение')
    description = models.TextField(
        blank=True,
        verbose_name='Описание')
    previous_evolution = models.ForeignKey(
        'self',
        verbose_name='Из кого эволюционирует',
        null=True,
        blank=True,
        related_name='next_evolutions',
        on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    """Экземляр покемона"""
    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.CASCADE,
                                related_name='entities')
    lat = models.FloatField(
        blank=True,
        verbose_name='Широта')
    lon = models.FloatField(
        blank=True,
        verbose_name='Долгота')
    appears_at = models.DateTimeField(
        blank=True,
        verbose_name='Появляется с')
    disappears_at = models.DateTimeField(
        blank=True,
        verbose_name='Исчезает с')
    level = models.IntegerField(
        blank=True,
        verbose_name='Уровень')
    health = models.IntegerField(
        blank=True,
        verbose_name='Здоровье')
    attack = models.IntegerField(
        blank=True,
        verbose_name='Аттака')
    defence = models.IntegerField(
        blank=True,
        verbose_name='Защита')
    stamina = models.IntegerField(
        blank=True,
        verbose_name='Выносливость')

    def __str__(self):
        return self.pokemon.title
