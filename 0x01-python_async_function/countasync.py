#!/usr/bin/python3
import asyncio
import time


async def count(name: str):
    print(f"Count: {name}")
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count("A"), count("B"), count("C"))
    print("Done!")

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"{__file__} program finished in {elapsed:0.2f} seconds")
