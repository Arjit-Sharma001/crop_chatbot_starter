import pandas as pd

DATA_FILE = "data2.csv"

df = pd.read_csv(DATA_FILE)

def get_yield_trend():
    return f"Avg yield over years: {df.groupby('Year')['CropYield'].mean().round(2).to_dict()}"

def get_soil_moisture_trend():
    return f"Soil moisture avg per year: {df.groupby('Year')['SoilMoisture'].mean().round(2).to_dict()}"

def handle_query(keywords):
    if "yield" in keywords:
        return get_yield_trend()
    elif "moisture" in keywords or "soil" in keywords:
        return get_soil_moisture_trend()
    else:
        return "I couldn't find relevant info. Try asking about 'yield' or 'soil moisture'."
