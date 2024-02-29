import tkinter as tk

class CurrencyConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Currency Converter")
        
        self.amount_label = tk.Label(master, text="Amount:")
        self.amount_label.grid(row=0, column=0)
        self.amount_entry = tk.Entry(master)
        self.amount_entry.grid(row=0, column=1)
        
        self.source_label = tk.Label(master, text="Source Currency:")
        self.source_label.grid(row=1, column=0)
        self.source_currency_var = tk.StringVar()
        self.source_currency_var.set("INR")
        self.source_currency_option = tk.OptionMenu(master, self.source_currency_var, "INR", "USD")
        self.source_currency_option.grid(row=1, column=1)
        
        self.target_label = tk.Label(master, text="Target Currency:")
        self.target_label.grid(row=2, column=0)
        self.target_currency_var = tk.StringVar()
        self.target_currency_var.set("USD")
        self.target_currency_option = tk.OptionMenu(master, self.target_currency_var, "INR", "USD")
        self.target_currency_option.grid(row=2, column=1)
        
        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, column=0, columnspan=2)
        
        self.result_label = tk.Label(master, text="Converted Amount:")
        self.result_label.grid(row=4, column=0)
        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(master, textvariable=self.result_var, state='readonly')
        self.result_entry.grid(row=4, column=1)
        
        self.refresh_button = tk.Button(master, text="Refresh", command=self.refresh)
        self.refresh_button.grid(row=5, column=0, columnspan=2)
        
        # Fixed exchange rate
        self.exchange_rate = 83  # 1 USD = 83 INR
        
    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            source_currency = self.source_currency_var.get()
            target_currency = self.target_currency_var.get()
            
            if source_currency == target_currency:
                self.result_var.set("Source and target currencies must be different.")
                return
            
            if source_currency == "INR" and target_currency == "USD":
                converted_amount = amount / self.exchange_rate
            elif source_currency == "USD" and target_currency == "INR":
                converted_amount = amount * self.exchange_rate
            else:
                self.result_var.set("Conversion not supported.")
                return
            
            self.result_var.set(f"{converted_amount:.2f} {target_currency}")
        except ValueError:
            self.result_var.set("Invalid amount.")
        
    def refresh(self):
        self.amount_entry.delete(0, tk.END)
        self.result_var.set("")
        
def main():
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
