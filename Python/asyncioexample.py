import asyncio

async def func1():
    print("This is func 1")
    return 1

async def func2():
    print("This is func 2")
    return 2


async def main():
    x = loop.create_task(func1())
    y = loop.create_task(func2())
    # t1 = loop.create_task(func1[,])
    # t2 = loop.create_task(func2[])
    # await asyncio.wait([t1,t2])

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()