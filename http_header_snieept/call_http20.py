import httpx
import asyncio

async def fetch():
    # 虽然发送的是http2请求，但是服务端是http1.1的，还是http1.1的请求
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get('http://127.0.0.1:8000/http11')
        print(f'Status Code: {response.status_code}')
        print(f'Response Content: {response.text}')

if __name__ == '__main__':
    asyncio.run(fetch())