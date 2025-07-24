import wantgoo
import asyncio

def main():
    urls = [
        "https://www.wantgoo.com/stock/2330/technical-chart",
        "https://www.wantgoo.com/stock/2317/technical-chart",
        "https://www.wantgoo.com/stock/3008/technical-chart",
        "https://www.wantgoo.com/stock/5274/technical-chart",
        "https://www.wantgoo.com/stock/2454/technical-chart",
        "https://www.wantgoo.com/stock/3037/technical-chart",
        "https://www.wantgoo.com/stock/3014/technical-chart",
        "https://www.wantgoo.com/stock/2002/technical-chart",
        "https://www.wantgoo.com/stock/2610/technical-chart",
        "https://www.wantgoo.com/stock/2618/technical-chart",
    ]
    reuslts:list[dict] = asyncio.run(wantgoo.get_stock_data(urls=urls))
    for stock in reuslts:
        print(stock)

if __name__ == "__main__":
    # main()
    print(wantgoo.get_stocks_with_twstock())
