import asyncio
import cognee
 
async def main():
    # Load from various file types
    await cognee.add("/home/dusty/Documents/GitHub/cognee-neo4j/src/5c4e8733d36e3e0001562f6a.csv")
    await cognee.cognify()

if __name__ == "__main__":
    asyncio.run(main())