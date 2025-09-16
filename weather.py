import requests
import pandas as pd
import dask.dataframe as dd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from meteostat import Point, Daily
from datetime import datetime, timedelta



API_KEY = "5d016d810e7382a90ac6d7007767023f"


cities_input = input("Enter city names (comma-separated): ")
try:
    num_days = int(input("Enter number of days to analyze : "))
except ValueError:
    num_days = 30

city_list = [city.strip() for city in cities_input.split(",") if city.strip()]


end = datetime.now()
start = end - timedelta(days=num_days)


fig, ax = plt.subplots(figsize=(12, 6))
stats_data = []


for city in city_list:
    try:
        print(f"\n Fetching data for {city}...")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url).json()

        if "main" not in response or "coord" not in response:
            print(f" OpenWeatherMap error for {city}: {response.get('message', 'No data')}")
            continue

        current_temp = response["main"]["temp"]
        lat = response["coord"]["lat"]
        lon = response["coord"]["lon"]


        location = Point(lat, lon)
        hist_data = Daily(location, start, end).fetch()

        if hist_data.empty:
            print(f" No historical data found for {city}")
            continue

        hist_data = hist_data.reset_index()
        hist_data = hist_data.rename(columns={"tavg": "Temperature"})
        hist_data["city"] = city


        now = datetime.now()
        current_df = pd.DataFrame([{
            "time": now,
            "Temperature": current_temp,
            "city": city
        }])

        combined_df = pd.concat([hist_data[["time", "Temperature", "city"]], current_df])
        print(f"\n📅 Daily Temperatures for {city}:")
        for i, row in combined_df.iterrows():
            print(f"{row['time'].strftime('%Y-%m-%d')}: {row['Temperature']} °C")



        ddf = dd.from_pandas(combined_df, npartitions=2)
        avg_temp = ddf["Temperature"].mean().compute()
        max_temp = ddf["Temperature"].max().compute()
        min_temp = ddf["Temperature"].min().compute()
        std_temp = ddf["Temperature"].std().compute()


        print(f" {city}")
        print(f"Average Temperature: {avg_temp:.2f} °C")
        print(f"Max Temperature:     {max_temp:.2f} °C")
        print(f"Min Temperature:     {min_temp:.2f} °C")
        print(f"Std Deviation:       {std_temp:.2f} °C")


        stats_data.append({
            "City": city,
            "Avg Temp (°C)": avg_temp,
            "Max Temp (°C)": max_temp,
            "Min Temp (°C)": min_temp,
            "Std Dev (°C)": std_temp
        })

        # Plot
        ax.plot(combined_df["time"], combined_df["Temperature"], label=city)

    except Exception as e:
      print("Error processing", city + ":", e)



if len(ax.lines) > 0:
    ax.set_title("Temperature Trends Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()

    chart_path = "weather_chart.png"
    plt.savefig(chart_path)
    print(f"\n Chart saved as: {chart_path}")


if stats_data:
    stats_df = pd.DataFrame(stats_data)
    csv_path = "weather_stats.csv"
    stats_df.to_csv(csv_path, index=False)
    print(f" Stats exported to: {csv_path}")
else:
    print("No statistics to save.")

    plt.show()

