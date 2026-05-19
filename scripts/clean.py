import pandas as pd
import numpy as np
from pathlib import Path

# Loads data/raw/events.csv
events = pd.read_csv("data/raw/events.csv")
events = events[events.isnull().any(axis=1)==False] # Drop any rows with null
valid_types = ['click', 'login', 'purchase', 'scroll', 'view']
events = events[events["event_type"].isin(valid_types) == True] # Drop invalid event types
events = events[events["duration_seconds"]>0] # Drop non-positive duration seconds
events["duration_seconds"] = events["duration_seconds"].apply(lambda x: int(x))
events["timestamp"] = events["timestamp"].apply(lambda x: pd.Timestamp(x)).dt.floor("s").apply(lambda x: x.isoformat()) # Normalize timestamp to ISO 8601
Path("data/clean").mkdir(parents=True, exist_ok=True)
events.to_csv("data/clean/events.csv",index=False) # Save cleaned events.csv to data/clean/events.csv