import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

print("Scheme Name:")
print(data["meta"]["scheme_name"])

latest_nav = data["data"][0]

print("\nLatest NAV:")
print(latest_nav)

df = pd.DataFrame([latest_nav])

df.to_csv("data/raw/hdfc_top100_nav.csv", index=False)

print("\nCSV file saved successfully!")