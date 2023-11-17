import os
import json
import requests
import time
import boto3

TMDB_API_KEY = os.environ.get('TMDB_API_KEY')
TMDB_API_TOKEN = os.environ.get('TMDB_API_TOKEN')

S3_BUCKET_NAME = 'ryan-desafio-bucket'
S3_PREFIX = 'Raw/Local/JSON'

# Inicialização de clientes
s3 = boto3.client('s3')

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

def save_movies_to_s3(filmes, contador):
    """Salva os filmes no S3."""
    file_name = f'filmes_arquivo_{contador}.json'
    s3_path = f"{S3_PREFIX}/{file_name}"

    # Convertendo a lista de filmes para uma string JSON
    filmes_json = json.dumps(filmes, ensure_ascii=False, indent=4)

    # Upload direto para o S3
    s3.put_object(Body=filmes_json, Bucket=S3_BUCKET_NAME, Key=s3_path)

    print(f"Arquivo {file_name} enviado com sucesso para o S3.")

def discover_movies(api_key, params):
    """Descobre e coleta informações sobre filmes."""
    url = "https://api.themoviedb.org/3/discover/movie"
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
                    save_movies_to_s3(filmes, contador)
                    filmes = []

            else:
                print(f"Erro na requisição: {response.status_code}")
    else:
        print(f"Erro na requisição: {response.status_code}")

def lambda_handler(event, context):
    """Função de manipulador principal."""
    # Configurações iniciais
    api_key = TMDB_API_KEY
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

    # Executa a descoberta de filmes e salva no S3
    discover_movies(api_key, params)
