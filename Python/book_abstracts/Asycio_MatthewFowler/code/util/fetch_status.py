from aiohttp import ClientSession

from Python.book_abstracts.Asycio_MatthewFowler.code.util.async_timer import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status
