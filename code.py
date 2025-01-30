!pip install requests
import requests

# Funkcja pobierania współrzędnych od użytkownika
def get_coordinates():
    print("Podaj współrzędne punktu A:")
    lat1 = float(input("Szerokość geograficzna (lat): "))
    lon1 = float(input("Długość geograficzna (lon): "))
    print("Podaj współrzędne punktu B:")
    lat2 = float(input("Szerokość geograficzna (lat): "))
    lon2 = float(input("Długość geograficzna (lon): "))
    return lon1, lat1, lon2, lat2

# Funkcja obliczania odległości między punktami
def calculate_distance(lon1, lat1, lon2, lat2):
    # Adres  OSRM Route API
    osrm_route_url = "http://router.project-osrm.org/route/v1/driving"
    # Tworzenie ciągu współrzędnych
    coordinates = str(lon1) + "," + str(lat1) + ";" + str(lon2) + "," + str(lat2)

    # Wysyłanie zapytania do OSRM API
    response = requests.get(osrm_route_url + "/" + coordinates, params={"overview": "false"})

    # Sprawdzanie odpowiedzi
    if response.status_code == 200:
        route_data = response.json()
        if 'routes' in route_data and len(route_data['routes']) > 0:
            # Pobieranie odległości i konwersja w kilometry
            distance_meters = route_data['routes'][0]['distance']
            distance_km = distance_meters / 1000
            print("Odległość między punktami wynosi: " + str(round(distance_km, 2)) + " km")
        else:
            # API działa, ale nie może wyznaczyć trasy
            print("Brak możliwości wyznaczenia trasy")
    elif response.status_code == 400:
        # Niepoprawne dane wejściowe
        print("Błąd: Niepoprawne dane. Upewnij się, że dane są poprawnie wprowadzone (np. lat = 52.2297).")
    else:
        # Inny problem z API
        print("Błąd połączenia z API: "+ str({response.status_code}))
        print("Odpowiedź serwera: "+ str({response.text}))

# Kontrola wykonania
if __name__ == "__main__":
    lon1, lat1, lon2, lat2 = get_coordinates()
    calculate_distance(lon1, lat1, lon2, lat2)
