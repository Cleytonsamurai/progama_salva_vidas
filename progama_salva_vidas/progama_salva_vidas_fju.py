import requests
from bs4 import BeautifulSoup
import webbrowser

def search_google(keyword, site):
    print(f"Resultados para {site}:\n")
    for kw in keyword:
        query = kw + f" site:{site}.com"  # Pesquisa no Google com a palavra-chave no site específico
        url = f"https://www.google.com/search?q={query}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Analisar os resultados da pesquisa
        search_results = soup.find_all("div", class_="g")
        for idx, result in enumerate(search_results, start=1):
            title = result.find("h3").text
            link = result.find("a")["href"]
            link = link.replace("/url?q=", "")  # Remover prefixo indesejado do link

            if "vou me matar hoje" in title.lower() or "vou me matar hoje" in link.lower():
                formatted_title = f"\033[1m{title}\033[0m"  # Título em negrito
                formatted_link = f"\033[1m\033[4m{link}\033[0m"  # Link em negrito e sublinhado
            else:
                formatted_title = title
                formatted_link = link

            print(f"{idx}. Título: {formatted_title}")
            print(f"   Link: {formatted_link}")
            print()

# Exemplo de uso
search_keywords = ["quero me matar", "quero morrer", "vou tirar minha vida", "vou me matar hoje"]

# Redes sociais
social_media = ["twitter", "facebook", "instagram", "linkedin", "tiktok"]

for site in social_media:
    search_google(search_keywords, site)
