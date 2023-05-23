import requests

url = "https://api.marafon-champion.ru/api/v1/score/statistics/members/"  # Замените на нужный URL

headers = {
    "authority": "api.marafon-champion.ru",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,ru;q=0.8,ru-RU;q=0.7",
    "authorization": "Token 3e74c63f9e3c93d06a4a05b4bae4b153e46dc51e",
    "cache-control": "no-cache",
    "origin": "https://marafon-champion.ru",
    "pragma": "no-cache",
    "referer": "https://marafon-champion.ru",
    "sec-ch-ua": "'Google Chrome';v='113', 'Chromium';v='113', 'Not-A.Brand';v='24'",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Запрос выполнен успешно")
    print("Ответ сервера:")
    print(response.text)
else:
    print("Произошла ошибка при выполнении запроса")
    print("Статус код:", response.status_code)
