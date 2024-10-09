# -*- coding: utf-8 -*-
"""CustomerSegmentationusingKMeansClustering.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/epicskills1/PRODIGY_ML_02/blob/main/CustomerSegmentationusingKMeansClustering.ipynb
"""

# Google Colab implementation

# Import necessary libraries
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('/content/Mall_Customers.csv')

# Display the first few rows of the dataset
print(df.head())

# Data preprocessing
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Elbow Method to find the optimal number of clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plot the results of the Elbow Method
plt.figure(figsize=(10, 5))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Fit K-means to the dataset with the optimal number of clusters
optimal_clusters = 5
kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(X)

# Add the cluster column to the original dataframe
df['Cluster'] = y_kmeans

# Visualize the clusters
plt.figure(figsize=(10, 5))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', data=df, palette='viridis')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()

# Install required packages
!pip install streamlit pyngrok

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import pandas as pd
# from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt
# import seaborn as sns
# 
# # Title of the Streamlit app
# st.title("Customer Segmentation using K-means Clustering")
# 
# # Load the dataset
# df = pd.read_csv('/content/Mall_Customers.csv')
# 
# # Data preprocessing
# X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
# 
# # Elbow Method to find the optimal number of clusters
# wcss = []
# for i in range(1, 11):
#     kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
#     kmeans.fit(X)
#     wcss.append(kmeans.inertia_)
# 
# # Plot the Elbow Method
# plt.figure(figsize=(10, 5))
# plt.plot(range(1, 11), wcss, marker='o')
# plt.title('Elbow Method')
# plt.xlabel('Number of clusters')
# plt.ylabel('WCSS')
# st.pyplot(plt)
# 
# # Fit K-means to the dataset with the optimal number of clusters
# optimal_clusters = 5
# kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
# y_kmeans = kmeans.fit_predict(X)
# 
# # Add the cluster column to the original dataframe
# df['Cluster'] = y_kmeans
# 
# # Visualize the clusters
# plt.figure(figsize=(10, 5))
# sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', data=df, palette='viridis')
# plt.title('Clusters of customers')
# plt.xlabel('Annual Income (k$)')
# plt.ylabel('Spending Score (1-100)')
# plt.legend()
# st.pyplot(plt)
# 
#

!pip install --upgrade pyngrok

from pyngrok import ngrok
ngrok.set_auth_token("2N13huDP2ANtbXSJQ7OQ2HvAShU_2pEtgBSQ4CM4B6mY6kTEF") # Removed extra space before this line

# Terminate all existing ngrok tunnels
ngrok.kill()

# Create a new ngrok tunnel, explicitly specifying HTTP protocol
public_url = ngrok.connect(8501, proto="http") # Specify protocol as "http"
print(f"Streamlit App URL: {public_url}")

import subprocess

# Run Streamlit app
subprocess.Popen(['streamlit', 'run', 'app.py'])