import asyncio, time

async def first_task():
    print('first_task before await')
    await asyncio.sleep(1)
    print('first_task after await')

async def second_task():
    print('second_task before await')
    await asyncio.sleep(5)
    print('second_task after await')

async def third_task():
    print('third_task before await')
    await asyncio.sleep(3)
    print('third_task after await')

async def main():
    await asyncio.gather(first_task(), second_task(), third_task())
    ...

start = time.time()
asyncio.run(main())
end = time.time()
print('work time: ', round(end - start, 3))