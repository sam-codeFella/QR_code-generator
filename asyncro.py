import asyncio

async def async_func():
    print('Velotio ...')
    print('... Technologies!')
    return 'shams'


async def main():
    #async_func()#this will do nothing because coroutine object is created but not awaited
    taskB = asyncio.ensure_future(async_func())
    print("yoyoyooy")
    responses = await asyncio.gather(taskB)
    print(responses.content)

loop = asyncio.get_event_loop()
val = loop.run_until_complete(main())
#future = asyncio.ensure_future(fetch_async(ntimes))
#print("shams")
# i need to put the loops on here.
#print(val)