import openai
import os

# Adicione sua chave de API do OpenAI aqui
openai.api_key = "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"


# Essa integração permite pedir a IA para gerar imagens
def createImageFromText(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url


# Essa integração permite pedir a IA para variar uma imagem a partir de uma imagem enviada pelo usuário
def imageVariation():
    response = openai.Image.create_variation(
        image=open("corgi_and_cat_paw.png", "rb"),
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']


print('\n')

print('GPT: Em que posso te ajudar?')
prompt = input('Eu: ')
print('GPT: Confira abaixo:\n', createImageFromText(prompt))

print('\n')


# Dragão branco com o presidente do Brasil montado em cima e atrás a amazônia
