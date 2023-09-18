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

# Display the data
st.write('Population Data:')
st.write(data)

# Plot a bar chart for population comparison
st.write('### Population Comparison')
fig, ax = plt.subplots()
x = np.arange(num_entries)
width = 0.35
ax.bar(x, data['Population'][0], width, label='Hindu')
ax.bar(x + width, data['Population'][1], width, label='Muslim')
ax.set_xlabel('Entry')
ax.set_ylabel('Population')
ax.set_title('Population Comparison')
ax.set_xticks(x + width / 2)
ax.set_xticklabels([f'Entry {i+1}' for i in range(num_entries)])
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)
