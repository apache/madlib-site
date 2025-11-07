---
date: 2022-08-03
categories:
  - Release
authors:
  - madlib-team
---

# MADlib 1.20.0 Release

On August 3, 2022, MADlib completed its tenth release as an Apache Software Foundation Top Level Project.

<!-- more -->

## New Features

### XGBoost Integration
- **Python based XGBoost with single and grid search executions**: Complete integration of XGBoost algorithm with both single model training and automated hyperparameter grid search capabilities

### Graph Algorithm Enhancements
- **Add multicolumn support for WCC and Pagerank**: Enhanced Weakly Connected Components (WCC) and PageRank algorithms to support composite identifiers, making them more suitable for complex real-world graph data

## Improvements

### Performance Optimizations
- **Reuse update plan in GroupIterationController**: Significant performance improvement for iterative algorithms by reusing query execution plans
- **Adjust ORCA to reduce planning time**: Optimized query planning for Elastic Net, GLM, and SVM algorithms, reducing overall execution time

### Documentation
- **Update online examples for various modules**: Refreshed and expanded examples across multiple algorithm modules for better user experience

## Download and Installation

You are invited to [download the 1.20.0 release](https://dist.apache.org/repos/dist/release/madlib/1.20.0/) and [review the release notes](https://github.com/apache/madlib/blob/master/RELEASE_NOTES). 

Also please refer to the [list of supported databases and OS](https://cwiki.apache.org/confluence/display/MADLIB/Database+and+OS+Support) for compatibility information.

## What's New

This release marks a significant milestone with the introduction of XGBoost, one of the most popular gradient boosting frameworks. The Python-based implementation provides seamless integration with MADlib's existing ecosystem while offering both simple training and advanced hyperparameter optimization capabilities.

The graph algorithm improvements make MADlib more suitable for complex network analysis tasks, while the performance optimizations ensure better scalability for large datasets.

For technical support and questions, please visit our [community forums](../../community/index.md) or check the [documentation](../../documentation/user-guide.md).