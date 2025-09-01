# main.py
# Main script for the Weather Tracker application.
# Collects city names from user, fetches weather data, and displays reports.

from weather_utils import fetch_weather  # Import the fetch function

def main():
    """
    Main function to run the Weather Tracker program.
    """
    cities = []
    print("Enter city names (type 'done' to finish):")
    
    while True:
        city_input = input("City: ").strip()
        if city_input.lower() == 'done':
            break
        if city_input:
            cities.append(city_input)
    
    if not cities:
        print("No cities entered. Exiting.")
        return
    
    print("Weather Report:")
    
    for city in cities:
        weather = fetch_weather(city)
        if weather:
            print(weather)
            print("-" * 110)  # Separator line as per sample

if __name__ == "__main__":
    main()