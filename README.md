# 🚇 Delhi Metro Route Density Analyzer

A Streamlit-based web application for analyzing and visualizing Delhi Metro operations using GTFS-format datasets. This tool helps address overcrowding and inefficiencies by offering insights into stop density, trip frequency, and route coverage.

---

## 📂 Dataset Overview

This application uses the following GTFS `.txt` files:

- **agency.txt**: Information about the Delhi Metro Rail Corporation (DMRC)
- **calendar.txt**: Weekly service schedules and valid operation dates
- **routes.txt**: Metro route IDs, names, and descriptions
- **shapes.txt**: Geographical path (latitude, longitude) of each route
- **stop_times.txt**: Arrival/departure times for each trip-stop pair
- **stops.txt**: Coordinates and metadata for metro stops
- **trips.txt**: Mapping of trip IDs to routes and service schedules

---

## 🎯 Problem Statement

Overcrowding during peak hours and imbalanced service distribution challenge commuter satisfaction and network efficiency. This app helps:

- Visualize route density and stop load
- Identify days and times with high service demands
- Pinpoint stops requiring frequency optimization

---

## 🛠 Features

- 📍 **Visualize route shapes** with latitude-longitude mapping
- 📅 **Trip frequency by weekday**
- 🚏 **Geospatial view of stop density**
- 🔁 **Route overlap per stop**

---

🖼 Sample Visuals
Line map of metro shapes

Bar chart of trip volume by day

Density map showing route count per stop

---

🔧 Technologies Used
Python 3.13

Streamlit

Pandas

Matplotlib

Seaborn

---
📌 Future Enhancements
Interactive maps (using Plotly/Folium)

Demand prediction using ML

Real-time density monitoring via CCTV
---

## 🚀 Run the App

### 1. Clone this repository

```bash
git clone https://github.com/your-username/metro-density-analyzer.git
cd metro-density-analyzer
