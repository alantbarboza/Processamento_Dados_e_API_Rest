import asyncio
import aiohttp
from dotenv import load_dotenv
import os

load_dotenv()
weather_key = os.getenv('weather_key')

async def obter_dados(cidade):
    try:
        async with aiohttp.ClientSession() as sessao:
            async with sessao.get(f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={weather_key}&lang=pt_br&units=metric') as response:
                if response.status == 200:
                    data = await response.json()
                    print(f'Cidade: {data['name']}')
                    print(f'Descrição: {data['weather'][0]['description']}')
                    print(f'Temperatura: {data['main']['temp']}')
                elif response.status == 404:
                        print(f'Cidade não encontrada.')
                else:
                        print(f'Erro desconhecido.')

    except Exception as erro:
        print(f'Erro na requisição: {str(erro)}')

async def main():
    resposta = 'sim'
    while resposta.lower().strip() not in ['nao', 'n']:
        os.system('cls')  
        cidade = input("Digite o nome da cidade: ")
        await obter_dados(cidade)
        resposta = input("Deseja continuar (sim ou não)? ")

# Verifica se o script está sendo executado diretamente como programa principal
if __name__ == "__main__":
    asyncio.run(main())
