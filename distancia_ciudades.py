import geopy.distance
from geopy.geocoders import Nominatim

def obtener_coordenadas(ciudad):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(ciudad)
    return (location.latitude, location.longitude)

def calcular_distancia(coord_origen, coord_destino):
    return geopy.distance.distance(coord_origen, coord_destino).km

def main():
    while True:
        print("Ingrese 's' para salir.")
        ciudad_origen = input("Ciudad de Origen: ")
        if ciudad_origen.lower() == 's':
            break
        ciudad_destino = input("Ciudad de Destino: ")
        if ciudad_destino.lower() == 's':
            break

        try:
            coord_origen = obtener_coordenadas(ciudad_origen)
            coord_destino = obtener_coordenadas(ciudad_destino)

            distancia_km = calcular_distancia(coord_origen, coord_destino)
            distancia_millas = distancia_km * 0.621371

            print(f"Distancia entre {ciudad_origen} y {ciudad_destino}:")
            print(f"{distancia_km:.2f} kilómetros")
            print(f"{distancia_millas:.2f} millas")

            print("Seleccione el medio de transporte:")
            print("1. Coche (80 km/h)")
            print("2. Bicicleta (20 km/h)")
            print("3. Avión (900 km/h)")
            opcion = input("Opción: ")

            if opcion == '1':
                velocidad = 80
                medio = "Coche"
            elif opcion == '2':
                velocidad = 20
                medio = "Bicicleta"
            elif opcion == '3':
                velocidad = 900
                medio = "Avión"
            else:
                print("Opción no válida.")
                continue

            duracion_horas = distancia_km / velocidad
            duracion_minutos = duracion_horas * 60

            print(f"Duración del viaje en {medio}:")
            print(f"{duracion_horas:.2f} horas")
            print(f"{duracion_minutos:.2f} minutos")

        except Exception as e:
            print(f"Error al obtener la información: {e}")

if __name__ == "__main__":
    main()
