import supabase
from supabase import SupabaseClient
import os
import asyncio

supabase_url: str = os.environ.get("SUPABASE_URL")
supabase_key: str = os.environ.get("SUPABASE_KEY")

print("supabase_url", supabase_url)
print("supabase_key", supabase_key)

supabase_client: SupabaseClient = SupabaseClient(supabase_url, supabase_key)


async def main():
    data = await supabase_client.table("countries").insert({"name": "Germany"}).execute()
    print(data)
    assert len(data.data) > 0


async def class_test():
    async with supabase_client.on("countries") as c:
        listx = [
            {"name": "Germany"},
            {"name": "France"},
            {"name": "Italy", "population": 1000000},
        ]
        single = {"name": "Spain", "population": 1000000}
        data = await c.insert(single).execute()
        print(data)
        assert len(data.data) > 0

if __name__ == "__main__":
    # asyncio.run(main())
    asyncio.run(class_test())

