import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import threading
import io
import requests
import json
import os

def get_weather_data(city: str):
    # Read API key from environment to avoid accidental placeholder usage.
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    if not API_KEY:
        return {
            "success": False,
            "error": (
                "OpenWeather API key not set.\n"
                "Please set the environment variable OPENWEATHER_API_KEY or add your key to the script."
            ),
        }

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        r = requests.get(url, timeout=8)
        r.raise_for_status()
        raw = r.json()
        # OpenWeather returns cod as int or str depending on error/success; normalize check
        cod = int(raw.get("cod", 0)) if str(raw.get("cod", "0")).isdigit() else raw.get("cod")
        if cod != 200:
            return {"success": False, "error": raw.get("message", "Unknown error")}
        data = {
            "city": raw.get("name"),
            "temp": raw["main"]["temp"],
            "condition": raw["weather"][0]["description"].title(),
            "humidity": raw["main"]["humidity"],
            "wind_speed": raw["wind"]["speed"],
            "raw": raw,
        }
        return {"success": True, "data": data}
    except requests.RequestException as e:
        return {"success": False, "error": f"Network error: {e}"}
    except Exception as e:
        return {"success": False, "error": str(e)}


class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather — Mini Projects")
        self.geometry("480x360")
        self.resizable(False, False)
        self.style = ttk.Style(self)
        self.style.theme_use("clam")

        self._build_ui()
        self._icon_img_ref = None  # Initialize icon image reference

    def _build_ui(self):
        frm = ttk.Frame(self, padding=16)
        frm.pack(fill=tk.BOTH, expand=True)

        header = ttk.Label(frm, text="Current Weather", font=("Arial", 18, "bold"))
        header.pack(pady=(0, 12))

        inp_row = ttk.Frame(frm)
        inp_row.pack(fill=tk.X, pady=(0, 10))

        self.city_var = tk.StringVar()
        city_entry = ttk.Entry(inp_row, textvariable=self.city_var)
        city_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        city_entry.bind("<Return>", lambda e: self.fetch())

        fetch_btn = ttk.Button(inp_row, text="Fetch", command=self.fetch)
        fetch_btn.pack(side=tk.LEFT, padx=(8, 0))

        self.sep = ttk.Separator(frm, orient=tk.HORIZONTAL)
        self.sep.pack(fill=tk.X, pady=8)

        self.result_frame = ttk.Frame(frm)
        self.result_frame.pack(fill=tk.BOTH, expand=True)

        # Left: icon
        left = ttk.Frame(self.result_frame)
        left.pack(side=tk.LEFT, padx=(0, 12))
        self.icon_label = ttk.Label(left)
        self.icon_label.pack()

        # Right: details
        right = ttk.Frame(self.result_frame)
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.city_label = ttk.Label(right, text="—", font=("Arial", 14, "bold"))
        tkw = tk.W
        self.city_label.pack(anchor=tkw)

        self.cond_label = ttk.Label(right, text="Condition: —")
        self.cond_label.pack(anchor=tk.W, pady=(6, 0))

        self.temp_label = ttk.Label(right, text="Temperature: —")
        self.temp_label.pack(anchor=tk.W, pady=(6, 0))

        self.hum_label = ttk.Label(right, text="Humidity: —")
        self.hum_label.pack(anchor=tk.W, pady=(6, 0))

        self.wind_label = ttk.Label(right, text="Wind: —")
        self.wind_label.pack(anchor=tk.W, pady=(6, 0))

        # Status bar
        self.status = ttk.Label(self, text="Ready", anchor=tk.W)
        self.status.pack(fill=tk.X, side=tk.BOTTOM)

    def set_status(self, text: str):
        self.status.config(text=text)

    def fetch(self):
        city = self.city_var.get().strip()
        if not city:
            messagebox.showinfo("Input required", "Please enter a city name.")
            return

        # Run network call in background
        self.set_status("Fetching...")
        threading.Thread(target=self._fetch_thread, args=(city,), daemon=True).start()

    def _fetch_thread(self, city: str):
        res = get_weather_data(city=city)
        if not res.get("success"):
            self.after(0, lambda: (self.set_status("Error"), messagebox.showerror("Error", res.get("error"))))
            return

        data = res["data"]
        city_name = data.get("city")
        temp = data.get("temp")
        cond = data.get("condition")
        humidity = data.get("humidity")
        wind = data.get("wind_speed")

        # Attempt to fetch OpenWeather icon if available
        icon_img = None
        try:
            raw = data.get("raw", {})
            weather = raw.get("weather")
            if isinstance(weather, list) and weather:
                icon = weather[0].get("icon")
                if icon:
                    url = f"http://openweathermap.org/img/wn/{icon}@2x.png"
                    r = requests.get(url, timeout=6)
                    r.raise_for_status()
                    img_data = r.content
                    pil = Image.open(io.BytesIO(img_data)).resize((96, 96), Image.Resampling.LANCZOS)
                    icon_img = ImageTk.PhotoImage(pil)
        except Exception:
            icon_img = None

        # Update UI on main thread
        def update():
            self.set_status("Ready")
            self.city_label.config(text=f"{city_name}")
            self.cond_label.config(text=f"Condition: {cond}")
            self.temp_label.config(text=f"Temperature: {temp} °C")
            self.hum_label.config(text=f"Humidity: {humidity}%")
            self.wind_label.config(text=f"Wind: {wind} m/s")
            if icon_img:
                self.icon_label.config(image=icon_img)
                self._icon_img_ref = icon_img  # Keep a reference to prevent garbage collection
            else:
                self.icon_label.config(image="", text="—")

        self.after(0, update)


if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
