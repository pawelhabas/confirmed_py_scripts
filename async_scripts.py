import asyncio

#####################

async def say_hello():
    print("Hello...")
    await asyncio.sleep(1)
    print("World")

async def single_main():
    await say_hello()

asyncio.run(single_main())

####################
#  Synchroniczne, jednen po drugim
async def task1():
    print("Start task 1")
    await asyncio.sleep(1)
    print("End task 1")

async def task2():
    print("Start task 2")
    await asyncio.sleep(4)
    print("End task 2")

async def seqvence_main():
    await task1()
    await task2()  # dopiero po task1

asyncio.run(seqvence_main())

##################
# synchroniczne
async def task1_sync() -> str:
    await asyncio.sleep(1)
    return "Hello"

async def task2_sync() -> str:
    await asyncio.sleep(1)
    return "World"

async def main_sync() -> str:
    result1 : str = await task1_sync()
    result2 : str = await task2_sync()
    combined = f"{result1} {result2}!"
    print(combined)

asyncio.run(main_sync())

#####################
# wywołanie wielu funkcji synchronicznie
async def do_work(n) -> str:
    await asyncio.sleep(1)
    return f"Result from task {n}"

async def main_multiple():
    tasks = [do_work(i) for i in range(5)]
    results: list = await asyncio.gather(*tasks)  # zbiera wszystkie wyniki
    print("All results:", results)

asyncio.run(main_multiple())
