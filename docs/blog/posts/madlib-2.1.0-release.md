---
date: 2023-09-08
categories:
  - Release
authors:
  - madlib-team
---

# MADlib 2.1.0 Release

On September 8, 2023, MADlib completed its thirteenth release as an Apache Software Foundation Top Level Project.

<!-- more -->

## Improvements

### Build System
- **Fix PG 15 support**: Enhanced compatibility with PostgreSQL 15
- **Add ubuntu flag for PyXB installation**: Improved installation process on Ubuntu systems
- **Add the actual path of $libdir to dynamic_library_path**: Better library path handling
- **Remove PyXB as a packaged dependency**: Replaced with external pyxb-x dependency for better maintainability
- **Use PG15 in Jenkins CI**: Updated continuous integration to test against PostgreSQL 15

### Algorithm Fixes
- **Assoc_rules: Fix SERIAL cache issue**: Resolved caching problems in association rules algorithm
- **DL: Remove SERIAL from load_keras_model**: Improved deep learning model loading functionality
- **CRF: Fix anyarray -> anycompatiblearray change for PG14**: Updated Conditional Random Fields for PostgreSQL 14 compatibility

## Download and Installation

You are invited to [download the 2.1.0 release](https://dist.apache.org/repos/dist/release/madlib/2.1.0/) and [review the release notes](https://github.com/apache/madlib/blob/madlib2-master/RELEASE_NOTES). 

Also please refer to the [list of supported databases and OS](https://cwiki.apache.org/confluence/display/MADLIB/Installation+Guide+for+MADlib+2.X) for compatibility information.

## What's Next

This release focuses on stability and compatibility improvements, ensuring MADlib works seamlessly with the latest PostgreSQL versions while maintaining backward compatibility with existing installations.

For technical support and questions, please visit our [community forums](../../community/index.md) or check the [documentation](../../documentation/user-guide.md).