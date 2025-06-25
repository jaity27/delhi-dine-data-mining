# Delhi Restaurant Usage Analysis

This project explores restaurant trends and consumer behavior in Delhi by analyzing data scraped from Swiggy. We focus on key metrics such as average pricing, popular dishes, and bestsellers across different zones in Delhi. The dataset was collected using web scraping with Python, and visual analytics were used to uncover regional patterns and trends.

## 📌 Project Overview

Objective: To analyze restaurant-related data in Delhi and identify patterns based on geography and consumer preferences.

Method: Web scraping from Swiggy using Delhi pincodes, classification of regions, and exploratory data analysis.

## 🧰 Technologies Used

Python

BeautifulSoup / Requests / Selenium (for web scraping)

Pandas / NumPy (for data wrangling)

Matplotlib / Seaborn / Plotly (for visualization)

scikit-learn (for clustering and analysis)

## 🗺️ Dataset Creation

Delhi was segmented into North, South, East, West, and Central zones.

Pincodes corresponding to each region were gathered.

For each pincode, restaurants listed on Swiggy were scraped to extract:

Restaurant Name

Cuisine Types

Average Price for Two

Location

Most Popular Items

Bestsellers / Recommended

## 📊 Key Analysis

Average Pricing by Region: Compared median/mean pricing across zones.

Popular Items Heatmap: Identified frequently occurring items per region.

Cuisine Clustering: Grouped restaurants based on cuisine and popularity metrics.

Bestseller Trends: Analyzed overlap and uniqueness of bestseller items across areas.

## 🔍 Outcomes

Found notable differences in pricing and food preferences between zones.

Identified specific cuisines or items with high demand in particular regions.

Clustered regions based on restaurant density, affordability, and popularity.

