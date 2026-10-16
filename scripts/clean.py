import pandas as pd
import json
from pathlib import Path

# Read raw JavaScript data
raw = Path("data/SerenaWilliamsCareer.js").read_text()

# Extract the JavaScript array
start = raw.index("[")
end = raw.rfind("]") + 1

matches = json.loads(raw[start:end])

# Convert into a DataFrame
df = pd.DataFrame(matches)

# Keep relevant columns
df = df[[0, 4, 11, 16]].copy()

df.columns = [
    "match_date",
    "result",
    "opponent",
    "opponent_dob"
]

# Convert dates
df["match_date"] = pd.to_datetime(
    df["match_date"],
    format="%Y%m%d",
    errors="coerce"
)

df["opponent_dob"] = pd.to_datetime(
    df["opponent_dob"],
    format="%Y%m%d",
    errors="coerce"
)

# Serena's date of birth
serena_dob = pd.Timestamp("1981-09-26")

# Calculate ages in years
df["serena_age"] = (
    (df["match_date"] - serena_dob).dt.days / 365.25
)

df["opponent_age"] = (
    (df["match_date"] - df["opponent_dob"]).dt.days / 365.25
)

# Calculate age difference
df["age_difference"] = (
    df["serena_age"] - df["opponent_age"]
)

# Convert match result labels
df["result"] = df["result"].map({
    "W": "Win",
    "L": "Loss"
})

# Remove missing or invalid observations
df = df.dropna(
    subset=["serena_age", "opponent_age",
            "age_difference", "result"]
)

# Save clean dataset
Path("data").mkdir(exist_ok=True)
df.to_csv("data/serena.csv", index=False)

print("Cleaning complete!")
print("Number of matches:", len(df))
print(df.head())


