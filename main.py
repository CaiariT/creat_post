import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

#le o arquivo
def ler_arquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        return file.read()

# Definições GPT
def definicoesChat(texto):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f'{texto}',
        temperature=0.7,
        max_tokens=2400,
        n=1,
        stop=None
    )

    # Retorne a primeira escolha da solicitação
    return response['choices'][0]['text']
#le o arquivo de texto
text = ler_arquivo('arquivo.txt')
#chamaaa function
resultado = definicoesChat(text)
print(resultado)
