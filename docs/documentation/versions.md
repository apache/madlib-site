# Documentation Versions

Apache MADlib maintains documentation for all major releases. Choose the version that matches your MADlib installation.

!!! info "Legacy Documentation"
    The version-specific documentation links below point to the complete API reference documentation generated from the source code. These have a different interface than this site but contain comprehensive technical details.

## Current Versions

### Latest Stable Release
- [MADlib Latest](../../docs/latest/index.html) - Always points to the most recent stable release

### Recent Releases
- [MADlib v2.1.0](../../docs/v2.1.0/index.html) - September 2023
- [MADlib v2.0.0](../../docs/v2.0.0/index.html) - June 2023 (Major Release)
- [MADlib v1.21.0](../../docs/v1.21.0/index.html) - March 2023
- [MADlib v1.20.0](../../docs/v1.20.0/index.html) - August 2022
- [MADlib v1.19.0](../../docs/v1.19.0/index.html) - March 2022
- [MADlib v1.18.0](../../docs/v1.18.0/index.html) - April 2021

## Historical Versions

<details>
<summary>Click to expand historical versions</summary>

- [MADlib v1.17.0](../../docs/v1.17.0/index.html) - April 2020
- [MADlib v1.16](../../docs/v1.16/index.html) - September 2019
- [MADlib v1.15.1](../../docs/v1.15.1/index.html) - February 2019
- [MADlib v1.15](../../docs/v1.15/index.html) - September 2018
- [MADlib v1.14](../../docs/v1.14/index.html) - January 2018
- [MADlib v1.13](../../docs/v1.13/index.html) - July 2017
- [MADlib v1.12](../../docs/v1.12/index.html) - September 2016
- [MADlib v1.11](../../docs/v1.11/index.html) - July 2016
- [MADlib v1.10](../../docs/v1.10/index.html) - February 2016
- [MADlib v1.9.1](../../docs/v1.9.1/index.html) - September 2015
- [MADlib v1.9](../../docs/v1.9/index.html) - July 2015
- [MADlib v1.8](../../docs/v1.8/index.html) - February 2015
- [MADlib v1.7.1](../../docs/v1.7.1/index.html) - October 2014
- [MADlib v1.7](../../docs/v1.7/index.html) - July 2014
- [MADlib v1.6](../../docs/v1.6/index.html) - December 2013
- [MADlib v1.5](../../docs/v1.5/index.html) - July 2013
- [MADlib v1.4](../../docs/v1.4/index.html) - February 2013
- [MADlib v1.3](../../docs/v1.3/index.html) - October 2012
- [MADlib v1.2](../../docs/v1.2/index.html) - July 2012
- [MADlib v1.1](../../docs/v1.1/index.html) - March 2012
- [MADlib v1.0](../../docs/v1.0/index.html) - October 2011

</details>

## Version Compatibility

| MADlib Version | PostgreSQL | Greenplum | Python | Release Date |
|----------------|------------|-----------|---------|--------------|
| 2.1.0 | 11-15 | 6.x, 7.x | 3.x | Sep 2023 |
| 2.0.0 | 11-15 | 6.x, 7.x | 3.x | Jun 2023 |
| 1.21.0 | 9.6-12 | 5.x, 6.x | 2.7, 3.x | Mar 2023 |
| 1.20.0 | 9.6-12 | 5.x, 6.x | 2.7, 3.x | Aug 2022 |
| 1.19.0 | 9.6-12 | 5.x, 6.x | 2.7 | Mar 2022 |
| 1.18.0 | 9.6-12 | 5.x, 6.x | 2.7 | Apr 2021 |

## Finding the Right Version

1. **Check your MADlib installation**:
   ```sql
   SELECT madlib.version();
   ```

2. **Match the documentation version** to your installed version

3. **For new installations**, use the [latest stable release](../../docs/latest/index.html)

## Migration Guides

When upgrading between major versions, please refer to:

- [MADlib 2.0 Migration Guide](../blog/posts/madlib-2.0.0-release.md) - For upgrading from 1.x to 2.x
- [Release Notes](https://github.com/apache/madlib/blob/master/RELEASE_NOTES) - Detailed changes for each version

## Need Help?

If you can't find the documentation version you need or have questions about compatibility:

- Visit our [community forums](../community/index.md)
- Check the [installation guide](installation.md)
- Review [supported platforms](https://cwiki.apache.org/confluence/display/MADLIB/Database+and+OS+Support)