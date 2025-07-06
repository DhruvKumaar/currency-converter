import tkinter as tk
from tkinter import ttk, messagebox

RATES = {
    'USD': 1, 'EUR': 0.91, 'GBP': 0.78, 'JPY': 149.50, 'CAD': 1.35,
    'AUD': 1.48, 'CNY': 7.18, 'INR': 83.42, 'BRL': 5.04, 'ZAR': 18.16
}

SYMBOLS = {
    'USD': '$', 'EUR': '€', 'GBP': '£', 'JPY': '¥', 'CAD': 'C$',
    'AUD': 'A$', 'CNY': '¥', 'INR': '₹', 'BRL': 'R$', 'ZAR': 'R'
}

def convert_currency():
    try:
        amt = float(amount_var.get())
        from_cur = from_var.get()
        to_cur = to_var.get()

        from_rate = RATES[from_cur]
        to_rate = RATES[to_cur]
        result = (amt / from_rate) * to_rate
        rate = to_rate / from_rate
        symbol = SYMBOLS.get(to_cur, '')

        result_text = f"{amt} {from_cur} = {symbol}{result:.2f} {to_cur}\n"
        result_text += f"Exchange Rate: 1 {from_cur} = {rate:.4f} {to_cur}"
        result_var.set(result_text)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def swap_currency():
    from_cur = from_var.get()
    to_cur = to_var.get()
    from_var.set(to_cur)
    to_var.set(from_cur)

root = tk.Tk()
root.title("Currency Converter")
root.geometry("450x450")
root.config(bg="#f5f7fa", padx=20, pady=20)

amount_var = tk.StringVar()
from_var = tk.StringVar(value="USD")
to_var = tk.StringVar(value="INR")
result_var = tk.StringVar()

tk.Label(root, text="Currency Converter", font=("Arial", 18, "bold"),
         bg="#f5f7fa", fg="#1c2c5b").pack(pady=10)

tk.Label(root, text="Amount", font=("Arial", 12, "bold"), bg="#f5f7fa").pack()
tk.Entry(root, textvariable=amount_var, font=("Arial", 12), justify="center").pack(pady=5)

dropdown_frame = tk.Frame(root, bg="#f5f7fa")
dropdown_frame.pack(pady=10)

ttk.Label(dropdown_frame, text="From").grid(row=0, column=0, padx=5)
from_menu = ttk.Combobox(dropdown_frame, textvariable=from_var, values=list(RATES), state="readonly")
from_menu.grid(row=1, column=0, padx=5)

ttk.Button(dropdown_frame, text="⇆", command=swap_currency).grid(row=1, column=1, padx=5)

ttk.Label(dropdown_frame, text="To").grid(row=0, column=2, padx=5)
to_menu = ttk.Combobox(dropdown_frame, textvariable=to_var, values=list(RATES), state="readonly")
to_menu.grid(row=1, column=2, padx=5)

tk.Button(root, text="Convert", font=("Arial", 12),
          bg="#007AFF", fg="white", command=convert_currency,
          relief="flat", padx=10, pady=5).pack(pady=15)

tk.Label(root, textvariable=result_var, font=("Arial", 14),
         bg="#f5f7fa", fg="#1c2c5b", wraplength=380).pack(pady=10)

root.mainloop()