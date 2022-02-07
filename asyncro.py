import asyncio

async def async_func():
    print('Velotio ...')
    await asyncio.sleep(10)
    print('... Technologies!')
    return 1


async def main():
    #async_func()#this will do nothing because coroutine object is created but not awaited
    taskB = asyncio.ensure_future(async_func())
    print("yoyoyooy")


loop = asyncio.get_event_loop()
val = loop.run_until_complete(main())
#future = asyncio.ensure_future(fetch_async(ntimes))
#print("shams")
# i need to put the loops on here.
#print(val)