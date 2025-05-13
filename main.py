import requests

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

BI = "Białystok"

addresses = [
    f"Studio Łazienek AGA Sp. J., {BI}",
    f"INTERO internetowy salon łazienek, {BI}",
    f"Bocaro Galeria Łazienek, {BI}",
    f"BLU Sp. z o.o. sp. k. Centrala (dawniej BR Konsorcjum), {BI}",
    f"Saber łazienki wnętrza, {BI}",
    f"Aneks Sp. z o.o., {BI}",
    f"Drew-Met {BI}",
    f"KREATOR Studio Łazienek, {BI}",
]


# --- Krok 1: Geokodowanie ---
def geocode_address(address):
    url = f"https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": address, "key": API_KEY}
    response = requests.get(url, params=params).json()
    location = response["results"][0]["geometry"]["location"]
    return (location["lat"], location["lng"])


# --- Krok 2: Macierz odległości ---
def get_distance_matrix(coords):
    origins = destinations = "|".join([f"{lat},{lng}" for lat, lng in coords])
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": origins,
        "destinations": destinations,
        "key": API_KEY,
        "mode": "driving"
    }
    response = requests.get(url, params=params).json()
    matrix = []
    for row in response["rows"]:
        matrix.append([el["distance"]["value"] for el in row["elements"]])
    return matrix


# --- Krok 3: Heurystyczny TSP: najbliższy sąsiad ---
def nearest_neighbor(matrix):
    n = len(matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True

    for _ in range(n - 1):
        last = route[-1]
        next_city = min((i for i in range(n) if not visited[i]), key=lambda i: matrix[last][i])
        route.append(next_city)
        visited[next_city] = True
    return route


# --- Krok 4: Directions API - pobierz trasę ---
def get_route_directions(route, coords):
    waypoints = "|".join([f"{coords[i][0]},{coords[i][1]}" for i in route[1:-1]])
    origin = f"{coords[route[0]][0]},{coords[route[0]][1]}"
    destination = f"{coords[route[-1]][0]},{coords[route[-1]][1]}"

    url = f"https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": origin,
        "destination": destination,
        "waypoints": waypoints,
        "key": API_KEY
    }
    response = requests.get(url, params=params).json()
    return response["routes"][0]["legs"]

# --- Wyświetl trasę ---
def format_duration(seconds):
    minutes, sec = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours}h {minutes}m"
    return f"{minutes}m"


def display_best_route(directions):
    total_km = 0
    total_time = 0
    for i, leg in enumerate(directions):
        distance = leg["distance"]["value"]
        duration = leg["duration"]["value"]
        total_km += distance
        total_time += duration
        print(
            f"{i + 1:>2}. {leg['start_address']} ➡ {leg['end_address']}\n"
            f"     🚗 {leg['distance']['text']}   ⏱️ {leg['duration']['text']}"
        )
    print("-" * 50)
    print(f"📏 Łącznie: {total_km / 1000:.2f} km")
    print(f"⏳ Czas całkowity: {format_duration(total_time)}")


def main():
    coordinates = [geocode_address(addr) for addr in addresses]
    distance_matrix = get_distance_matrix(coordinates)
    route_order = nearest_neighbor(distance_matrix)
    directions = get_route_directions(route_order, coordinates)
    display_best_route(directions)

if __name__ == "__main__":
    main()
