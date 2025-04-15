import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import os

DATA_PATH = "data2.csv"
STATIC_DIR = "static"

def generate_chart(chart_type: str, plot_type: str = "line") -> str:
    try:
        df = pd.read_csv(DATA_PATH)
    except Exception as e:
        return f"Error reading data: {e}"

    os.makedirs(STATIC_DIR, exist_ok=True)
    filename = f"{STATIC_DIR}/{chart_type}_{plot_type}.png"

    try:
        if chart_type == "yield_over_years":
            df.plot(x='Year', y='CropYield', title="Crop Yield Over Years", kind=plot_type)
        elif chart_type == "temp_vs_yield":
            df.plot(x='Temperature', y='CropYield', title="Temperature vs Yield", kind=plot_type)
        elif chart_type == "soil_moisture_over_time":
            df.plot(x='Year', y='SoilMoisture', title="Soil Moisture Over Time", kind=plot_type)
        else:
            return ""

        plt.savefig(filename)
        plt.close()
        return filename
    except Exception as e:
        return f"Error generating chart: {e}"
