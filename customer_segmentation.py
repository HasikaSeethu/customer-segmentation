import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('customer_data.csv')

# Select features
X = df[['AnnualIncome', 'SpendingScore']]

# K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Save clustered data
df.to_csv('customer_segments.csv', index=False)

# Plot clusters
plt.figure(figsize=(6, 4))
plt.scatter(X['AnnualIncome'], X['SpendingScore'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.title('Customer Segments')
plt.savefig('cluster_plot.png')
plt.show()
