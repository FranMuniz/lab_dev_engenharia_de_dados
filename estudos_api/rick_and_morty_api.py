# import requests

# def fetch_data(endpoint):
#     response = requests.get(f'https://rickandmortyapi.com/api/{endpoint}')

#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None

# characters = fetch_data('character')
# # characters = None

# if characters:
#     print(characters)
# else:
#     print('Failed to fetch data')

#################################################################################

import requests

def fetch_character(character_id):
    response = requests.get(
        f'https://rickandmortyapi.com/api/character/{character_id}'
    )

    if response.status_code == 200:
        return response.json()
    return None

character = fetch_character(2)

if character:
    print(f'Hi, I am {character['name']} o/')
else:
    print('Character not found')