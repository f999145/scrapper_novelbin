import asyncio
import random
import time
import threading


# https://gist.github.com/1st1/f110d5e2ade94e679c4442e9b6d117e1
async def worker(name, queue):
    while True:
        sleep_for = await queue.get()
        await asyncio.sleep(sleep_for)
        queue.task_done()
        print(f'Dequeue {name} for {sleep_for:.2f}')


def task_inqueue(queue):
    while True:
        sleep_for = random.uniform(0.05, 1.0)
        print(f"inserting queue:{sleep_for}")
        queue.put_nowait(sleep_for)
        time.sleep(1)


async def task_dequeue(queue):
    print("====> ENTERING DEQUEUE")
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f'worker-{i}', queue))
        tasks.append(task)


def main():
    queue = asyncio.Queue()
    t_inqueue = threading.Thread(target=task_inqueue, args=(queue, ))
    t_inqueue.start()
    time.sleep(3)
    asyncio.run(task_dequeue(queue))


if __name__ == '__main__':
    main()