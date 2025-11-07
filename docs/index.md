---
hide:
  - navigation
  - toc
---

<div class="homepage-content" markdown>

<div class="hero-center" markdown>

# Welcome to Apache MADlib, Big Data Machine Learning in SQL

<img src="./assets/madlib.svg" width="300px" class="hero-logo">

</div>

<div class="hero-section" markdown align="center">

**Apache MADlib** is an open source machine learning library designed for big data analytics that runs directly in PostgreSQL and Greenplum Database®.

[Download](download.md){ .md-button .md-button--primary }
[View Documentation](documentation/user-guide.md){ .md-button }

</div>

<!-- Latest News Section -->
<div class="latest-news-light" markdown>

### 📢 Latest News: [MADlib 2.1.0 Release](blog/posts/madlib-2.1.0-release.md)

</div>

## Hightlights

<div class="grid cards" markdown>

-   __Open Source, Commercially Friendly Apache License__

    ---

    Apache License, commercially friendly open source license

-   __For PostgreSQL and Greenplum Database®__

    ---

    Supports PostgreSQL and Greenplum Database®, process data in-place

-   __Powerful Machine Learning, Graph, Statistics and Analytics__

    ---

    Provides powerful machine learning, graph, statistics and analytics for data scientists

</div>

## Product Overview

<div class="text-center" markdown>

In a world of ever increasing data size, many existing analytics solutions are not up to the task. The MADlib project seeks to address this need by creating a framework built to take advantage of modern computing capabilities to provide robust solutions that scale with the needs of the business.

Our approach is to leverage the efforts of commercial practice, academic research, and the open-source development community.

</div>

### Key Philosophies Driving the Architecture of MADlib

<div class="grid cards" markdown>

-   __Operate on the data locally in-database__

    ---

    Do not move data between multiple runtime environments unnecessarily.

-   __Utilize best of breed database engines__

    ---

    But separate the machine learning logic from database specific implementation details.

-   __Leverage MPP shared nothing technology__

    ---

    Such as the Greenplum Database, to provide parallelism and scalability.

-   __Open implementation__

    ---

    Maintaining active ties into Apache community and ongoing academic research.

</div>

## Features & Capabilities

<div class="grid cards" markdown>

-   ![Classification](assets/classification.png){ align=left width=64 } __Classification__

    ---

    When the desired output is categorical in nature, we use classification methods to build a model that predicts which of the various categories a new result would fall into.

-   ![Regression](assets/regression.png){ align=left width=64 } __Regression__

    ---

    When the desired output is continuous in nature, we use regression methods to build a model that predicts the output value.

-   ![Deep Learning](assets/neural-net.png){ align=left width=64 } __Deep Learning__

    ---

    Deep learning uses artificial neural networks inspired by biology of the brain. GPU acceleration is widely used to speed training.

-   ![Clustering](assets/clustering.png){ align=left width=64 } __Clustering__

    ---

    Identify groups of data such that items within one cluster are more similar to each other than to items in other clusters.

-   ![Topic Modeling](assets/topic-modelling.png){ align=left width=64 } __Topic Modeling__

    ---

    Similar to clustering but specific to text domain, attempting to identify clusters of documents and their main themes.

-   ![Association Rule Mining](assets/rule-mining.png){ align=left width=64 } __Association Rule Mining__

    ---

    Also called market basket analysis, this identifies which items tend to occur together more frequently than random chance.

-   ![Descriptive Statistics](assets/descriptive-statistics.png){ align=left width=64 } __Descriptive Statistics__

    ---

    Provide valuable insights into data that may influence choice of data model and help analysts understand underlying patterns.

-   ![Validation](assets/validation.png){ align=left width=64 } __Validation__

    ---

    Evaluate model accuracy on test data using techniques like N-fold cross validation to ensure models are not over-fitting.

</div>

## Getting Started with Apache MADlib using Jupyter Notebooks

<div class="text-center" markdown>

We have created a [library of Jupyter Notebooks](https://github.com/apache/madlib-site/tree/asf-site/community-artifacts) to help you get started quickly with MADlib. It includes many commonly used algorithms by data scientists.

</div>
</div> <!-- End homepage-content -->