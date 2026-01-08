import requests
from bs4 import BeautifulSoup
from django.core.files.base import ContentFile

def fetch_game_images(game_name: str, max_images: int = 4):
    """
    Busca até 4 imagens reais do Google via scraping.
    Retorna lista de ContentFile.
    """
    images = []

    try:
        query = "+".join(game_name.split())
        url = f"https://www.google.com/search?tbm=isch&q={query}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()

        soup = BeautifulSoup(r.text, "html.parser")
        img_tags = soup.find_all("img")[1:]  # pular logo do Google

        for i, img_tag in enumerate(img_tags[:max_images]):
            img_url = img_tag.get("src")
            if not img_url:
                continue
            r_img = requests.get(img_url, timeout=10)
            r_img.raise_for_status()
            img_file = ContentFile(r_img.content, name=f"{game_name}_{i+1}.jpg")
            images.append(img_file)

    except Exception as e:
        print(f"Scraping falhou, usando placeholder: {e}")
        # fallback placeholder
        for i in range(max_images):
            placeholder_url = f"https://via.placeholder.com/400x400.png?text={game_name.replace(' ', '+')}_{i+1}"
            try:
                r = requests.get(placeholder_url, timeout=10)
                r.raise_for_status()
                img_file = ContentFile(r.content, name=f"{game_name}_{i+1}.jpg")
                images.append(img_file)
            except:
                continue

    return images
