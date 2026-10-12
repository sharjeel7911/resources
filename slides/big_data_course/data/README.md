# 📦 Datasets

This folder contains sample datasets for the SE446 Big Data Analytics course.

## 📁 Sample Datasets (Included in Repository)

These sample datasets are included directly in this repository for quick testing and development:

| Dataset | Records | Format | Description |
|---------|---------|--------|-------------|
| `nyc_taxi_sample.csv` | 50 | CSV | NYC Yellow Taxi trips with fares, tips, locations |
| `chicago_crimes_sample.csv` | 30 | CSV | Chicago Police crime incidents with GPS coords |
| `nyc_weather_sample.csv` | 40 | CSV | Daily weather data for NYC (temp, snow, rain) |
| `air_quality_sample.csv` | 40 | CSV | Air Quality Index for 5 major US cities |

## 🚀 Quick Start (Using Sample Data)

Load directly from GitHub raw URLs in Google Colab or Databricks:

```python
import pandas as pd

# Base URL for raw files
BASE_URL = "https://raw.githubusercontent.com/aniskoubaa/big_data_course/main/data/"

# NYC Taxi Data (50 trips)
taxi_df = pd.read_csv(BASE_URL + "nyc_taxi_sample.csv")
print(f"Taxi records: {len(taxi_df)}")

# Chicago Crimes (30 incidents)
crimes_df = pd.read_csv(BASE_URL + "chicago_crimes_sample.csv")
print(f"Crime records: {len(crimes_df)}")

# NYC Weather (40 days)
weather_df = pd.read_csv(BASE_URL + "nyc_weather_sample.csv")
print(f"Weather records: {len(weather_df)}")

# Air Quality Index (40 records, 5 cities)
aqi_df = pd.read_csv(BASE_URL + "air_quality_sample.csv")
print(f"AQI records: {len(aqi_df)}")
```

## 📥 Full Datasets (Kaggle - Free Account Required)

For the complete project work, download full datasets from Kaggle:

| Dataset | Kaggle Link | Full Size |
|---------|-------------|-----------|
| NYC Yellow Taxi | [kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data) | ~50 MB |
| Chicago Crimes | [kaggle.com/datasets/chicago/chicago-crime](https://www.kaggle.com/datasets/chicago/chicago-crime) | ~30 MB |
| NYC Weather | [kaggle.com/datasets/danbraswell/new-york-city-weather-data-2019](https://www.kaggle.com/datasets/danbraswell/new-york-city-weather-data-2019) | ~5 MB |
| Air Quality Index | [kaggle.com/datasets/programmerrdai/air-quality-data-2012-to-2024](https://www.kaggle.com/datasets/programmerrdai/air-quality-data-2012-to-2024) | ~3 MB |

### How to Download from Kaggle:
1. Create a free Kaggle account at [kaggle.com](https://www.kaggle.com)
2. Navigate to the dataset page
3. Click "Download" button
4. Upload to Google Colab or Databricks

## 📊 Dataset Schema Details

### NYC Yellow Taxi (`nyc_taxi_sample.csv`)
| Column | Type | Description |
|--------|------|-------------|
| VendorID | int | TPEP provider (1=CMT, 2=VeriFone) |
| tpep_pickup_datetime | datetime | Trip start time |
| tpep_dropoff_datetime | datetime | Trip end time |
| passenger_count | int | Number of passengers |
| trip_distance | float | Miles traveled |
| RatecodeID | int | Rate code (1=Standard, 2=JFK, 3=Newark, etc.) |
| store_and_fwd_flag | string | Y/N - stored before sending |
| PULocationID | int | Pickup location zone |
| DOLocationID | int | Dropoff location zone |
| payment_type | int | 1=Credit, 2=Cash, 3=No charge, 4=Dispute |
| fare_amount | float | Base fare ($) |
| extra | float | Extras and surcharges ($) |
| mta_tax | float | MTA tax ($0.50) |
| tip_amount | float | Tip amount ($) - credit card only |
| tolls_amount | float | Tolls paid ($) |
| improvement_surcharge | float | Improvement surcharge ($0.30) |
| total_amount | float | Total charged ($) |
| congestion_surcharge | float | NYS congestion surcharge ($2.50) |
| airport_fee | float | Airport pickup fee ($1.75 for JFK/LGA) |


### Chicago Crimes (`chicago_crimes_sample.csv`)
| Column | Type | Description |
|--------|------|-------------|
| ID | int | Unique identifier |
| Case Number | string | CPD case number |
| Date | datetime | When crime occurred |
| Primary Type | string | Crime category (THEFT, BATTERY, etc.) |
| Description | string | Detailed crime type |
| Location Description | string | Where it happened |
| Arrest | boolean | Was arrest made? |
| Domestic | boolean | Was it domestic-related? |
| District | int | Police district |
| Latitude | float | GPS latitude |
| Longitude | float | GPS longitude |

### NYC Weather (`nyc_weather_sample.csv`)
| Column | Type | Description |
|--------|------|-------------|
| date | date | Calendar date |
| temp_max | int | Maximum temperature (°F) |
| temp_min | int | Minimum temperature (°F) |
| temp_avg | int | Average temperature (°F) |
| precipitation | float | Rainfall (inches) |
| snow | float | Snowfall (inches) |
| wind_speed | float | Avg wind speed (mph) |
| weather_condition | string | Clear, Rain, Snow, etc. |

### Air Quality Index (`air_quality_sample.csv`)
| Column | Type | Description |
|--------|------|-------------|
| date | date | Measurement date |
| city | string | City name |
| aqi_value | int | AQI value (0-500) |
| aqi_category | string | Good/Moderate/Unhealthy |
| main_pollutant | string | PM2.5, Ozone, PM10, etc. |
| pm25 | float | Fine particulate matter |
| ozone | float | Ozone level |

## 🔗 Official Data Sources

- **NYC Taxi:** [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- **Chicago Crimes:** [Chicago Data Portal](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)
- **Weather:** [NOAA Climate Data Online](https://www.ncdc.noaa.gov/cdo-web/datasets)
- **Air Quality:** [EPA Air Quality System](https://aqs.epa.gov/aqsweb/airdata/download_files.html)

---

**Note:** Sample datasets are for testing and learning. Use full Kaggle datasets for realistic project analysis.
