import aiohttp

class Completion:
    async def create(self, prompt):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(
                    url="https://api.binjie.fun/api/generateStream",
                    headers={
                        "origin": "https://chat.jinshutuan.com",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                    },
                    json={
                        "prompt": prompt,
                        "system": "Always talk in English.",
                        "withoutContext": True,
                        "stream": False,
                    },
                ) as resp:
                    resp.raise_for_status()  # Raise an exception for HTTP errors
                    return await resp.text()
            except aiohttp.ClientError as exc:
                raise aiohttp.ClientError("Unable to fetch the response.") from exc
