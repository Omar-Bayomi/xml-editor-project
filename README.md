## About peer-to-peer
Our peer-to-peer lending dataset is a rich and diverse collection of information that provides a comprehensive view of the lending landscape. It encompasses a wide range of variables that capture various aspects of loan transactions and borrower profiles. This section aims to highlight some of the key characteristics of our dataset, shedding light on its depth and potential for analysis.

1. Loan Specifics:
   The dataset comprises detailed loan-specific attributes such as loan amounts, interest rates, and durations. These variables allow us to explore the distribution of loan sizes, interest rate trends, and the various loan terms borrowers engage with.

2. Borrower Demographics:
   We have access to demographic information about borrowers, including their age, gender, education level, and marital status. This demographic data enables us to understand the composition of borrowers and identify any trends or patterns based on these characteristics.

3. Employment and Income:
   The dataset provides insights into the employment status and income levels of borrowers. By analyzing this information, we can gain insights into the financial stability of borrowers and their ability to meet their repayment obligations.

4. Credit Score and History:
   Credit scores and credit history are vital indicators of borrower creditworthiness. Our dataset includes credit score information, enabling us to assess the impact of credit scores on loan approval and interest rates.

5. Loan Performance:
   With details about principal and interest payments, as well as penalty payments and defaults, we can analyze the performance of loans over time. This information helps us understand the factors contributing to loan success or default.

6. Temporal Data:
   The dataset includes timestamps such as loan issuance dates and maturity dates. Temporal analysis allows us to study how lending trends and borrower behaviors evolve over time.

7. Geographic Insights:
   Through borrower country information, we can explore lending activities across different regions and potentially uncover geographic variations in loan characteristics.

8. Missing Data and Outliers:
   Our dataset also includes missing values and potential outliers, which add a layer of complexity to our analysis. Handling missing data and outliers appropriately is crucial to ensure the accuracy and reliability of our findings.

By understanding the unique characteristics of our dataset, we can make informed decisions during data preprocessing, feature engineering, and modeling. The diverse nature of the data opens the door to a wide array of analyses, and we are excited to uncover valuable insights from this comprehensive peer-to-peer lending dataset.

## Table of Contents

- [Introduction](#introduction)
- [Data Collection](#data-collection)
- [Data Preprocessing](#data-preprocessing)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Feature Engineering](#feature-engineering)
- [Mutual selection](#mutual-selection)
- [Modelling and pipeline](#modelling-and-pipeline)
- [Deployment](#deployment)
- [User Interface](#user-interface)
- [Challenges and Limitations](#challenges-and-limitations)
- [Future Work](#future-work)
- [Acknowledgements](#acknowledgements)

## Introduction

Peer-to-peer lending has transformed the lending landscape, offering borrowers and investors a unique platform for financial transactions.Our data-driven approach not only predicts loan statuses but also anticipates key factors like EMI (Equated Monthly Installments), ELA (Effective Loan Amount), and ROI (Return on Investment).
Our journey unfolds as follows:
1. Data Collection.
2. Data Preprocessing.
3. Exploratory Data Analysis.
4. Feature Engineering.
5. Modelling and pipeline.
6. Deployment.
7. User Interface.

## Data Collection

In this project, the dataset used for analysis was graciously provided by our supervisor. The peer-to-peer lending data, available on Kaggle, was meticulously curated and encompasses a wide array of information sourced from loan platforms and borrower profiles.

## Data Preprocessing
During this phase, we focus on preparing the raw dataset for analysis by addressing issues such as missing values, outliers, and inconsistent formatting. By ensuring the data is clean and standardized, we lay the groundwork for accurate and reliable analysis.
We start by identifying and handling missing values in both categorical and numerical columns. Categorical columns are imputed with the "Unknown" category, while numerical columns are imputed using either the mean or median, depending on the presence of outliers.
Next, we address outliers in the numeric columns. Outliers can significantly impact the distribution and statistical measures of the data. We employ various techniques to identify and handle outliers, including z-score analysis and the Interquartile Range (IQR) method.
Furthermore, categorical variables are mapped to more meaningful labels using predefined mappings. This ensures that categorical data is easily interpretable and contributes effectively to our analysis.
Through these preprocessing steps, we create a clean and standardized dataset that serves as the foundation for exploratory data analysis, feature engineering, and subsequent modeling.

<img src="screenshots/1 (1).png" alt="drawing" width="700"/> <img src="screenshots/1 (2).png" alt="drawing" width="700"/>


## Exploratory Data Analysis
In the Exploratory Data Analysis phase of our project, we delve into the prepared dataset to uncover insights and patterns that can guide our analysis and modeling. Through a combination of statistical analysis and data visualization.
So we made some visualization like :-
Univariate Analysis:
We begin by examining individual variables in isolation through univariate analysis.
<img src="screenshots/1 (3).png" alt="drawing" width="700"/> 
Bivariate Analysis:
Moving beyond individual variables, we explore relationships between two variables using bivariate analysis. Scatter plots, bar plots, and box plots are used to visualize the interactions between pairs of variables.
<img src="screenshots/1 (4).png" alt="drawing" width="700"/>
Multivariate Analysis:
Incorporating more complexity, multivariate analysis involves the visualization of interactions between three or more variables.

## Feature Engineering
Feature engineering was an important step in our analysis as it played a significant role in using each feature properly and getting the most advantage from it.

These are the stpes we followed in our feature engineering:
- Scaling numerical features using MinMaxScaler.

```
scaler = MinMaxScaler()

numeric_cols = ['Status','Interest', 'IncomeTotal', 'ExistingLiabilities', 'DebtToIncome', 'CreditScoreEeMini', 'AppliedAmount', 'PrincipalPaymentsMade', 'InterestAndPenaltyPaymentsMade' 'Loan_Tenure']

df_new[numeric_cols] = scaler.fit_transform(df_new[numeric_cols])
```

- Performing one-hot encoding on categorical features.
```
df_new = pd.get_dummies(df_new, columns=['Age','Gender','Country','Education','MaritalStatus','EmploymentStatus','CreditScoreEsMicroL','ActiveLateCategory','WorseLateCategory'], drop_first=True)
```

- Dropping some columns: 

dropping features that are unique for each loan and dropping some unneeded dates 

```
df_new.drop(['LoanId', 'LoanNumber', 'MaturityDate_Original', 'LoanDate'], axis=1, inplace=True)
```
  dropping some features with high correlation (>80%) with other features.

```
dropped_features=['LoanDuration','MonthlyPayment','Amount','Total_Payment_Due','Max_allowable_amount','LiabilitiesTotal']

df_new = df_new.drop(dropped_features, axis=1)
```

   <img src="screenshots/image-4.png" alt="drawing" width="700"/>


- Replacing 'ELA' feature with 'ELA_mean' which contains the mean values of 'EMI' feature for each unique value in the 'ELA' column.

```
target_mean = df_new.groupby('ELA')['EMI'].mean()

df_new['ELA_mean'] = df_new['ELA'].map(target_mean)
```

<img src="screenshots/image.png" alt="drawing" width="300"/><img src="screenshots/image-1.png" alt="drawing" width="300"/>

- Converting AppliedAmount scale to log scale as it is skewed.

```
df_new['AppliedAmount_log'] = np.log1p(df_new['AppliedAmount'])
```

<img src="screenshots/image-2.png" alt="drawing" width="300"/><img src="screenshots/image-3.png" alt="drawing" width="300"/>

**Notice the scale**

## Mutual selection 

The features DataFrame contains the input features, while target_emi, target_ela, and target_roi are the target variables ('EMI', 'ELA_mean', and 'ROI', respectively) extracted from the df_new DataFrame.

Any infinite or NaN values in the target variables are replaced with zeros to ensure the data's numerical stability.

The StandardScaler is used to scale the target variables individually. This helps standardize the data and can lead to better performance during modeling.

Mutual information scores are calculated between the features and each scaled target variable using the mutual_info_regression function. Mutual information measures the dependence between variables, which helps in identifying informative features.

The calculated mutual information scores are sorted in descending order, and the indices of the top features are extracted to create lists of selected features (selected_features_emi, selected_features_ela, and selected_features_roi) for each target variable.

Finally, new DataFrames (reduced_features_emi, reduced_features_ela, and reduced_features_roi) are created by concatenating the selected features with their respective target variables. These reduced feature sets can then be used for machine learning modeling tasks.


```
scaler = StandardScaler()

target_emi_scaled = scaler.fit_transform(target_emi.values.reshape(-1, 1))

mi_scores_emi = mutual_info_regression(features, target_emi_scaled.ravel())

selected_features_emi = features.columns[(-mi_scores_emi).argsort()[:10]]

reduced_features_emi = pd.concat([features[selected_features_emi], target_emi], axis=1)
```
**(Same for ELA and ROI targets)**

```
reduced_feature_sets = [reduced_features_emi, reduced_features_ela.iloc[:, :-1], reduced_features_roi.iloc[:, :-1]]

combined_features = pd.concat(reduced_feature_sets, axis=1)

mutual_selection_features = combined_features.loc[:, ~combined_features.columns.duplicated()]
```

## Modeling and Pipeline

<p align="center">
<img src="screenshots/image-5.jpg" alt="drawing" width="700"/>
</p>

**Regression:**

We create a regression model, Pipeline for constructing a pipeline of processing steps, StandardScaler for feature scaling, PCA for dimensionality reduction, and r2_score for calculating the R-squared score.

We have three models, linear regression, ridge regression, and xgboost regression

A regression model is initialized, which will serve as the final regression model in the pipeline.

The pipeline is defined by stacking preprocessing steps, PCA, and the regression model. The pipeline starts with feature scaling using StandardScaler to standardize the input features, then applies PCA to reduce the dimensionality of the data, and finally includes the linear regression model as the classifier.

The pipeline is trained on the training data (X_train and y_train_ROI) using the fit method.

The pipeline model is used to make predictions (pred) on the test data (X_test).

The R-squared score is calculated using the r2_score function, which measures the proportion of the variance in the dependent variable that is predictable from the independent variables.

The R-squared score is printed, providing insight into the quality of the model's predictions. A higher R-squared score indicates a better fit to the data.
```
linear_regression_model = LinearRegression()

model_linear_regression = Pipeline([
    ('stdscaler', stdscaler),
    ('pca', pca),
    ('classifier', linear_regression_model)
])
```
Same for `ridge_regression_model = Ridge(alpha=1.0)` and `xgboost_regression_model = XGBRegressor()`

| Model              | Accuracy |
| ---------          | ------- |
Linear regression  | 59% 
Ridge regression| 50%
xgboost regression |91%
Stacked model  | 90% 
```
knn_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=0.95, random_state=42)),
    ('regressor', StackedRegressor())
])
```

**Classification :**

We used similar steps for the classification pipelines, and we had two models which are KNN classifier and xgb classifier.

```
knn_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=0.95, random_state=42)),
    ('classifier', KNeighborsClassifier())
])
```
Same for `XGBClassifier()`
| Model              | Accuracy |
| ---------          | ------- |
KNN  Classification  | 87% 
xgb Classification |88%


## Deployment

Once we performed the pipelines, we provided detailed steps and code for deploying the model. Our team has developed an intuitive and user-friendly Streamlit application that serves as a powerful tool for making predictions on loan data. This application boasts a simple yet effective user interface, designed to effortlessly facilitate user interaction. With a seamless interface, users can conveniently input various features related to loans, whether they are numerical or categorical in nature. Once the feature values are provided, our app leverages both regression and classification models to generate insightful predictions. For regression, users gain predictions on three crucial variables: 'ROI' (Return on Investment), 'EMI' (Equated Monthly Installment), and 'ELA_mean' (Expected Loan Amount mean). Meanwhile, the classification model outputs predictions on the 'Status' of the loan. Our Streamlit app empowers users to make informed decisions by swiftly and accurately obtaining these predictions, thus adding an extra layer of data-driven decision-making to the loan management process.
