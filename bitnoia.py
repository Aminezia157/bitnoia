import requests
import schedule
import time

def get_bitcoin_price():
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {
        'symbol': 'BTCUSDT'  # Par de moedas BTC/USDT
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        data = response.json()
        price = data['price']
        print(f"Preço do Bitcoin (BTC/USDT): {price}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter o preço do Bitcoin: {e}")

def job():
    print("\n--- Verificando o preço do Bitcoin ---")
    get_bitcoin_price()

# Agendar a execução da função job a cada 60 segundos
schedule.every(60).seconds.do(job)

# Loop para manter o script rodando
print("Iniciando monitoramento do preço do Bitcoin...")
while True:
    schedule.run_pending()
    time.sleep(1)