import openai
import os

# Adicione sua chave de API do OpenAI aqui
openai.api_key = "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"


# API DaVinciText: Essa API permite realizar perguntas a IA e obter uma resposta
def davinciText(prompt):
    prompt = prompt
    model = "text-davinci-002"
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100
    )
    message = completions.choices[0].text
    return message


print('\n')

print('GPT: Em que posso te ajudar?')
prompt = input('Eu: ')
print("GPT: ", davinciText(prompt+' Informe tudo isso em até 100 caracteres'))

print('\n')
