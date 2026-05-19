import pandas as pd
import numpy as np

# Loads data/transformed/events.csv
events = pd.read_csv("data/transformed/events.csv")
events["duration_minutes"] = events["duration_seconds"]/60
events["weekday"] = events["timestamp"].apply(lambda x: pd.Timestamp(x)).dt.day_name()
events.to_csv("data/features/events.csv", index = False) # Save cleaned events.csv to data/transformed/events.csv 