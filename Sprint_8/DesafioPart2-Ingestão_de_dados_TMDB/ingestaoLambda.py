import requests
import json
import time

def get_movie_data(movie_id, api_key):
    """Obtém informações adicionais sobre um filme usando o ID do filme."""
    filme_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    filme_params = {"api_key": api_key}
    filme_response = requests.get(filme_url, params=filme_params)

    if filme_response.status_code == 200:
        return filme_response.json()
    else:
        print(f"Falha na requisição de informações adicionais para o filme com ID {movie_id}. Código de status: {filme_response.status_code}")
        return None

def save_movies_to_file(filmes, contador):
    """Salva os filmes em um arquivo JSON."""
    file_name = f'filmes_arquivo_{contador}.json'
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(filmes, json_file, ensure_ascii=False, indent=4)
        print(f"Arquivo {file_name} salvo com sucesso!")

def discover_movies(api_key, params):
    """Descobre e coleta informações sobre filmes."""
    url = "https://api.themoviedb.org/3/discover/movie"
    base_url = "https://api.themoviedb.org/3/movie"
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        total_pages = data.get('total_pages', 1)

        contador = 0
        filmes = []

        for page in range(1, total_pages + 1):
            params['page'] = page
            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                data = response.json()

                for filme in data['results']:
                    filme_data = get_movie_data(filme['id'], api_key)

                    if filme_data:
                        filmes.append(filme_data)
                        time.sleep(0.02)

                if len(filmes) >= 100 or page == total_pages:
                    contador += 1
                    save_movies_to_file(filmes, contador)
                    filmes = []

            else:
                print(f"Erro na requisição: {response.status_code}")
    else:
        print(f"Erro na requisição: {response.status_code}")

# Configurações iniciais
api_key = "2866514b7137f96a2f188f3f14e80b37"
params = {
    "include_adult": False,
    "include_video": False,
    "language": "pt-BR",
    "page": 1,
    "primary_release_date.gte": "2018-01-01",
    "sort_by": "popularity.desc",
    "vote_count.gte": 10,
    "with_genres": 80,
    "api_key": api_key
}

# Executa a descoberta de filmes
discover_movies(api_key, params)
