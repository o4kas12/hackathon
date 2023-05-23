import requests
import json
import pandas as pd

url = "https://api.marafon-champion.ru/api/v1/score/statistics/members/"

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
    content = response.content

    with open("response.json", "wb") as file:
        file.write(content)

    print("Ответ сохранен в файле response.json")
else:
    print("Произошла ошибка при выполнении запроса")
    print("Статус код:", response.status_code)

# парсим
with open("response.json", "r", encoding="utf-8") as file:
    json_data = file.read()

data = json.loads(json_data)

# Теперь у вас есть объект Python, представляющий JSON-данные
# Вы можете обращаться к данным, используя стандартные операции работы со словарями и списками

print("Количество участников = ", len(data))

# работа с excel

# Создание пустого DataFrame
df = pd.DataFrame()

# Пример: Перебор элементов списка и вывод значений
# Добавление данных построчно
for item in data:
    df = df.append({'Место': item["index"], 'ФИО': item["full_name"], 'Пол': item["gender"], 'Отдел': item["team"], 'Счет': item["total_score"]}, ignore_index=True)
    print(item["index"], item["full_name"], item["gender"], item["team"], item["total_score"])

# Запись данных в файл Excel
file_path = 'output.xlsx'  # Путь к файлу Excel
sheet_name = 'Лист1'  # Имя листа в Excel

df.to_excel(file_path, sheet_name=sheet_name, index=False)

print("Данные успешно записаны в файл Excel.")