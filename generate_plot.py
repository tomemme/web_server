import pandas as pd
import plotly.express as px

# Example data, replace with actual data collection
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Bitcoin Power Consumption (TWh)': [60, 70, 80, 90, 100],
    'AI/ML Training Power Consumption (TWh)': [5, 10, 20, 30, 40]
}
df = pd.DataFrame(data)

# Create plot
fig = px.line(df, x='Year', y=['Bitcoin Power Consumption (TWh)', 'AI/ML Training Power Consumption (TWh)'],
              labels={'value': 'Power Consumption (TWh)', 'variable': 'Category'})

# Save plot to HTML
fig.write_html('plot.html')
