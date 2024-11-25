import plotly.express as px
import pandas as pd

# Data for top Super Bowl ad spenders, spending, and number of ads from fox business (https://www.foxbusiness.com/media/biggest-super-bowl-ad-spenders)
data = {
    "Brand": ["Budweiser", "Pepsi", "Coca-Cola", "McDonald's", "Ford", "Toyota", 
                "Dodge", "Honda", "FedEx", "Miller"],
    "Spending": [449.5, 289.5, 202.0, 108.9, 109.8, 146.0, 85.2, 82.9, 66.2, 38.9],
    "Ads": [135, 92, 51, 54, 52, 41, 39, 30, 31, 30]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create the bubble chart using Plotly
fig = px.scatter(df, x="Ads", y="Spending", size="Spending", color="Brand", 
                 hover_name="Brand", size_max=100, 
                 title="All Time Super Bowl Ad Spending  and Number of Ads")

fig.update_layout(
    xaxis_title="Number of Ads",
    yaxis_title="Spending in millions"
)

# Show the plot
fig.show()
