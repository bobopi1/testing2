import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the web app
st.title('CSV Data to Bar Chart')

# File uploader allows user to add their own CSV
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Display the DataFrame
    st.write(df)
    
    # Ask for columns to plot
    column_to_plot_x = st.selectbox('Select the column for X-axis', df.columns)
    column_to_plot_y = st.selectbox('Select the column for Y-axis', df.columns)
    
    # Plotting the bar chart
    st.write("Bar chart:")
    fig, ax = plt.subplots()
    ax.bar(df[column_to_plot_x], df[column_to_plot_y])
    ax.set_xlabel(column_to_plot_x)
    ax.set_ylabel(column_to_plot_y)
    st.pyplot(fig)

