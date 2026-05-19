import pandas as pd
import numpy as np

# Loads data/raw/events.csv
events = pd.read_csv("data/raw/events.csv")
events = events[events.isnull().any(axis=1)==False] # Drop any rows with null
invalid_types = ["unknown"]
events = events[events["event_type"].isin(invalid_types) == False] # Drop invalid event types
events["timestamp"] = events["timestamp"].apply(lambda x: pd.Timestamp(x).isoformat()) # Normalize timestamp to ISO 8601
events.to_csv("data/clean/events.csv") # Save cleaned events.csv to data/clean/events.csv