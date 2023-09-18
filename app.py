import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data for Hindu and Muslim populations
def generate_sample_data(num_entries):
    data = {
        'Religion': ['Hindu', 'Muslim'],
        'Population': np.random.randint(100, 10000, size=(2, num_entries)).tolist()
    }
    return pd.DataFrame(data)

st.title('Comparison of Hindu and Muslim Populations in Bihar')

# Generate sample data
num_entries = 50
data = generate_sample_data(num_entries)

# Plot a bar chart for population comparison
fig, ax = plt.subplots(figsize=(12, 6))  # Adjust the figure size
x = np.arange(num_entries)
width = 0.4  # Adjust the bar width

ax.bar(x - width/2, data['Population'][0], width, label='Hindu',color="orange")
ax.bar(x + width/2, data['Population'][1], width, label='Muslim',color="#aaffaa")

ax.set_xlabel('Entry', fontsize=12)
ax.set_ylabel('Population', fontsize=12)
ax.set_title('Population Comparison', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels([f'Entry {i+1}' for i in range(num_entries)], rotation=45, ha='right')

# Add legend and grid
ax.legend()
ax.grid(True)

plt.tight_layout()  # Adjust layout

# Display the plot using Streamlit
st.pyplot(fig)
