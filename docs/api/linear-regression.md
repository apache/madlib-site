# Linear Regression

Linear regression models the relationship between a scalar dependent variable and one or more explanatory variables using linear predictor functions.

## Overview

Linear regression is one of the most fundamental algorithms in machine learning and statistics. MADlib provides a robust implementation that works efficiently with large datasets in PostgreSQL and Greenplum Database.

## Key Features

- **Scalable**: Handles large datasets efficiently using parallel processing
- **Robust**: Includes options for heteroskedasticity-consistent standard errors
- **Flexible**: Supports various input formats and grouping variables
- **Statistical**: Provides comprehensive statistical output including R², p-values, and confidence intervals

## Basic Usage

### Training a Model

```sql
SELECT madlib.linregr_train(
    'source_table',      -- Input table
    'output_table',      -- Output model table  
    'dependent_var',     -- Y variable
    'ARRAY[1, x1, x2]'   -- Independent variables (include 1 for intercept)
);
```

### Making Predictions

```sql
SELECT madlib.linregr_predict(
    (SELECT coef FROM output_table),
    ARRAY[1, new_x1, new_x2]
) as prediction;
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `source_table` | TEXT | Name of the table containing training data |
| `out_table` | TEXT | Name of the output table for model |
| `dependent_varname` | TEXT | Name of the dependent variable column |
| `independent_varname` | TEXT | Expression for independent variables |
| `grouping_cols` | TEXT | Optional grouping columns |
| `heteroskedasticity_option` | BOOLEAN | Enable robust standard errors |

## Output

The trained model includes:

- **coef**: Coefficient vector
- **r2**: R-squared value
- **std_err**: Standard errors
- **t_stats**: T-statistics  
- **p_values**: P-values for significance testing
- **condition_no**: Condition number for numerical stability

## Examples

### Simple Linear Regression

```sql
-- Create sample data
CREATE TABLE housing AS
SELECT 
    random() * 1000 + 500 as sqft,
    random() * 100000 + 200000 as price
FROM generate_series(1, 1000);

-- Train model
SELECT madlib.linregr_train(
    'housing',
    'housing_model', 
    'price',
    'ARRAY[1, sqft]'
);

-- View results
SELECT * FROM housing_model;
```

### Multiple Linear Regression

```sql
-- Multiple predictors
SELECT madlib.linregr_train(
    'housing',
    'housing_multi_model',
    'price', 
    'ARRAY[1, sqft, bedrooms, bathrooms]'
);
```

### Grouped Regression

```sql
-- Separate models by region
SELECT madlib.linregr_train(
    'housing',
    'housing_by_region',
    'price',
    'ARRAY[1, sqft]',
    'region'
);
```

## Advanced Features

### Robust Standard Errors

```sql
-- Heteroskedasticity-consistent standard errors
SELECT madlib.linregr_train(
    'housing',
    'housing_robust',
    'price',
    'ARRAY[1, sqft]',
    NULL,  -- no grouping
    TRUE   -- robust standard errors
);
```

### Model Diagnostics

```sql
-- Check model quality
SELECT 
    r2,
    CASE WHEN r2 > 0.7 THEN 'Good fit'
         WHEN r2 > 0.5 THEN 'Moderate fit' 
         ELSE 'Poor fit' END as fit_quality
FROM housing_model;
```

## Performance Tips

1. **Include intercept**: Always include 1 in the independent variables array for the intercept term
2. **Scale features**: Consider scaling features if they have very different ranges
3. **Check condition number**: High condition numbers (>1000) may indicate multicollinearity
4. **Use appropriate data types**: FLOAT8 is recommended for numerical stability

## Related Functions

- [Logistic Regression](../versions/latest/group__grp__logreg.html) - For binary/categorical outcomes
- [Elastic Net](../versions/latest/group__grp__elasticnet.html) - Regularized regression
- [Robust Regression](../versions/latest/group__grp__robust.html) - Outlier-resistant regression

## Complete Documentation

For detailed syntax, additional parameters, and more examples:

[**View Complete Linear Regression Documentation**](../versions/latest/group__grp__linreg.html){ .md-button .md-button--primary }

## Mathematical Background

Linear regression finds the best-fitting line through data points by minimizing the sum of squared residuals:

$$\min_{\beta} \sum_{i=1}^{n} (y_i - X_i\beta)^2$$

Where:
- $y_i$ is the dependent variable
- $X_i$ is the vector of independent variables  
- $\beta$ is the coefficient vector to be estimated

The solution is given by the normal equation:
$$\hat{\beta} = (X^TX)^{-1}X^Ty$$