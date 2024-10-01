import requests
from bs4 import BeautifulSoup
import csv

# URL da página de tendências do GitHub
url = 'https://github.com/trending'

# Fazer a requisição HTTP
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todos os repositórios
repositories = soup.find_all('article', class_='Box-row')

# Criar uma lista para armazenar os dados
repo_data = []

# Extrair as informações de cada repositório
for repo in repositories:
    repo_name = repo.h2.a.text.strip()  # Nome do repositório
    repo_url = 'https://github.com' + repo.h2.a['href']  # URL do repositório
    description = repo.p.text.strip() if repo.p else 'No description'
    language = repo.find('span', itemprop='programmingLanguage').text if repo.find('span', itemprop='programmingLanguage') else 'No language'
    stars = repo.find('a', href=lambda x: x and x.endswith('/stargazers')).text.strip()
    forks = repo.find('a', href=lambda x: x and x.endswith('/forks')).text.strip()

    # Adicionar os dados extraídos na lista
    repo_data.append([repo_name, description, language, stars, forks, repo_url])

# Escrever os dados em um arquivo CSV
with open('github_trending.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Repository Name', 'Description', 'Language', 'Stars', 'Forks', 'URL'])
    writer.writerows(repo_data)

print("Dados extraídos com sucesso para 'github_trending.csv'.")
