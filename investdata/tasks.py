from celery import shared_task, group
from investdata.models import Stocks
import yfinance as yf # biblioteca da api do Yohoo Finance


# tarefa pra pegar os valores das ações da Yohoo Finance
@shared_task
def get_stock_price_task(stock_name):
    stock = yf.Ticker(stock_name + ".SA")
    price = stock.history(period="1d")["Close"].iloc[-1]
    
    Stocks.objects.create(
        name=stock_name, 
        price=float(price)
    )

    return float(price)


# Tarefa que buscar uma lista de 100 ações
@shared_task
def fetch_all_stocks_task():
    stocks_list = [
        "ABEV3", "AZUL4", "B3SA3", "BBAS3", "BBDC3", "BBDC4", "BBSE3", "BEEF3", "BPAC11", "BRAP4",
        "BRFS3", "BRKM5", "BRSR6", "BRST3", "BSLI3", "CALI3", "CAMB3", "CAML3", "CASH3", "CBAV3",
        "CBEE3", "CCRO3", "CEAB3", "CEBR3", "CESP6", "CIEL3", "CMIG4", "CNTO3", "COCE3", "COGN3",
        "CPFE3", "CRFB3", "CSAN3", "CSNA3", "CTIP3", "CTSA3", "CYRE3", "DMMO3", "DOHL3", "DTEX3",
        "ECOR3", "EGIE3", "ELET3", "ELET6", "EMBR3", "ENBR3", "ENEV3", "ENGI11", "EQTL3", "EZTC3",
        "FLRY3", "GGBR4", "GOAU4", "HAPV3", "HYPE3", "IGTI11", "IRBR3", "ITSA4", "ITUB4", "JBSS3",
        "KLBN11", "LREN3", "LWSA3", "MGLU3", "MRFG3", "BEEF3", "MRVE3", "MULT3", "PCAR3", "PETR3",
        "PETR4", "RECV3", "PRIO3", "PETZ3", "RADL3", "RAIZ4", "RDOR3", "RAIL3", "SBSP3", "SANB11",
        "SMTO3", "CSNA3", "SLCE3", "SUZB3", "TAEE11", "VIVT3", "TIMS3", "TOTS3", "TRPL4", "UGPA3",
        "USIM5", "VALE3", "VAMO3", "VBBR3", "WEGE3", "YDUQ3", "VIVT3", "TIMS3", "TOTS3", "TRPL4",
        "UGPA3", "USIM5", "VALE3", "VAMO3", "VBBR3", "WEGE3", "YDUQ3"
    ]

    job = group(get_stock_price_task.s(stock) for stock in stocks_list)
    job.apply_async()
