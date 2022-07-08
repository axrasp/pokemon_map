import folium
from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.timezone import localtime

from pokemon_entities.models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    now = localtime()
    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    pokemon_entities = PokemonEntity.objects.filter(
        Q(appears_at__lt=now),
        Q(disappears_at__gt=now)
    )
    for pokemon_entity in pokemon_entities:
        image_uri = \
            request.build_absolute_uri(pokemon_entity.pokemon.image.url)
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            image_uri
        )
    for pokemon in pokemons:
        image_uri = request.build_absolute_uri(pokemon.image.url)
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': image_uri,
            'title_ru': pokemon.title,
        })
    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        if pokemon.id == int(pokemon_id):
            requested_pokemon = pokemon
            break
    else:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    reqested_pokemon_entities = requested_pokemon.entities.all()
    for pokemon_entity in reqested_pokemon_entities:
        image_uri = \
            request.build_absolute_uri(pokemon_entity.pokemon.image.url)
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url)
        )
    pokemon = {
        'img_url': image_uri,
        'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description,
        'previous_evolution': pokemon.previous_evolution,
        'next_evolutions': pokemon.next_evolutions.first(),
    }
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
