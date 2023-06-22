import asyncio

from Python.book_abstracts.Asycio_MatthewFowler.code.util.async_input import create_stdin_reader
from Python.book_abstracts.Asycio_MatthewFowler.code.util.delay import delay


async def main():
    stdin_reader = await create_stdin_reader()
    while True:
        delay_time = await stdin_reader.readline()
        asyncio.create_task(delay(int(delay_time)))

asyncio.run(main())
