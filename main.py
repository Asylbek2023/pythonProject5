import requests

class Requester():
    def __init__(self, url):
        self.url = url

    def get_request(self):
        result = None
        try:
            response = requests.get(url=self.url)
        except requests.RequestException as e:
            return f"Произошла ошибка: {e}"
        else:
            if response.status_code == 200:
                try:
                    result = response.json()
                except:
                    try:
                        result = response.content()
                    except:
                        try:
                            result = response.text
                        except:
                            result = 'ошибка: '
            else:
                result = 'ошибка: '+ str(response.status_code)
        print(result)

need_url = str(input('Введите ваш URL: '))
requester = Requester(need_url)
result = requester.get_request()
print(result)


