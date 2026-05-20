import math
num_points = 120
print(num_points)
# Comenzar con un número
location_data = 42.3601
# Cambiar a texto
location_data = "Boston"
# Cambiar a una lista de coordenadas
location_data = [42.3601, -71.0589]
print(location_data)
# Buenos nombres de variables para datos geoespaciales
latitude = 42.3601
longitude = -71.0589
elevation = 147.2
city_name = "Boston"
population = 685094
coordinate_system = "WGS 84"
print(latitude, longitude, elevation, city_name, population, coordinate_system)
# Tipos de datos
num_features = 500
print(type(num_features))
latitude = 35.6895
print(type(latitude))
longitude = 139.6917
print(type(longitude))
coordinate_system = "WGS 84"
print(type(coordinate_system))
is_urban = True
print(type(is_urban))
# listas de coordenadas
location_data = [42.3601, -71.0589]
print(type(location_data))
# Diccionario de datos geoespaciales
location_info = {
    "latitude": 42.3601,
    "longitude": -71.0589,
    "elevation": 147.2,
    "city_name": "Boston",
    "population": 685094,
    "coordinate_system": "WGS 84"
}
print(type(location_info))
print(location_info)
num_features += 100
print(num_features)
latitude = 42.3601
latitude_radians = math.radians(latitude)
print(latitude_radians)
# Caracteres de escape insertar una nueva línea
print("La ciudad de\nBoston tiene una población de 685094 habitantes.")
# Caracteres de escape insertar una tabulación
print("La ciudad de\tBoston tiene una población de 685094 habitantes.")
# COmbinación de caracteres de escape
print("La ciudad de\n\tBoston tiene una población de 685094 habitantes.")
# Usar comillas simples para evitar el uso de caracteres de escape
print('What\'s your name?')
print("What's your name?")  # Usar comillas dobles para evitar el uso de
# Operaciones con cadenas de texto
city_name = "Boston city"
print(city_name.upper())
print(city_name.lower())
print(city_name.replace("o", "0"))
print(city_name.replace("Boston", "Yale"))
print(city_name.split("o"))
print(city_name.title())
# Quitando espacios en blanco
city_name = "  Boston city  "
print(city_name.strip())
print(city_name.lstrip())
print(city_name.rstrip())

latitude = 40.7128
longitude = -74.0060
population = 8336817
area = 783.8
population_density = population / area
print(population_density)
print(f'Latitude: {latitude}, Longitude: {longitude}, Population Density: {population_density:.2f} people per square kilometer')

city_name = "New York City"
print(city_name.lower())
print(city_name.upper())
print(city_name.replace("New York", "Los Angeles"))
