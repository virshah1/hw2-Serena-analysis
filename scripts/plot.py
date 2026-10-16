import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load cleaned data
df = pd.read_csv("data/serena.csv")

# Set colors based on match outcome
colors = {
    "Win": "blue",
    "Loss": "purple"
}

# Create scatterplot
fig, ax = plt.subplots(figsize=(10, 6))

for result in ["Win", "Loss"]:
    subset = df[df["result"] == result]

    ax.scatter(
        subset["serena_age"],
        subset["age_difference"],
        color=colors[result],
        label=result,
        alpha=0.5,
        s=18
    )

# Labels and title
ax.set_title(
    "Serena Williams' Tennis Matches, Age 14 to 40"
)

ax.set_xlabel("Serena Williams' Age")
ax.set_ylabel("Serena's Age - Opponent's Age")

# White background and faint grid
ax.set_facecolor("white")
fig.patch.set_facecolor("white")
ax.grid(alpha=0.2)

# Add legend
ax.legend(title="Match Result")

# Add caption
fig.text(
    0.5, 0.01,
    "Source: Tennis Abstract. Each point represents one match.",
    ha="center",
    fontsize=9
)

# Save plot
Path("outputs").mkdir(exist_ok=True)

plt.savefig(
    "outputs/serena_plot.png",
    dpi=300,
    bbox_inches="tight"
)

print("Plot created successfully!")
