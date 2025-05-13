# 🧭 TravelSalesmanGoogleApi

A lightweight script that calculates the most efficient route between multiple locations using the **Google Maps API**. Ideal for tackling simplified versions of the **Traveling Salesman Problem (TSP)**.

> **Disclaimer:**  
> This project uses the Google Maps API and is **not affiliated with or endorsed by Google**. Usage of the API must comply with [Google’s Terms of Service](https://developers.google.com/terms).

---

## 🚀 Features

- Optimizes travel routes between multiple locations
- Integrates with the Google Maps Directions API
- Easy setup and minimal configuration
- Future-ready for CLI and file input options

---

## 🛠️ Setup

### 1. Get a Google API Key

To use this script, you must have a valid Google Maps API key.  
Follow the instructions here:  
👉 [Get an API Key](https://cloud.google.com/docs/authentication/api-keys)

Ensure the following APIs are **enabled** in your Google Cloud Console:
- **Directions API**
- **Maps JavaScript API** (if using maps in the browser)
- **Geocoding API** (if using address-to-coordinates conversion)

### 2. Configure Environment Variables

Create a `.env` file in the project’s root directory and add your API key:

```env
GOOGLE_API_KEY="your_google_api_key_here"
```
⚠️ Important:
Do not commit your .env file to version control. It contains sensitive information.

---

## ▶️ Usage
Currently, the addresses are hardcoded inside main.py.
In future versions, address input via command-line arguments or file upload will be supported.

To run the script:

```bash
python main.py
```

---

## 📄 License
This project is licensed under the Apache 2.0 License.
