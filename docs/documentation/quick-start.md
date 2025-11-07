# Quick Start Guide

Introduction to themes and concepts in MADlib. This guide walks you through an initial data load, training a model, inspecting a model, and scoring a model.

For the complete quick start guide, please visit the [MADlib Wiki Quick Start Guide for Users](https://cwiki.apache.org/confluence/display/MADLIB/Quick+Start+Guide+for+Users).

## Your First MADlib Model

### 1. Create Sample Data
```sql
CREATE TABLE sample_data AS
SELECT 
    random() * 100 as feature1,
    random() * 50 as feature2,
    random() * 200 + 100 as target
FROM generate_series(1, 1000);
```

### 2. Train a Model
```sql
SELECT madlib.linregr_train(
    'sample_data',
    'my_model', 
    'target',
    'ARRAY[1, feature1, feature2]'
);
```

### 3. View Results
```sql
SELECT * FROM my_model;
```

### 4. Make Predictions
```sql
SELECT madlib.linregr_predict(
    (SELECT coef FROM my_model),
    ARRAY[1, 75, 25]
) as prediction;
```

For detailed examples and advanced usage, please refer to the [complete quick start guide](https://cwiki.apache.org/confluence/display/MADLIB/Quick+Start+Guide+for+Users).