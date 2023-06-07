import requests

LINK = ' https://economia.awesomeapi.com.br/last/USD-BRL'
#API = 'S3HKL7JYM4ZFBXHO'

def mostrar_cotacao(ticker):
    try:
        if ticker == 'DOLAR':
            r = requests.get(LINK).json()
            dolar = r['USDBRL']['high']
            return f'O dolar está em R$ {round(float(dolar),2)}'
        else:    
            r = requests.get(f'https://brapi.dev/api/quote/{ticker}').json()
            name = r['results'][0]['longName']
            price = r['results'][0]['regularMarketPrice']
            return f'{name} R${price}'
    except:
        return('Não encontrada, verifique se digitou certo 😔')







