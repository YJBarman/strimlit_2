# Import necessary libraries
import pandas as pd
import numpy as np
import streamlit as st

# Create a sample dataframe
df = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])

# Add a slider
slider_val = st.slider('Select a range', 0, 10)

# Filter the dataframe
filtered_df = df[df['A'] > slider_val]

# Display the filtered dataframe
st.write(filtered_df)
