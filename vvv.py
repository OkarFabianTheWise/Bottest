from pip import main
import websockets
import asyncio
import logging
async def main():
    url = "WSS://stream.binance.com:9443/stream?streams=btcusdt@miniTicker"
    async with websockets.connect(url) as client:
        pass 
    print(await client.recv())
   

if  __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
