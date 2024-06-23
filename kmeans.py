import numpy as np
import random

# 随机初始化质心
def initialize_centroids(points, k):
    indices = random.sample(range(len(points)), k)
    centroids = points[indices]
    return centroids

# 分配数据点到最近的质心
def assign_clusters(points, centroids):
    clusters = np.zeros(len(points))
    for i, point in enumerate(points):
        distances = np.linalg.norm(centroids - point, axis=1)
        clusters[i] = np.argmin(distances)
    return clusters

# 更新质心
def update_centroids(points, clusters, k, counts):
    new_centroids = np.zeros((k, points.shape[1]))
    for i in range(k):
        cluster_points = points[clusters == i]
        if len(cluster_points) > 0:
            new_centroid = np.average(cluster_points, axis=0, weights=counts[clusters == i])
        else:
            new_centroid = random.choice(points)
        new_centroids[i] = new_centroid
    return new_centroids

# K-means 聚类
def kmeans(points, k, counts, max_iters=100, tol=1e-2):
    centroids = initialize_centroids(points, k)
    for _ in range(max_iters):
        clusters = assign_clusters(points, centroids)
        new_centroids = update_centroids(points, clusters, k, counts)
        if np.linalg.norm(new_centroids - centroids) < tol:
            break
        centroids = new_centroids
    return centroids, clusters

