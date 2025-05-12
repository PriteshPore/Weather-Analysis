import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("Weather Data Analysis App")
    st.sidebar.title("Upload your Weather Dataset")

    # File uploader
    uploaded_file = st.sidebar.file_uploader("Upload your csv File",type=['csv'])

    if uploaded_file is not None:
        try:
            # Load the data
            data = pd.read_csv(uploaded_file)
            st.sidebar.success("File uploaded successfully!")
            st.subheader("Data overview")
            st.dataframe(data.head())

            # Basic dataset information
            st.subheader("Basic Information")
            st.write("**Shape of the dataset**",data.shape)
            st.write("**Columns in the dataset**",data.columns)
            st.write("**Missing values**",data.isnull().sum())


            # Summary statistics
            st.subheader("Summary Statistics")
            st.write(data.describe())

            # Visualisation
            st.subheader("Visualisation")
            if 'temperature_celsius' in data.columns:
                st.write("**Temperature Distribution**")
                fig,ax = plt.subplots()
                sns.histplot(data['temperature_celsius'],kde=True,bins=20,color='skyblue',ax=ax)
                ax.set_title("Temperature Distribution (°C)")
                ax.set_xlabel("Temperature (°C)")
                ax.set_ylabel("Frequency")
                st.pyplot(fig)

            if 'air_quality_PM2.5' in data.columns:
                st.write("**Air quality (PM2.5) distribution**")
                fig,ax = plt.subplots()
                sns.histplot(data['air_quality_PM2.5'],kde = True,bins=20,color='lightgreen',ax=ax)
                ax.set_title("Air quality (PM2.5) distribution")
                ax.set_xlabel("PM2.5 Levels")
                ax.set_ylabel("Frequency")
                st.pyplot(fig)
            
            if 'sunrise' in data.columns and 'sunset' in data.columns:
            

                st.write("**Sunrise and Sunset Time Distribution")
                fig,ax = plt.subplots()
                sns.histplot(data['sunrise'],kde = True,bins=12,color='gold',ax = ax)
                sns.histplot(data['sunset'],kde = True,bins=12,color='orange',ax=ax)
                ax.set_title("Sunrise and Sunset Time Distribution")
                ax.set_xlabel("Time")
                ax.set_ylabel("Frequency")
                ax.legend()
                st.pyplot(fig)

        except Exception as e:
            st.error(f"Error while loading the file {e}")
    else:
        print("Please upload the file to get started!!")

if __name__ == "__main__":
    main()

