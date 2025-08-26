import tkinter as tk
from tkinter import ttk
from currency_converter import fetch_conversion, get_supported_symbols


class CurrencyConverterGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Converter")
        self.resizable(False, False)

        main = ttk.Frame(self, padding=12)
        main.grid(row=0, column=0)

        ttk.Label(main, text="From (e.g. KES)").grid(row=0, column=0, sticky="w")
        self.from_var = tk.StringVar()
        self.from_widget = None

        # Try to populate dropdown from supported symbols
        symbols = sorted(get_supported_symbols())
        if symbols:
            self.from_var.set('KES')
            self.from_widget = ttk.Combobox(main, textvariable=self.from_var, values=symbols, width=10)
            self.from_widget.state(['!disabled', 'readonly'])
            self.from_widget.grid(row=0, column=1)
        else:
            self.from_var.set('KES')
            self.from_widget = ttk.Entry(main, textvariable=self.from_var, width=10)
            self.from_widget.grid(row=0, column=1)

        ttk.Label(main, text="To (e.g. USD)").grid(row=1, column=0, sticky="w")
        self.to_var = tk.StringVar()
        # use same symbols list
        if symbols:
            self.to_var.set('USD')
            self.to_widget = ttk.Combobox(main, textvariable=self.to_var, values=symbols, width=10)
            self.to_widget.state(['!disabled', 'readonly'])
            self.to_widget.grid(row=1, column=1)
        else:
            self.to_var.set('USD')
            self.to_widget = ttk.Entry(main, textvariable=self.to_var, width=10)
            self.to_widget.grid(row=1, column=1)

        ttk.Label(main, text="Amount").grid(row=2, column=0, sticky="w")
        self.amount_var = tk.StringVar(value="1")
        ttk.Entry(main, textvariable=self.amount_var, width=12).grid(row=2, column=1)

        self.convert_btn = ttk.Button(main, text="Convert", command=self.on_convert)
        self.convert_btn.grid(row=3, column=0, columnspan=2, pady=(8, 0))

        self.result_lbl = ttk.Label(main, text="", font=("Arial", 11))
        self.result_lbl.grid(row=4, column=0, columnspan=2, pady=(8, 0))

    def on_convert(self):
        frm = self.from_var.get().strip().upper()
        to = self.to_var.get().strip().upper()
        try:
            amt = float(self.amount_var.get())
        except ValueError:
            self.result_lbl.config(text="Invalid amount")
            return

        self.convert_btn.config(state="disabled")
        self.result_lbl.config(text="Converting...")
        self.update_idletasks()

        converted, err = fetch_conversion(frm, to, amt)
        if converted is not None:
            self.result_lbl.config(foreground="black", text=f"{amt} {frm} = {converted:.2f} {to}")
        else:
            # Show error messages in red
            self.result_lbl.config(foreground="red", text=err if err is not None else "Unknown error")

        self.convert_btn.config(state="normal")


if __name__ == "__main__":
    app = CurrencyConverterGUI()
    app.mainloop()
