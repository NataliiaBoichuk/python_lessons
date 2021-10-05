# Інтерфейс прикладного програмування (API) - це веб -служба, яка надає доступ до певних даних та методів,
# до яких інші програми можуть отримати доступ - а іноді і редагувати - за допомогою стандартних протоколів HTTP,
# як і веб -сайт.
# Ця простота полегшує швидку інтеграцію API в найрізноманітніші програми.
# REpresetational State Transfer (REST)- це, мабуть, найпопулярніший архітектурний стиль API для веб -служб .
# Він складається з набору вказівок, призначених для спрощення спілкування клієнта / сервера.
# API REST роблять доступ до даних набагато більш простим і логічним.
import requests

# GET requests
response = requests.get("http://api.open-notify.org/astros.json")
# out <response[200]>
# print(response)
# status_code == 200
# print(response.status_code)
# вміст відповіді GET, bytes
# print(response.content)
# return str
# print(response.text)
# return json obj
# print(response.json())
# return dict with headers, allowing us to access header values by key. Like response.headers['Content-Type']
# not case-sensitive
# print(response.headers)


# code response between 200 and 400 == True
if response:
    print("Success")
else:
    print("An error has occurred(")

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

# Inspect some attributes of the `requests` repository
json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')
print(f'Repository name: {repository["name"]}')
print(f'Repository description: {repository["description"]}')

# Message body. Method POST
# Data can be like a dict or a list of tuple
# requests.post('https://httpbin.org/post', data={'key': 'value'})
# json_response = response.json()
# return that body what we pass early? if this is json obj
# print(json_response['data'])

# Authentication
from getpass import getpass
from requests.auth import HTTPBasicAuth
requests.get('https://api.github.com/user', auth=HTTPBasicAuth('username', getpass()))

# Retrieve
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

github_adapter = HTTPAdapter(max_retries=1)

session = requests.Session()

# Use `github_adapter` for all requests to endpoints that start with this URL
session.mount('https://api.github.com', github_adapter)

try:
    session.get('https://api.github.com')
except ConnectionError as ce:
    print(ce)
