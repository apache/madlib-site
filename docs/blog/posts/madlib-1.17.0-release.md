---
date: 2020-04-09
categories:
  - Release
authors:
  - madlib-team
---

# MADlib 1.17.0 Release

On April 9, 2020, MADlib completed its seventh release as an Apache Software Foundation Top Level Project.

<!-- more -->

## New Features

### Deep Learning Advancements
- **Model selection framework for Keras with TensorFlow backend**: Comprehensive framework for model architecture search and hyperparameter optimization with GPU acceleration
- **Support for heterogeneous clusters**: Enhanced support for clusters where GPUs are attached to only certain segment hosts, enabling flexible deployment scenarios
- **Support inference for imported models**: "Bring your own model" capability - perform inference on models not trained in MADlib
- **Support transfer learning for multiple model fit function**: Advanced transfer learning capabilities for leveraging pre-trained models
- **Generate model selection table for grid search or random search**: Automated model selection with comprehensive result tracking
- **Helper function to get GPU type and configuration**: Utility functions for GPU discovery and configuration management

### Clustering Enhancements
- **k-Means clustering - Select optimal number of centroids**: Automated cluster number selection using elbow or silhouette methods for optimal clustering results

### Platform Support
- **PostgreSQL 12 support**: Extended compatibility to PostgreSQL 12 for broader deployment options

## Improvements

### Algorithm Enhancements
- **Association rules - Add option to set number of posterior rules**: Enhanced control over association rule mining output
- **Correlation and covariance - Improve memory usage with large number of groups**: Better memory management for statistical computations with many grouping variables

### Deep Learning Performance
- **Improve performance of mini-batch preprocessor and fit functions**: Significant performance improvements for neural network training workflows

### Documentation and Infrastructure
- **Docs - Improve installation guide on wiki**: Enhanced installation documentation for better user experience
- **Graph - SSSP should not show vertices in output table that are unreachable**: Cleaner output for Single Source Shortest Path algorithm
- **LDA - Add stopping criteria on perplexity**: Better convergence control for Latent Dirichlet Allocation

## Download and Installation

You are invited to [download the 1.17.0 release](https://dist.apache.org/repos/dist/release/madlib/1.17.0/) and [review the release notes](https://github.com/apache/madlib/blob/master/RELEASE_NOTES).

For more details about the new deep learning features, please refer to the [Apache MADlib deep learning notes](https://cwiki.apache.org/confluence/display/MADLIB/Deep+Learning) and the [Jupyter notebook examples](https://github.com/apache/madlib-site/tree/asf-site/community-artifacts/Deep-learning).

## What's New

This release marks a significant milestone in MADlib's deep learning capabilities, introducing a comprehensive model selection framework that automates the often complex process of finding optimal neural network architectures and hyperparameters. The support for heterogeneous GPU clusters makes MADlib more flexible for real-world deployment scenarios.

The "bring your own model" feature opens up new possibilities for integrating MADlib with existing machine learning workflows, while the enhanced k-means clustering with automatic cluster selection makes unsupervised learning more accessible.

For technical support and questions, please visit our [community forums](../../community/index.md) or check the [documentation](../../documentation/user-guide.md).