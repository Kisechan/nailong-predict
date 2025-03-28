import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(keyword, num_images, output_dir):

    os.makedirs(output_dir, exist_ok=True)

    base_url = f"https://cn.bing.com/images/search?q={keyword}&first=1"

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all('img')
    for i, img in enumerate(img_tags[:num_images]):
        try:
            img_url = img['src']
            if not img_url.startswith('http'):
                img_url = urljoin(base_url, img_url)

            img_data = requests.get(img_url).content
            with open(os.path.join(output_dir, f"{keyword}_{i}.jpg"), 'wb') as f:
                f.write(img_data)
        except Exception as e:
            print(f"图片 {i + 1} 下载错误: {e}")

download_images("奶龙", 500, "../../data/raw/tang")
# download_images("藤田琴音", 50, "../../data/raw/cute")