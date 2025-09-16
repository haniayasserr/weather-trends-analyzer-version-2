

# 🌦️ Weather Trends Analyzer

A Python application that analyzes weather trends by combining current weather data with historical temperature records. Compare multiple cities and visualize temperature patterns over time.

## ✨ Features

- **Multi-city Analysis**: Compare weather trends across multiple cities simultaneously
- **Historical Data**: Analyze temperature patterns over the past 3. **Enter number of days** to analyze (default: 30):
   ```
   Enter number of days to analyze: 14
   ```

4. **View results:**
   - Daily temperature data printed to console
   - Statistical summary for each city
   - Interactive temperature chart
   - Files saved: `weather_chart.png` and `weather_stats.csv`

## 📊 Sample Output

```
📅 Daily Temperatures for Cairo:
2024-08-20: 28.5 °C
2024-08-21: 30.2 °C
...

🌡️ Cairo Statistics:
Average Temperature: 29.15 °C
Max Temperature:     35.80 °C
Min Temperature:     22.10 °C
Std Deviation:       3.45 °C

✅ Chart saved as: weather_chart.png
✅ Stats exported to: weather_stats.csv
```

## 📁 Output Files

- **`weather_chart.png`**: Line chart showing temperature trends for all cities
- **`weather_stats.csv`**: Statistical summary including average, min, max, and standard deviation

## 🔧 Configuration

### API Key Setup
Replace the API key in the script:
```python
API_KEY = "your_actual_api_key_here"
```

### Custom Time Range
The script prompts for number of days, or you can modify the default:
```python
num_days = 30  # Change default value here
```

## 🛠️ Dependencies

- **requests**: HTTP requests to weather APIs
- **pandas**: Data manipulation and analysis
- **dask**: Distributed computing for large datasets
- **matplotlib**: Data visualization and plotting
- **meteostat**: Historical weather data access

## 🌍 Supported Cities

Any city supported by OpenWeatherMap API, including:
- Major cities worldwide
- Cities with latitude/longitude coordinates
- Use exact city names for best results

## ⚠️ Troubleshooting

### Common Issues:

1. **"Invalid API key"**
   - Verify your OpenWeatherMap API key is correct
   - Ensure the API key is activated (may take a few minutes)

2. **"No historical data found"**
   - Some remote locations may lack historical data
   - Try a different nearby city

3. **Connection errors**
   - Check your internet connection
   - Verify API endpoints are accessible

4. **City not found**
   - Use exact city names (e.g., "New York" not "NYC")
   - Try adding country code: "London,UK"

## 📈 Example Use Cases

- **Travel Planning**: Compare temperatures across potential destinations
- **Climate Research**: Analyze temperature patterns and trends
- **Agricultural Planning**: Monitor temperature variations for farming
- **Energy Analysis**: Understand heating/cooling requirements


## 🙏 Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for weather API
- [Meteostat](https://meteostat.net/) for historical weather data
- Python community for excellent libraries


## 📋 Requirements

- Python 3.7+
- OpenWeatherMap API key (free registration required)

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/haniayasserr/weather-trends-analyzer-version-2.git
   cd weather-trends-analyzer-version-2
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv weather_env
   source weather_env/bin/activate  # On Windows: weather_env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Get your OpenWeatherMap API key:**
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Generate an API key
   - Replace `"5d016d810e7382a90ac6d7007767023f"` in the script with your actual API key

## 🎯 Usage

1. **Run the application:**
   ```bash
   python weather_analyzer.py
   ```

2. **Enter city names** when prompted (comma-separated for multiple cities):
   ```
   Enter city names (comma-separated): Cairo, London, New York
   ```

3
