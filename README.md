# distance_determination
determining the distance between points
Opis:

Jest to aplikacja która umożliwia wyliczanie dystansu pomiędzy dwoma punktami, posiadając tylko współrzędne geograficzne dwóch punktów, wprowadzone prze użytkownika. Bazuje na OSMR API. Rezultat podawany jest w kilometrach.

Sposób użycia:

Uruchomić kod w środowisku pozwalającym uruchomanie skryptów Python, wprowadzić współrzędne geograficzne, odczytac wynik.

Wymagania:

1.sprawdzenie poprawności danych wprowadzanych przez użytkowników;
2.obsługa błędów w komunikacji z API;
Jakie dane posiadamy:

1.współrzędzne geograficzne dwoch punktów (podane przez uzytkownika);
2.zewnętrzne źródło danych: Api Open Streat Map;
3.rezultat: odległość w kilometrach;
Wykonanie:

Sprawdzenie Api Open Streat Map, jakie dane udostępnia. Jak możemy na podstawie danych pozyskanych z api wyliczyć dystans. OSM API udostępnia surowe dane geoprzestrzenne, dla wyznaczenia dystansu musimy skorzystac z serwisów bazujących na OSM umożliwiających trasowanie (np.OSMR,GraphHopper)

Naszym wymaganiom odpowiada ROUT Servis (OSMR API), na jego podstawie będzimy budować narzedzie zwracające dystans

Model działania aplikacji:

1.Użytkownik wprowadza koordynaty punktow A i B;
2.Program tworzy URL z parametrami współrzędnych podanych przez uzytkownika;
3.Wysyłamy zapytanie HTTP do API OSMR;  
4.Sprawdzamy kod odpowiedzi;
5.Parsowanie danych JSON;
6.Odczytujemy wartości "distance";
7.Zwracamy odpowiedź uzytkownikowi o dlugości danego odciku;
Co warto wziąć pod uwagę

Dystans jest wyliczany na podstawie wyznaczania trasy drogowej pomiędzy dwoma punktami, przy braku możliwości wyznaczania trasy - brak wyniku. Wynik różni się od rzeczywistej geodezyjnej długości wyliczanej na podstawie linii prostej.

Możliwe ulepszenia /zagrożenia dla aplikacji i wykorzystania:

Ulepszenia:

1.Dodanie nazw wytypowanych punktów przy użyciu nominatim api.
2.Dodanie możliwości wyboru wyznaczonej trasy (pieszo,samochodem,rowerem).
3.Dodanie wizualizacji trasy na mapie przy użuciu biblioteki np.folium.
4.Zapis wyników do pliku w celu dalszej analizy.
Zagrożenia:

1.Problemy z siecią: API wymaga dostępu do internetu, co może uniemożliwić działanie aplikacji w trybie offline.
2.Limit API OSRM: Publiczny serwer ma ograniczoną wydajność; w przypadku dużej liczby zapytań mogą pojawić się opóźnienia lub limity.
3.Nieprawidłowe dane wejściowe: Brak walidacji współrzędnych może prowadzić do błędów
Linki:

https://project-osrm.org/docs/v5.5.1/api/?language=cURL#route-service

https://wiki.openstreetmap.org/wiki/Software_libraries

https://nominatim.org/
