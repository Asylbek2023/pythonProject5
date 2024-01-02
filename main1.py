import requests

url = input("Введите URL: ")
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(response.content)
    else:
        print('Ошибка при получении данных от сервера')
except Exception as e:
    print("Произошла ошибка: " + str(e))