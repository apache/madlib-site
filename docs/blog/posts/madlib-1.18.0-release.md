---
date: 2021-04-05
categories:
  - Release
authors:
  - madlib-team
---

# MADlib 1.18.0 Release

On April 5, 2021, MADlib completed its eighth release as an Apache Software Foundation Top Level Project.

<!-- more -->

## New Features

### Deep Learning Enhancements
- **New grid and random search methods**: Advanced hyperparameter optimization techniques for neural networks
- **AutoML methods Hyperband and Hyperopt**: Automated machine learning capabilities for efficient model selection and hyperparameter tuning
- **Custom loss functions and custom metrics**: Flexibility to define domain-specific loss functions and evaluation metrics
- **TensorBoard support**: Integration with TensorBoard for visualization and monitoring of training progress
- **Multi-input and output support for fit and evaluate**: Enhanced neural network architecture support for complex models

### Clustering Algorithms
- **DBSCAN - Density based clustering (phase 1)**: Initial implementation of DBSCAN algorithm for density-based clustering

## Improvements

### Deep Learning Performance
- **Implement cache logic to speed performance**: Intelligent caching mechanisms to reduce computation overhead
- **Reduce GPU idle time when moving model state between workers**: Optimized GPU utilization in distributed training scenarios
- **Use Keras version from TensorFlow**: Streamlined dependency management by using TensorFlow's built-in Keras
- **Add top n to evaluate**: Enhanced model evaluation with top-n accuracy metrics

### Graph Algorithm Enhancements
- **Support BIGINT for all graph methods**: Extended data type support for large-scale graph processing

### Infrastructure Improvements
- **Switch to CloudBees (was Jenkins)**: Upgraded continuous integration infrastructure for better reliability and performance

## Download and Installation

You are invited to [download the 1.18.0 release](https://dist.apache.org/repos/dist/release/madlib/1.18.0/) and [review the release notes](https://github.com/apache/madlib/blob/master/RELEASE_NOTES). 

Also please refer to the [list of supported databases and OS](https://cwiki.apache.org/confluence/display/MADLIB/Database+and+OS+Support) for compatibility information.

## What's New

This release represents a major advancement in MADlib's deep learning capabilities, introducing AutoML features that make machine learning more accessible to users without extensive hyperparameter tuning expertise. The TensorBoard integration provides powerful visualization capabilities for monitoring and debugging neural network training.

The performance improvements, particularly in GPU utilization and caching, make MADlib more suitable for production deep learning workloads at scale.

For more details about the new deep learning features, please refer to the [Apache MADlib deep learning notes](https://cwiki.apache.org/confluence/display/MADLIB/Deep+Learning) and the [Jupyter notebook examples](https://github.com/apache/madlib-site/tree/asf-site/community-artifacts/Deep-learning).

For technical support and questions, please visit our [community forums](../../community/index.md) or check the [documentation](../../documentation/user-guide.md).