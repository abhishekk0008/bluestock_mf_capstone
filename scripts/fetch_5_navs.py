import requests
import pandas as pd

schemes = {
    119551: "sbi_bluechip",
    120503: "icici_bluechip",
    118632: "nippon_largecap",
    119092: "axis_bluechip",
    120841: "kotak_bluechip"
}

for amfi_code, scheme_name in schemes.items():

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    data = response.json()

    latest_nav = data["data"][0]

    df = pd.DataFrame([latest_nav])

    file_name = f"data/raw/{scheme_name}_nav.csv"

    df.to_csv(file_name, index=False)

    print(f"{scheme_name} saved successfully!")