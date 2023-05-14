# Stock Forecast App
 # Introduction
  This is a simple Kivy app that uses the yfinance and Prophet libraries to download stock data from Yahoo Finance, make predictions using the Prophet library, and plot the results.

# Requirements
 Python 3.6 or later <br/>
 Kivy framework<br/>
 yfinance library<br/>
 kivy-garden library<br/>
 kivy-garden.graph library<br/>
 matplotlib library<br/>
 prophet library<br/>
 buildozer library (optional)<br/>
# Installation
 1. Clone or download the repository.
 2. Install the required libraries by running the following command: pip install -r requirements.txt
 3. If you want to build an Android package, install buildozer by running the following command: pip install buildozer
# Usage
  To run the app, navigate to the root directory of the repository and run the following command:
  python main.py
  
  The app will open and prompt you to enter the stock symbol, start date, and end date. After entering the necessary information, click the "Plot" button to see the graph of the predicted stock prices.

# Build for Android
 # If you want to build an Android package, run the following command:
 # <code>buildozer android debug deploy run</code>
 This will generate an APK file that you can install on your Android device. Note that this command may take some time to run, especially if it's your first time building the package.

# Run the app
 To run the app and install required libraries, simply run the python script. This will launch the Kivy app after downloading the required libraries.

# Enter stock data
 Enter the stock symbol, start date, and end date in the input fields provided.

# Plot data
 Click on the "Plot" button to plot the stock data.

# About the app
 This app is built using the Kivy framework for Python. It allows the user to enter stock symbol, start date and end date, and plots the adjusted close price for the entered stock data. The app uses the yfinance library to download stock data from Yahoo Finance and the Prophet library to make predictions using the downloaded stock data. The matplotlib library is used to plot the data.

# Contributing
 Contributions are welcome. If you find any issues or have any suggestions for improvements, please feel free to create a pull request or open an issue.

# License
This app is licensed under the MIT License. See LICENSE file for details.

# Author
This app was created by Abhishek Kanther.

# Support
If you encounter any issues while using this script, please feel free to open an issue on the GitHub repository. We'll do our best to respond as quickly as possible and provide any necessary support.
