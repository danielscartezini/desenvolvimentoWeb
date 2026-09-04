import requests

'''
resp = requests.get("https://httpbin.org/get")
print("Status:", resp.status_code)
print("URL:", resp.url)
print("Headers:", resp.headers["Content-Type"])
print("Texto:", resp.text[:80], "...") # só os primeiros 80

print("JSON:", resp.json())

# Tarefa 1
url = "https://httpbin.org"

servico = "/ip"
resposta = requests.get(url + servico)
print(f"Status: {resposta.status_code}")
print(resposta.text)
print(resposta.json())
print(resposta.content)

# Tarefa 2
servico = "/image/jpeg"
resposta = requests.get(url, servico)
print(f"Status: {resposta.status_code}")
print(resposta.content)
with open("image.jpg", "wb") as arquivo:
    arquivo.write(resposta.content)
'''

#1. Consulta de API Pública (GET)
#• Use a API gratuita https://jsonplaceholder.typicode.com/posts
#• Faça uma requisição GET para buscar todos os p
url=" https://jsonplaceholder.typicode.com/posts"
servico = "/post"
resposta = requests.get(url, servico)
resposta.json()[:5] 
for postagem in resposta.json()[:5]:
    print(f"Title: {postagem['title']}")

#2. Consulta com Parâmetros (GET com query string)
#• Use https://jsonplaceholder.typicode.com/comments
#• Envie um GET com parâmetro postId=1.
#• Exiba os emails dos usuários que comentaram nesse post.
servico = "/comments?postId=1"
resposta = requests.get(url + servico)
comentarios = resposta.json()
for comentario in comentarios:
    print(f"Email: {comentario['email']}")

#3. Envie uma requisição POST para https://jsonplaceholder.typicode.com/posts.
#• Envie no corpo JSON:
#• { "title": "Teste API", "body": "Primeiro post com requests", "userId": 123 }
#• Exiba a resposta retornada pelo servidor.
