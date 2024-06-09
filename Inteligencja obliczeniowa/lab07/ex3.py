from twscrape import API, gather
import asyncio


async def main():
    api = API()

    await api.pool.add_account("memetelve", "redacted", "", "")
    await api.pool.login_all()
    posts = await gather(api.search("python", limit=10))
    for post in posts:
        with open("posts.json", "a") as f:
            f.write(post.json())


if __name__ == "__main__":
    asyncio.run(main())
