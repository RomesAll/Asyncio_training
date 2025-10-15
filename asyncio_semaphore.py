# Ист: https://www.youtube.com/watch?v=jkJqkFRoXSg
# Сервер может ограничивать кол-во запросов, которые он может обработать
# Чтобы это исправить можно, например, написать полностью синхронный код, но все будет работать медленнее
# Или можно использовать Semaphore. Он позволяет ограничить кол-во параллельно выполняющ. коррутин
# acquire - заняли коррутинную функцию
# release - освободили коррутинную функцию
# То есть с помощью этих ключевых слов мы ограничиваем кол-во параллельно выполняющ. коррутин

import asyncio
from asyncio import Semaphore
num = 0

async def api_test(semaphore: Semaphore):
    async with semaphore:
        global num
        num += 1
        print(f'working {num}')
        await asyncio.sleep(1)

async def main():
    semaphore = Semaphore(3)
    await asyncio.gather(*[api_test(semaphore) for _ in range(50)])

if __name__ == '__main__':
    asyncio.run(main())