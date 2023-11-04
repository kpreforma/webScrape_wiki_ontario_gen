import pandas as pd
import requests as req
import io
from bs4 import BeautifulSoup as bs

wikiurl = "https://en.wikipedia.org/wiki/List_of_generating_stations_in_Ontario"
res = req.get(wikiurl)
print(res.status_code)

gen_tables = bs(res.text, "html.parser").find_all(
    "table", {"class": "wikitable sortable"}
)
gen_tables_str = [io.StringIO(str(table)) for table in gen_tables]
gen_tables_df = [pd.read_html(table)[0] for table in gen_tables_str]

tech = ["Nuclear", "Fossil fuel", "Biomass", "Hydroelectric", "Wind", "Solar"]
for i, t in enumerate(tech):
    gen_tables_df[i]["Tech"] = t

all_tech = pd.concat(gen_tables_df)

print(all_tech[:100].to_string())
