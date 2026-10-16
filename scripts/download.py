import requests
from pathlib import Path

url = "https://www.tennisabstract.com/jsmatches/SerenaWilliamsCareer.js"

response = requests.get(url, timeout=30)
response.raise_for_status()

Path("data").mkdir(exist_ok=True)

Path("data/SerenaWilliamsCareer.js").write_bytes(
    response.content
)

print("Download complete!")
