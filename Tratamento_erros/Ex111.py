import requests
try:
    url = "https://www.google.com/"
    if requests.get(url).status_code == 200:
        print("O servidor está disponível.")
except Exception as erro:
    print(erro.__class__)        
    print("O servidor está indisponível.")