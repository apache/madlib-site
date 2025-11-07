---
date: 2023-06-20
categories:
  - Release
authors:
  - madlib-team
---

# MADlib 2.0.0 Release

On June 20, 2023, MADlib completed its second major release, marking a significant milestone in the project's evolution.

<!-- more -->

## New Features

### Platform Support
- **Add support for python3**: Full Python 3 compatibility for all MADlib components
- **Add support for GP7 Beta**: Early support for Greenplum Database 7 Beta
- **GP6 python3 extension support**: Enhanced Python 3 integration with Greenplum 6
- **Postgres 13/14/15 support**: Extended PostgreSQL compatibility to versions 13, 14, and 15

## Improvements

### Machine Learning Algorithms
- **XGBoost: Add support for version 1.7.5**: Updated to the latest XGBoost version with performance improvements and new features
- **DL: Add support for tensorflow 2.10.1 and keras 2.10.0**: Updated deep learning framework support for better performance and compatibility
- **DBScan: Add support for rtree 1.0.1**: Enhanced clustering algorithm with updated spatial indexing

## Breaking Changes

This major release includes some breaking changes. Please review the [migration guide](https://github.com/apache/madlib/blob/madlib2-master/RELEASE_NOTES) before upgrading from MADlib 1.x versions.

## Download and Installation

You are invited to [download the 2.0.0 release](https://dist.apache.org/repos/dist/release/madlib/2.0.0/) and [review the release notes](https://github.com/apache/madlib/blob/madlib2-master/RELEASE_NOTES). 

Also please refer to the [list of supported databases and OS](https://cwiki.apache.org/confluence/display/MADLIB/Installation+Guide+for+MADlib+2.X) for compatibility information.

## What's New in 2.0

This major release represents a significant step forward in MADlib's evolution, with comprehensive Python 3 support and expanded database platform compatibility. The updated machine learning libraries provide better performance and access to the latest algorithmic improvements.

For technical support and questions, please visit our [community forums](../../community/index.md) or check the [documentation](../../documentation/user-guide.md).