from scholarly import scholarly, ProxyGenerator
import json
from datetime import datetime
import os
from scholarly._proxy_generator import MaxTriesExceededException

pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_proxy(pg)

try:
    print("Searching for author information...")
    author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
except MaxTriesExceededException as e:
    print(f"Exception occurred: {e}")
else:
    print("Filling author details...")
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    name = author['name']
    author['updated'] = str(datetime.now())
    author['publications'] = {v['author_pub_id']:v for v in author['publications']}
    print(json.dumps(author, indent=2))
    
    print("Creating results directory...")
    os.makedirs('results', exist_ok=True)
    
    print("Saving author data...")
    with open(f'results/gs_data.json', 'w') as outfile:
        json.dump(author, outfile, ensure_ascii=False)
        
    print("Generating Shields.io data...")
    shieldio_data = {
      "schemaVersion": 1,
      "label": "citations",
      "message": f"{author.get('citedby', 0)}",
    }
    
    print("Saving Shields.io data...")
    with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)
        
    print("Data processing completed.")
