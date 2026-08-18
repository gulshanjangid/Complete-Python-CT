import asyncio

async def task(name, seconds):
    print(f"{name} started")

    await asyncio.sleep(seconds)

    print(f"{name} completed")

async def main():
    await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 1),
        task("Task 3", 3)
    )

asyncio.run(main())