import numpy as np
import pandas as pd

"""Here we type the UMICS data directly (We are entering the data directly for simplicity.)"""

# The UMICS data
actual = pd.Series([92.0, 91.7, 91.0, 89.0, 94.7, 93.5, 90.0, 89.8, 91.2, 87.2, 93.8, 98.2])

forecast = pd.Series(np.ones(len(actual) + 1))                          # Create the column for the forecast
forecast[0] = float("NaN") # No forecast here

# Run the indented commands repeatedly, with the value of `i` ranging from 1 to `actual.size`
for i in range(1, len(actual)+1):
    forecast[i] = actual[i - 1]                                         # Use the naive method to create the forecast

df = pd.DataFrame(data = {"Actual": actual, "Forecast": forecast})      # Create a DataFrame (like a spreadsheet)
# Print the DataFrame
print(df)

error = df["Actual"] - df["Forecast"]                                   # The error column
absError = abs(error)                                                   # The absolute error column
absPctError = absError/df["Actual"] * 100                               # The absolute percentage error column
mape = absPctError.mean()                                               # Find the mean absolute percentage error

# Append the error, absolute error, and absolute percentage error columns to the DataFrame `df`
df = pd.DataFrame(data = {**df, "Error": error, "Absolute Error": absError, "Absolute % Error": absPctError })
# Print a formatted string (put Python variable names inside of `{}`)
print(f"{df}\n\nMAPE: {mape}")