A Python program using Yahoo Finance to find stock prices and generate a graph for it.

How it works in 5 steps:
    1. The program asks the user for an input as to which stock they would like to view
    2. The program continually asks for more stock names until the user doesn't want to add anymore
    3. The data is collected from yfinance (Yahoo Finance) using the yfinance and pandas libraries
    4. The user is also asked which start date they would like to see the stock price from (if the date is too far back the
       program adjusts the start date to when the earliest company (inputted) was made)
    5. A graph is generated of the stock data using the matplot lib library