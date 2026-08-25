from scholarly import scholarly
import json, os
from datetime import datetime

author = scholarly.search_author_id(os.environ["GOOGLE_SCHOLAR_ID"])
scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
name = author["name"]
author["updated"] = str(datetime.now())
author["publications"] = {v["author_pub_id"]: v for v in author["publications"]}
os.makedirs("results", exist_ok=True)
with open("results/gs_data.json", "w") as f:
    json.dump(author, f, ensure_ascii=False)
shields = {"schemaVersion": 1, "label": "citations", "message": f"{author['citedby']}"}
with open("results/gs_data_shieldsio.json", "w") as f:
    json.dump(shields, f, ensure_ascii=False)
print(name, author["citedby"], author["hindex"])
