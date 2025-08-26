import os
import sys
import argparse
import requests


def get_weather(city: str, api_key: str | None, debug: bool = False):
    import os
    import sys
    import argparse
    import requests
    from typing import Optional, Dict, Any


    def get_weather_data(city: str, api_key: Optional[str] = None, debug: bool = False) -> Dict[str, Any]:
        """Fetch current weather for `city` from OpenWeather and return a structured result.

        Returns a dict with keys:
          - success: bool
          - data: dict (present when success is True)
          - error: str (present when success is False)
        """
        user_city = city.strip()
        if not user_city:
            return {"success": False, "error": "No city provided."}

        # Determine key priority: explicit provided key > env var > embedded fallback
        key = api_key or os.getenv("OPENWEATHER_API_KEY")
        if not key:
            # Fallback key (keep for convenience; you should provide your own key)
            key = "e9722d06623573de83654eb98d21c4d5"

        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": user_city,
            "appid": key,
            "units": "metric",
        }

        if debug:
            try:
                req = requests.Request("GET", base_url, params=params).prepare()
                print(f"Debug: Request URL -> {req.url}")
            except Exception:
                pass

        try:
            response = requests.get(base_url, params=params, timeout=10)
        except requests.RequestException as e:
            return {"success": False, "error": f"Network error: {e}"}

        if debug:
            print(f"Debug: HTTP {response.status_code}")
            print("Debug: Raw response body:")
            print(response.text)

        if response.status_code != 200:
            try:
                err = response.json()
                msg = err.get("message") or err.get("cod") or response.text
            except ValueError:
                msg = response.text
            return {"success": False, "error": f"HTTP {response.status_code}: {msg}"}

        try:
            data = response.json()
        except ValueError:
            return {"success": False, "error": "Invalid JSON from API."}

        main = data.get("main", {})
        weather = data.get("weather")
        wind = data.get("wind", {})

        temp = main.get("temp")
        condition = (
            weather[0].get("description", "N/A").capitalize()
            if isinstance(weather, list) and weather
            else "N/A"
        )
        humidity = main.get("humidity")
        wind_speed = wind.get("speed")

        result = {
            "success": True,
            "data": {
                "city": user_city,
                "temp": temp,
                "condition": condition,
                "humidity": humidity,
                "wind_speed": wind_speed,
                "raw": data,
            },
        }
        return result


    def get_weather(city: str, api_key: Optional[str] = None, debug: bool = False):
        """Backward-compatible wrapper used by the CLI. Prints results to stdout."""
        res = get_weather_data(city=city, api_key=api_key, debug=debug)
        if not res.get("success"):
            print(f"Error: {res.get('error')}")
            return

        data = res["data"]
        print(f"Weather Data for {data['city']} Retrieved Successfully:")
        print(f"Temperature: {data['temp']}°C")
        print(f"Condition: {data['condition']}")
        print(f"Humidity: {data['humidity']}%")
        print(f"Wind Speed: {data['wind_speed']} m/s")


    def main(argv: Optional[list[str]] = None):
        parser = argparse.ArgumentParser(description="Simple OpenWeather current weather lookup")
        parser.add_argument("--city", "-c", help='City name (e.g. Mumbai or "Mumbai,IN")')
        parser.add_argument("--key", help="OpenWeather API key (overrides OPENWEATHER_API_KEY env var)")
        parser.add_argument("--debug", action="store_true", help="Print debug info (request URL and raw response)")

        args = parser.parse_args(argv)

        if args.city:
            city = args.city
        else:
            try:
                city = input("Enter city name: ")
            except (EOFError, KeyboardInterrupt):
                print("No city provided. Exiting.")
                return

        get_weather(city=city, api_key=args.key, debug=args.debug)


    if __name__ == "__main__":
        main()