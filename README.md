# 🧭 TravelSalesmanGoogleApi

A simple and useful script to determine the most efficient route between multiple locations using the **Google Maps API**. Perfect for solving simplified versions of the **Traveling Salesman Problem (TSP)**.

> **Disclaimer:**  
> This project uses the Google Maps API. It is **not affiliated with or endorsed by Google**. Use of the API must comply with [Google’s Terms of Service](https://developers.google.com/terms).

---

## 🚀 Features

- Calculates optimized travel routes
- Integrates with Google Maps Directions API
- Lightweight and easy to configure

---

## 🛠️ Setup

### 1. Get a Google API Key
To use this script, you need a Google Maps API key. Follow the instructions here:  
👉 [Get an API key](https://cloud.google.com/docs/authentication/api-keys)

Make sure the following APIs are enabled in your Google Cloud Console:
- **Maps JavaScript API**
- **Directions API**
- **Geocoding API**

---

### 2. Configure Environment Variables

Create a `.env` file in the root directory and add your API key:

```env
GOOGLE_API_KEY="your_google_api_key_here"
