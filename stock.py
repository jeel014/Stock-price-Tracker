import yfinance as yf
import tkinter as tk
from tkinter import messagebox

def fetch_stock_price():
    stock_name = stock_entry.get().strip().upper()  # Get the stock name entered by the user
    if not stock_name:
        messagebox.showwarning("Warning", "Please enter a stock symbol.")
        return
    
    try:
        stock = yf.Ticker(stock_name)
        if stock.history(period='1d').empty:
            raise ValueError("No data found, symbol may be delisted.")
        
        current_price = stock.history(period='1d')['Close'].iloc[-1]  # Get the latest closing price
        price_in_rupees = "₹ {:.2f}".format(current_price)  # Format price with Rupee symbol
        price_label.config(text=f"Current Price: {price_in_rupees}")
    except ValueError as ve:    
        messagebox.showwarning("Warning", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch stock price: {e}")

# Create the main GUI window
root = tk.Tk()
root.title("Stock Price Lookup")

# Create a label and an entry widget for the stock name
tk.Label(root, text="Enter Stock Symbol:").pack(pady=10)
stock_entry = tk.Entry(root, font=("Helvetica", 14))
stock_entry.pack(pady=5)

# Create a button to fetch the stock price
fetch_button = tk.Button(root, text="Get Stock Price", command=fetch_stock_price)
fetch_button.pack(pady=10)

# Create a label to display the fetched stock price
price_label = tk.Label(root, text="", font=("Helvetica", 16))
price_label.pack(pady=20)

# Run the main event loop
root.mainloop()
