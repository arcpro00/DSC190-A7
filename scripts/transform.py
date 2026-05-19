import pandas as pd
import numpy as np

# Loads data/clean/events.csv
events = pd.read_csv("data/clean/events.csv")
events["date"] = events["timestamp"].apply(lambda x: pd.Timestamp(x)).dt.date
events.to_csv("data/transformed/events.csv", index=False) # Save cleaned events.csv to data/transformed/events.csv