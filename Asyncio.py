# A package is essentially a folder that contains an __init__.py file and one or more Python files (modules).
# Creating and Accessing Packages
# • Create a Directory: create a folder that will act as the package root.
# • Add Modules: Inside the directory, add Python files (modules). Each module can contain related functions or classes.
# • Add __init__.py: add an __init__.py file to the directory. This file tells Python that the directory should be treated as a package.
# • Create Sub-packages (Optional): One can organize code further by creating subdirectories with their own __init__.py files.
# • Import Modules: Modules or functions inside the package can be imported using dot notation

# ASYNCIO
# • It provides the tools needed to write asynchronous, non-blocking code.
# • It is ideal for programs that spend much of their time waiting on I/O— such as network requests, database calls, or file operations—allowing other tasks to run during those waits.
# • It powers many high-performance networking frameworks and lets you run many tasks concurrently within a single thread.

# Core Components
# 1. Event Loop
    # The event loop manages and schedules asynchronous tasks, deciding when each coroutine runs. It cycles through pending jobs and resumes them when their awaited operations complete.
        # asyncio.run(main())
# 2. Coroutines
    # Coroutines are functions declared with async def that can be paused and resumed. They represent units of asynchronous work
        # async def hello():
        #     print("Hello")
# 3. Tasks
    # Tasks wrap coroutines and allow them to run concurrently. You create them with asyncio.create_task().
# 4. Awaitables
    # Objects that can be awaited—typically coroutines, tasks, or certain asyncio primitives.
    # await asyncio.sleep(2)

# Demo program 1
import asyncio
async def greet():
    print("Hello")
    await asyncio.sleep(4)
    print("Welcome to Asyncio")
asyncio.run(greet())  # await greet() command in jupyter notebook
print()


# Demo Program 2
import asyncio
async def fn():
    print('This is ')
    await asyncio.sleep(1)
    print('asynchronous programming')
    await asyncio.sleep(2)
    print('and not multi-threading')
asyncio.run(fn())   # await fn()
print()


# Simple program
import asyncio
async def example():
    print("Task started")
    await asyncio.sleep(2)
    print("Task completed")
asyncio.run(example())  # await example()
print()


#Synchronous execution
import time
def task(name):
    print(f"{name} started")
    time.sleep(3)
    print(f"{name} completed")
task("Task1")
task("Task2")
task("Task3")
print()


# Asynchronious execution
import asyncio
async def task(name):
    print(f"{name} started")
    await asyncio.sleep(3)
    print(f"{name} completed")
async def main():
    await asyncio.gather(
        task("Task1"),
        task("Task2"),
        task("Task3")
    )   
asyncio.run(main())     # await main()
print()


# Print reults after gathering all
import asyncio
async def square(n):
    await asyncio.sleep(2)
    return n * n
async def main():
    results = await asyncio.gather(
        square(2),
        square(3),
        square(4)
    )
    print(results)
asyncio.run(main())     # await main()
print()


#Student attendance system
import asyncio
async def mark_attendance(student):
    print(f"Marking attendance for {student}")
    await asyncio.sleep(2)
    print(f"{student} completed")
async def main():
    await asyncio.gather(
        mark_attendance("A"),
        mark_attendance("B"),
        mark_attendance("C")
    )
asyncio.run(main())     # await main()
print()


#Exmaple 3
import asyncio
async def main():
    print("one")
    await asyncio.sleep(1)
    await fn2()
    print('four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)
async def fn2():
    await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)
    print("three")
asyncio.run(main())     # await main()
print()


# create task
import asyncio
async def main():
    task=asyncio.create_task(fn2())
    print("one")
    #await asyncio.sleep(1)
    #await fn2()
    print('four')
    await asyncio.sleep(3)
    print('five')
    await asyncio.sleep(1)
async def fn2():
    await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(4)
    print("three")
asyncio.run(main())     # await main()
print()


# I/O bound task using asyncio.sleep
import asyncio
async def func1():
    print("Function 1 started..")
    await asyncio.sleep(2)
    print("Function 1 Ended")
async def func2():
    print("Function 2 started..")
    await asyncio.sleep(3)
    print("Function 2 Ended")
async def func3():
    print("Function 3 started..")
    await asyncio.sleep(1)
    print("Function 3 Ended")
async def main():
    L = await asyncio.gather(
        func1(),
        func2(),
        func3(),
    )
    print("Main Ended..")
asyncio.run(main())     # await main()
print()



# https://www.geeksforgeeks.org/python/fastapi-tutorial/
# https://www.youtube.com/watch?v=pGQfWLN2tMY