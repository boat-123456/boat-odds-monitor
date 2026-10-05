import requests
from bs4 import BeautifulSoup

url = "https://www.boatrace.jp/owpc/pc/race/oddstf?hd=20261005&jcd=12&rno=1"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=20
)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

print("ページ取得成功")
print("URL:", url)

text = soup.get_text(" ", strip=True)

if "単勝オッズ" in text:
    print("単勝オッズ欄を確認しました")
else:
    print("単勝オッズ欄が見つかりません")
