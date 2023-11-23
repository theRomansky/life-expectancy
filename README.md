# Project Title

Life Expectancy Prediction

## Overview

Welcome to the Global Socio-Economic & Demographic Insights project! This initiative draws inspiration from the richness of the World Bank's World Development Indicators, offering a world of possibilities for data enthusiasts, academics, and policy-makers. The datasets provided in this project unfold narratives through numbers and facts, capturing socio-economic and demographic trends spanning multiple decades.

## Dataset Source

The dataset used in this project is sourced from Kaggle, specifically from the "🌏 Global Socio-Economic & Demographic Insights Dataset." The data is an extension of conventional socio-economic datasets, enriched with comprehensive indicators, and meticulously crafted to provide a contextual narrative to the numbers.

**Dataset Link:** [Global Socio-Economic & Demographic Insights Dataset](https://www.kaggle.com/datasets/samybaladram/databank-world-development-indicators)

## Dataset Description

Our datasets transcend traditional data analysis by providing a rich narrative context to numbers. Imputations are grounded in robust statistical methods, and the data is already in long format to facilitate easier analysis and prediction. The dataset covers a wide range of indicators, from fertility rates to economic contributions, offering a comprehensive lens to view and analyze the facets that shape nations.

## Acknowledgment

We acknowledge the origin of our data, aligning region and sub-region classifications with the United Nations geoscheme. The indicators are sourced from the popular indicators from the World Bank's World Development Indicators, attesting to the quality and reliability of the information provided.

## Target Variable

The project focuses on predicting life expectancy at birth (LifeExpBirth), a critical indicator of a nation's overall well-being. This variable is selected as the target variable for regression modeling.

## Models

The project employs regression models, specifically XGBRegressor and CatBoostRegressor, to predict life expectancy at birth. Multiple models are trained and evaluated to explore different approaches to capturing the intricate patterns within the dataset.

## Usage

1. **Data Source:**
   - The dataset is available on Kaggle at [Global Socio-Economic & Demographic Insights Dataset](https://www.kaggle.com/datasets/samybaladram/databank-world-development-indicators).
   - Download and save the dataset locally.

2. **Dependencies:**
   - Ensure you have the required dependencies installed by running `pip install -r requirements.txt`.

3. **Run the Project:**
   - Execute the project's main script to build and evaluate regression models.

    ```bash
    python pipeline.py
    ```

4. **Explore Models:**
   - Review the model performances, including mean squared errors and other relevant metrics, in the logs generated during script execution.

5. **Saved Models:**
   - The best-performing model is saved as a serialized file (`*.pkl`) for future use.

## Conclusion

The Global Socio-Economic & Demographic Insights project provides a platform to explore and analyze the intricate patterns within the World Development Indicators. By predicting life expectancy at birth, the project aims to contribute valuable insights to the understanding of socio-economic and demographic dynamics on a global scale.

Feel free to contribute, provide feedback, or explore additional avenues for analysis within this rich dataset!
