from flask import Flask, jsonify
import requests
import redis
import json
import random

app = Flask(__name__)

cache = redis.Redis(host='cache', port=6379)

def get_pokemon_data(pokemon_id):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
    return response.json()

@app.route('/pokemon', methods=['GET'])
def get_random_pokemon():
    # Check if we already have cached Pokémon IDs
    pokemon_ids = cache.get('pokemon_ids')
    if not pokemon_ids:
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=10000')
        data = response.json()
        pokemon_ids = [pokemon['url'].split('/')[-2] for pokemon in data['results']]
        cache.set('pokemon_ids', json.dumps(pokemon_ids))
    else:
        pokemon_ids = json.loads(pokemon_ids)

    random_pokemon_id = random.choice(pokemon_ids)
    pokemon_data = cache.get(f'pokemon_data_{random_pokemon_id}')
    if not pokemon_data:
        data = get_pokemon_data(random_pokemon_id)
        cache.set(f'pokemon_data_{random_pokemon_id}', json.dumps(data))
    else:
        data = json.loads(pokemon_data)

    return jsonify({
        'name': data['name'],
        'abilities': [ability['ability']['name'] for ability in data['abilities']]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
