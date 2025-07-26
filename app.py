import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

st.set_page_config(page_title="🗺️ Metro Route Density Monitoring", layout="wide")
st.title("🚇 Delhi Metro Route Density Monitoring System")

st.markdown("""
Upload your GTFS `.txt` files to visualize metro routes, stop density, and trip activity.
""")

# File Upload
agency = st.file_uploader("C:\\Users\\Sanskar Gupta\\OneDrive\\Desktop\\ML Projects\\Metro Route Density Analyzer\\agency.txt", type="txt")
calendar = st.file_uploader("C:\\Users\\Sanskar Gupta\\OneDrive\\Desktop\\ML Projects\\Metro Route Density Analyzer\\calendar.txt", type="txt")
routes = st.file_uploader("C:\\Users\\Sanskar Gupta\\OneDrive\\Desktop\\ML Projects\\Metro Route Density Analyzer\\routes.txt", type="txt")
shapes = st.file_uploader("C:\\Users\\Sanskar Gupta\\OneDrive\\Desktop\\ML Projects\\Metro Route Density Analyzer\\shapes.txt", type="txt")
stop_times = st.file_uploader("C:\\Users\\Sanskar Gupta\\OneDrive\\Desktop\\ML Projects\\Metro Route Density Analyzer\\stop_times.txt", type="txt")
stops = st.file_uploader("C:\\Users\\Sanskar Gupta\\OneDrive\\Desktop\\ML Projects\\Metro Route Density Analyzer\\stops.txt", type="txt")
trips = st.file_uploader("C:\\Users\\Sanskar Gupta\\OneDrive\\Desktop\\ML Projects\\Metro Route Density Analyzer\\trips.txt", type="txt")

if all([agency, calendar, routes, shapes, stop_times, stops, trips]):
    # Load all files
    agency = pd.read_csv(agency)
    calendar = pd.read_csv(calendar)
    routes = pd.read_csv(routes)
    shapes = pd.read_csv(shapes)
    stop_times = pd.read_csv(stop_times)
    stops = pd.read_csv(stops)
    trips = pd.read_csv(trips)

    st.subheader("🧭 Geographical Paths of Metro Routes")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='shape_pt_lon', y='shape_pt_lat', hue='shape_id', data=shapes,
                    palette='viridis', s=10, legend=False, ax=ax1)
    ax1.set_title('Geographical Paths of Delhi Metro Routes')
    ax1.set_xlabel('Longitude')
    ax1.set_ylabel('Latitude')
    ax1.grid(True)
    st.pyplot(fig1)

    st.subheader("📅 Number of Trips Per Day of the Week")
    trips_calendar = pd.merge(trips, calendar, on='service_id', how='left')
    trip_counts = trips_calendar[['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']].sum()

    fig2, ax2 = plt.subplots()
    trip_counts.plot(kind='bar', color='skyblue', ax=ax2)
    ax2.set_title("Number of Trips per Day")
    ax2.set_xlabel("Day")
    ax2.set_ylabel("Number of Trips")
    ax2.grid(True)
    st.pyplot(fig2)

    st.subheader("📍 Geographical Distribution of Metro Stops")
    fig3, ax3 = plt.subplots(figsize=(10, 8))
    sns.scatterplot(x='stop_lon', y='stop_lat', data=stops, color='red', s=50, ax=ax3)
    ax3.set_title("Geographical Location of Stops")
    ax3.set_xlabel("Longitude")
    ax3.set_ylabel("Latitude")
    ax3.grid(True)
    st.pyplot(fig3)

    st.subheader("🔁 Number of Routes per Stop")
    stops_with_routes = pd.merge(pd.merge(stop_times, trips, on='trip_id'), routes, on='route_id')
    stop_route_counts = stops_with_routes.groupby('stop_id')['route_id'].nunique().reset_index()
    stop_route_counts = stop_route_counts.rename(columns={'route_id': 'number_of_routes'})
    stop_route_counts = pd.merge(stop_route_counts, stops, on='stop_id')

    fig4, ax4 = plt.subplots(figsize=(10, 10))
    sns.scatterplot(x='stop_lon', y='stop_lat', size='number_of_routes', hue='number_of_routes',
                    sizes=(50, 500), palette='coolwarm', alpha=0.6, data=stop_route_counts, ax=ax4)
    ax4.set_title("Routes Passing Through Each Stop")
    ax4.set_xlabel("Longitude")
    ax4.set_ylabel("Latitude")
    ax4.grid(True)
    st.pyplot(fig4)

else:
    st.info("Please upload all required GTFS text files to visualize the data.")
