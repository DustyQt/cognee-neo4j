import asyncio
import webbrowser
import os
from cognee.api.v1.add import add
from cognee.api.v1.cognify import cognify
from cognee.api.v1.search import search, SearchType
from cognee.api.v1.visualize.visualize import visualize_graph
 
async def main():   
    print("🔄 Adding data to Cognee...")
    await add("/home/dusty/Documents/GitHub/cognee-neo4j/src/5c4e8733d36e3e0001562f6a.csv")
    
    print("🧠 Processing data through Cognee pipeline...")
    await cognify()
    
    print("🔍 Searching the knowledge graph...")
    results = await search(
        query_text="How is AI being used in healthcare?",
        query_type=SearchType.GRAPH_COMPLETION
    )
    
    print("📊 Search Results:")
    for result in results:
        print(f"- {result}")
    
    print("📈 Generating visualization...")
    await visualize_graph()
    
    # Open the generated visualization
    home_dir = os.path.expanduser("~")
    html_file = os.path.join(home_dir, "graph_visualization.html")
    
    print(f"🌐 Opening visualization at: {html_file}")
    webbrowser.open(f"file://{html_file}")
    
    print("✅ Tutorial completed successfully!")
 
if __name__ == '__main__':
    asyncio.run(main())