---
date: 2022-03-08
categories:
  - Release
authors:
  - madlib-team
---

# MADlib 1.19.0 Release

On March 8, 2022, MADlib completed its ninth release as an Apache Software Foundation Top Level Project.

<!-- more -->

## New Features

### Clustering Algorithms
- **DBSCAN: Fast parallel-optimized DBSCAN**: Introduction of Density-Based Spatial Clustering of Applications with Noise (DBSCAN) algorithm with parallel optimization for large-scale clustering tasks

### Neural Network Enhancements
- **MLP: Add rmsprop and Adam optimization techniques**: Enhanced Multi-Layer Perceptron (MLP) with additional optimization algorithms for better convergence and performance

## Improvements

### Graph Algorithm Optimizations
- **Improve WCC subtx count and catalog entry frequency**: Performance improvements for Weakly Connected Components algorithm, reducing transaction overhead and catalog access frequency

### Neural Network Improvements
- **MLP: Set lambda value for minibatch**: Better regularization control for mini-batch training in neural networks

### Algorithm Stability
- **GLM-multinom: Use non-temp tables in GroupIterationController**: Improved stability for multinomial GLM by using persistent tables instead of temporary ones

### Infrastructure
- **Jenkins: Add new dockerfile for PG11**: Enhanced continuous integration with PostgreSQL 11 support
- **Build: Use dynamic_library_path for module pathname**: Improved library loading mechanism for better portability

## Download and Installation

You are invited to [download the 1.19.0 release](https://dist.apache.org/repos/dist/release/madlib/1.19.0/) and [review the release notes](https://github.com/apache/madlib/blob/master/RELEASE_NOTES). 

Also please refer to the [list of supported databases and OS](https://cwiki.apache.org/confluence/display/MADLIB/Database+and+OS+Support) for compatibility information.

## What's New

This release introduces DBSCAN, a powerful clustering algorithm that can find clusters of arbitrary shape and is robust to outliers. The parallel-optimized implementation makes it suitable for large-scale data analysis tasks.

The neural network improvements provide more optimization options and better performance for deep learning workloads, while the various performance optimizations ensure better scalability across all algorithms.

For technical support and questions, please visit our [community forums](../../community/index.md) or check the [documentation](../../documentation/user-guide.md).