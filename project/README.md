# Fraud Predictor

## Problem Statement

Fraud is a huge issue for financial institutions because it loses the trust of the user and temporarily or permanently removes money from the users account. Furthermore, detecting fraud generally happens after the user notices the issue themselves.

Therefore, I propose an open source solution that detects fraud immediately when it happens using Machine Learning. By using Anomaly detection Algorithms like simpler Isolation Forests or neural netowrks, the Fraud can be detected as soon as the model inferences on the User History after a transaction or during the transaction, and can notify the User in real time. Ideally, no money would be lost and the issue would take less time to be solved. Some featuers involved would be spend per category, frequency, and time of day.

## Stakeholder & User

The Stakeholder would be the Financial Institutions because they have to implement it and want to reduce fraud.

The User would be customer, given they consent to the model, and they would receive alerts to it.

## Useful Answer & Decision

The Model would be predictive because it is predicting whether a transaction is fraudulent or not. The model's performance would be based on the F1-Score from preciison and recall to balance those two attributes. The higher the F1-Score, the better the model is. The deliverable would be the optimal paramters, and the model's performance.

## Assumptions & Constraints

- open source data is generally accurate
- don't have to worry about any Personally Identifiable Information (PII) due to mock datasets
- capacity should be pretty high as the dataset needs to be pretty large to be usable, especially with neural nets
- latency should be pretty medium-low considering the model's inference is pretty quick, constraints are running it on my computer instead of some high end server.

## Known Unknowns / Risks

- I am not sure which model is going to be the best, neural nets could end up being worse than forests due to the dataset - will use most optial strategy to counteract assumptions of performance
- Data Cleaning and Preparation becomes very complicated while model is underperforming - will use multiple datasets to make sure I don't have to spend a lot of time on this part.

## Data Rules/Storage

- Homework will have its own data folders for easier separation and less clutter around the project data
- raw/ stores raw unprocessed data from donwload/api/scrape
- processed/ stores cleaned and processed data (CSV,Parquet)
- plots/ stores visualizations of data for analysis and cleaning

### Data Folder content

- \*.csv -> Raw or Processed data based on original exported data
- \*.parquet -> optimized data converted form csv, smaller size, better columnar access
- \*.png -> data visualizations for EDA, or general analysis

### File Usage

- **CSV**: Primary format for fraud data inspection and debugging (human-readable)
- **Parquet**: Efficient storage for large fraud datasets (compressed, fast querying for 284K+ transactions) - binary nonreadable
- **Validation**: Both formats include fraud-specific validation (Amount; V1-V28 features will be added later)

## Data Preprocessing/Cleaning Strategy

- **Dataset:** 284,807 credit card transactions with 31 features (V1-V28, Time, Amount, Class)
- **Target:** Binary fraud classification (0=legitimate, 1=fraudulent)
- **Preprocessing Steps:** Missing value handling, data quality filtering, feature normalization
- **Dataset Analysis:** Dataset looks good, no rows dropped with high cleaning constraints, normalization for transactions

### Functions

- **fill_missing_median()**: Fills numeric missing values with column medians - reduce NaNs in column
- **drop_missing()**: Removes rows with missing values based on threshold or specific columns - if too many missing values remove it
- **normalize_data()**: Scales numeric data using MinMax or Standard scaling - scale the data for better visualization/training

## Assumptions

- Normalization improves model performance
- Median usage improves the dataset
- Threshold based dropping is more clear, as high NaN's in a row leads to bad data

## Lifecycle Mapping

Goal → Stage → Deliverable

- Start Project + Research into problem → Problem Framing & Scoping (Stage 01) → Homework 1
- Setup → Tooling Setup (Stage 02) → Homework 2
- Prepare for ML coding → Python Fundamentals (Stage 03) → Homework 3
- Find Data Source → Data Acquisition/Ingestion (Stage 04) → Good dataset found
- Store Dataset → Data Storage (Stage 05) → Place Dataset in data/raw or data/processed (parquet)
- Improve Dataset → Data Preprocessing (Stage 06) → Process the dataset and add it to data/processed
- Analyze Outliers → Outlier Analysis (Stage 07) → Test Winsorization and other data outliers>
- Analyze Data and Relations → Exploratory Data Analysis (Stage 08) → Notebook with Plots and Charts with EDA
- Create Features → Feature Engineering (Stage 09) → Notebook with example features
- Model with different models → Modeling (Regression / Time Series / Classification) (Stage 10) → time-series and linear-regression notebook
- <Goal K> → Evaluation & Risk Communication (Stage 11) → <Deliverable H>
- <Goal L> → Results Reporting, Delivery Design & Stakeholder Communication (Stage 12) → <Deliverable I>
- <Goal M> → Productization (Stage 13) → <Deliverable J>
- <Goal N> → Deployment & Monitoring (Stage 14) → <Deliverable K>
- <Goal O> → Orchestration & System Design (Stage 15) → <Deliverable L>

Stages with no goals or deliverables will be updated as soon as new homeworks are released

## Repo Plan

- /data will have the data
- /src will have useful functions and dir mapping
- /notebooks will have the notebooks to run the code
- /docs will have the documents to explain the code
