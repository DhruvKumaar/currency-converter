# Project 1: Currency Converter App

## Overview

This Currency Converter is a desktop application built using Python’s Tkinter library. It allows users to convert an entered amount from one currency to another based on predefined exchange rates. The user interface is simple, interactive, and beginner-friendly.

## Features

- Converts between 10 major world currencies.
- Uses static exchange rates stored in a dictionary.
- Intuitive dropdowns for selecting ‘From’ and ‘To’ currencies.
- Swap button to reverse selected currencies.
- Displays formatted result with currency symbol and exchange rate.
- Error handling for invalid numeric input.
- User-friendly and visually clean layout.

## Technologies Used

- **Python**: Core language for logic.
- **Tkinter**: GUI library for building the interface.
- **ttk** (Themed Tkinter Widgets): For enhanced dropdowns and buttons.
- **messagebox**: For popup error alerts.

## How to Run

1. Ensure Python is installed (preferably Python 3.6 or later).
2. Copy the script into a file, e.g.,
   ```bash
   currency_converter.py
   ```
3. Run the script using:

```bash 
python currency_converter.py
```

## Supported Currencies

- USD (US Dollar)
- EUR (Euro)
- GBP (British Pound)
- JPY (Japanese Yen)
- CAD (Canadian Dollar)
- AUD (Australian Dollar)
- CNY (Chinese Yuan)
- INR (Indian Rupee)
- BRL (Brazilian Real)
- ZAR (South African Rand)

## Note

These rates are hardcoded and not fetched live. They can be updated manually in the RATES dictionary.
