# Import the modules
import subprocess
import sys
import importlib

# Define a list of libraries to install
libraries = ["yfinance", "kivy-garden","kivy", "kivy-garden.graph","matplotlib", "prophet","buildozer"]

# Loop through each library in the list
for library in libraries:
    # Try to import the library
    try:
        importlib.import_module(library)
        print(f"{library} is already installed.")
    # If the import fails, install the library using pip
    except ImportError:
        print(f"{library} is not installed. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", library])

import yfinance as yf
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import yfinance as yf
import matplotlib.pyplot as plt
from prophet import Prophet
from kivy.metrics import dp

class StockApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        # create a box layout for the app
        layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))

        # create a grid layout for the labels and entry fields
        grid = GridLayout(cols=2, spacing=dp(10), size_hint=(1, 0.3))

        # create labels and entry fields for stock data
        symbol_label = Label(text="Stock Symbol:")
        self.symbol_entry = TextInput(text='AAPL', size_hint_x=0.7)
        start_date_label = Label(text="Start Date (YYYY-MM-DD):")
        self.start_date_entry = TextInput(text='2020-01-01', size_hint_x=0.7)
        end_date_label = Label(text="End Date (YYYY-MM-DD):")
        self.end_date_entry = TextInput(text='2023-01-01', size_hint_x=0.7)

        # add the labels and entry fields to the grid layout
        grid.add_widget(symbol_label)
        grid.add_widget(self.symbol_entry)
        grid.add_widget(start_date_label)
        grid.add_widget(self.start_date_entry)
        grid.add_widget(end_date_label)
        grid.add_widget(self.end_date_entry)

        # add the grid layout to the main layout
        layout.add_widget(grid)

        # create plot button
        plot_button = Button(text="Plot", size_hint=(1, 0.1))
        plot_button.bind(on_press=self.plot_stock_data)
        layout.add_widget(plot_button)

        # add the figure canvas to the layout
        self.figure_canvas = FigureCanvasKivyAgg(plt.gcf())
        layout.add_widget(self.figure_canvas)

        return layout

    def plot_stock_data(self, instance):
        symbol = self.symbol_entry.text
        start_date = self.start_date_entry.text
        end_date = self.end_date_entry.text

        # download stock data from Yahoo Finance
        data = yf.download(symbol, start=start_date, end=end_date, interval='1wk')['Adj Close'].fillna(method='ffill')

        # make predictions using Prophet library
        df = data.reset_index()
        df = df.rename(columns={'Date': 'ds', 'Adj Close': 'y'})
        model = Prophet()
        model.fit(df)
        future = model.make_future_dataframe(periods=52, freq='w')
        forecast = model.predict(future)

        # clear any previous plots
        plt.clf()

        # plot the stock data and forecast
        plt.plot(data.index, data.values)
        plt.plot(forecast['ds'], forecast['yhat'], 'r-', label='Predicted')
        plt.xlabel("Date")
        plt.ylabel("Adjusted Close Price")
        plt.title(f"{symbol} Stock Data from {start_date} to {end_date}")
        plt.legend()
        plt.tight_layout()

        # update the figure canvas
        self.figure_canvas.draw()

if __name__ == "__main__":
    StockApp().run()
