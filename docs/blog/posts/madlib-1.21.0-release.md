---
date: 2023-03-01
categories:
  - Release
authors:
  - madlib-team
---

# MADlib 1.21.0 Release

On March 1, 2023, MADlib completed its eleventh release as an Apache Software Foundation Top Level Project.

<!-- more -->

## New Features

### Graph Algorithms
- **Add warm start for weakly connected components**: Improved performance for iterative graph computations by allowing algorithms to resume from previous states
- **Add multicolumn identifier support for SSSP and APSP**: Enhanced Single Source Shortest Path (SSSP) and All Pairs Shortest Path (APSP) algorithms to work with composite keys

### Platform Support
- **Add support for Photon3 OS**: Extended platform compatibility to include VMware's Photon OS 3.0

## Improvements

### XGBoost Enhancements
- **Add support for bigint and varchar columns**: Expanded data type support for XGBoost algorithms, allowing for more flexible data processing
- **Enable eval_metrics parameter**: Added evaluation metrics configuration for better model assessment during training

## Download and Installation

You are invited to [download the 1.21.0 release](https://dist.apache.org/repos/dist/release/madlib/1.21.0/) and [review the release notes](https://github.com/apache/madlib/blob/master/RELEASE_NOTES). 

Also please refer to the [list of supported databases and OS](https://cwiki.apache.org/confluence/display/MADLIB/Database+and+OS+Support) for compatibility information.

## What's New

This release focuses on enhancing graph algorithms and expanding XGBoost capabilities. The warm start feature for graph algorithms significantly improves performance for large-scale graph computations, while the multicolumn support makes the algorithms more flexible for real-world data scenarios.

For technical support and questions, please visit our [community forums](../../community/index.md) or check the [documentation](../../documentation/user-guide.md).