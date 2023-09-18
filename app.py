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

# Allow user to select a location
selected_location = st.selectbox('Select a location:', [f'Entry {i+1}' for i in range(num_entries)])

# Get the index of the selected location
location_index = int(selected_location.split()[1]) - 1

# Plot a bar chart for population comparison for the selected location
fig, ax = plt.subplots(figsize=(12, 6))
width = 0.4

ax.bar(np.arange(2) - width/2, data['Population'][0][location_index], width, label='Hindu', color='orange')
ax.bar(np.arange(2) + width/2, data['Population'][1][location_index], width, label='Muslim', color='#aaffaa')

ax.set_xlabel('Religion', fontsize=12)
ax.set_ylabel('Population', fontsize=12)
ax.set_title(f'Population Comparison for {selected_location}', fontsize=14)
ax.set_xticks(np.arange(2))
ax.set_xticklabels(['Hindu', 'Muslim'])

ax.legend()
ax.grid(True)

plt.tight_layout()

# Display the plot using Streamlit
st.pyplot(fig)
