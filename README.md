# Sleep Health & Lifestyle Data Analysis


---> Project Overview:
This project explores the relationship between various lifestyle factors and sleep health using a dataset of personal health and lifestyle metrics. It focuses on visualizing patterns, correlations, and distributions for attributes such as age, occupation, physical activity, stress, heart rate, and sleep quality.
The goal is to provide insights into how lifestyle choices impact sleep duration, quality, and overall wellness.


---> Dataset:
Source: Sleep_health_and_lifestyle_dataset.csv (downloaded from Kaggle)


---> Key Features:
Age / Occupation / Sleep Duration / Quality of Sleep / Physical Activity Level / BMI Category / Blood Pressure / Heart Rate / Daily Steps / Stress Level


---> Data Preprocessing:
Missing values handled by replacing them with column means (e.g., Heart Rate).
Dataset read using pandas for structured analysis.
Correlation matrix computed to identify relationships between features.


---> Visualizations:
1. Bar Plots
   Used to compare individual features:
     Age vs Sleep Duration
     Age vs Quality of Sleep
     Age vs Physical Activity Level
     Age vs BMI Category
     Age vs Blood Pressure
     Age vs Heart Rate
     Age vs Daily Steps
     Occupation vs Sleep Duration & Quality of Sleep
     Physical Activity Level vs Quality of Sleep & Stress Level
2. Violin Plots
   Show distribution and density of features across age groups, occupation, and physical activity levels.
3. Line Plots
   Track trends for Age, Occupation, Physical Activity Level with Sleep Duration, Quality, and Stress Levels.
4. Scatter Plots
   Explore correlations between key health indicators such as Age, Daily Steps, Heart Rate, Sleep Duration, Quality of Sleep, and Stress Level.
5. Box Plots
   Highlight outliers and distributions for key features.
6. Heatmap
   Correlation heatmap to identify relationships between numerical variables.
7. 3D Visualizations
   3D Scatter Plot: Multi-dimensional comparison of features like Sleep Duration, Quality of Sleep, and Stress Level.
   3D Surface (trisurf) & Line Plot: Visual representation of trends in three dimensions.
   3D Bar Plot: Three-dimensional bar charts for Age, Daily Steps, Heart Rate, Sleep, and Stress Level.


---> Statistical Analysis:
1. Measures calculated for key variables:
   Mean / Median / Mode / Variance / Standard Deviation
2. Distributions studied using:
   Bernoulli / Binomial / Poisson / Uniform / Normal / Exponential

   
---> Tools & Libraries:
1. Python 3
2. pandas for data manipulation
3. numpy for numerical calculations
4. matplotlib & seaborn for visualization
5. scipy.stats for statistical distributions
6. mpl_toolkits.mplot3d for 3D visualizations


---> Insights:
Correlations between lifestyle factors and sleep patterns can be identified.
Visualizations highlight trends and anomalies.
3D plots provide multi-dimensional perspectives on relationships between physical activity, heart rate, sleep quality, and stress levels.


---> Usage:
Clone the repository.
Place the dataset Sleep_health_and_lifestyle_dataset.csv in the working directory.
Run the Jupyter Notebook or Python script to reproduce visualizations and statistical analysis.


---> Future work:
Add ML prediction (regression / classification)
Perform time-series analysis 
Deploy visual dashboard using Streamlit



