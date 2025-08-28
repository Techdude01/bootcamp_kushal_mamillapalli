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
- Evaluate Results and Risk → Evaluation & Risk Communication (Stage 11) → evaluation risk communication notebook
- Report Results → Results Reporting, Delivery Design & Stakeholder Communication (Stage 12) → Stakeholder_report_12.md
- <Goal M> → Productization (Stage 13) → <Deliverable J>
- <Goal N> → Deployment & Monitoring (Stage 14) → <Deliverable K>
- <Goal O> → Orchestration & System Design (Stage 15) → <Deliverable L>

Stages with no goals or deliverables will be updated as soon as new homeworks are released

## Repo Plan

- /data will have the data
- /src will have useful functions and dir mapping
- /notebooks will have the notebooks to run the code
- /docs will have the documents to explain the code
- /model stores pickled model artifacts (model.pkl)
- /reports stores stakeholder-ready summaries, charts, PDFs

### Quickstart (Fresh Clone)

```bash
git clone <repo>
cd project
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# Option 1: Use environment.yml (Recommended)
conda env create -f environment.yml
conda activate fraud-detection

# Option 2: Use requirements.txt ( may require more packages to be installed )
pip install -r requirements.txt

python app.py  # starts Flask on :8000
# In another terminal:
curl -s http://localhost:8000/health
curl -s -X POST http://localhost:8000/run_full_analysis | jq  # trains+saves model
curl -s -X POST http://localhost:8000/predict \
  -H 'Content-Type: application/json' \
  -d '{"rows":[{"Time":0,"V1":0,"V2":0,"V3":0,"V4":0,"V5":0,"V6":0,"V7":0,"V8":0,"V9":0,"V10":0,"V11":0,"V12":0,"V13":0,"V14":0,"V15":0,"V16":0,"V17":0,"V18":0,"V19":0,"V20":0,"V21":0,"V22":0,"V23":0,"V24":0,"V25":0,"V26":0,"V27":0,"V28":0,"Amount":123.45}]}'
```

### Endpoints Summary

- `GET /health` — service status
- `POST /predict` — JSON body with either `rows` (list of dicts) or `features` (list of lists)
- `GET /predict/<amount>` — convenience path param (other features zeroed)
- `GET /predict/<amount>/<time>` — set Amount and Time via path params
- `GET /plot` — simple inline PNG (homework parity)
- `POST /run_full_analysis` — trains model on processed data and saves artifact

### Error Handling

- Missing/invalid features → `400 {"error": "..."}`
- Missing model artifact → run `POST /run_full_analysis` first to create `model.pkl`.

### Artifacts & Deliverables

- Model artifacts: `project/model/model.pkl`
- Stakeholder report: `project/deliverables/Stakeholder_Report_12.md`
- Figures referenced by report: `project/data/images/`
- Reports directory (for future PDFs/exports): `project/reports/`

### Stakeholder Handoff Summary

- Overview: Binary fraud detection with logistic regression baseline.
- Key findings: High data quality; baseline (100% data) outperforms winsorization/IQR; PR AUC/F1 strongest without aggressive filtering.
- Assumptions: Stable schema, gradual fraud evolution, comparable train/production distributions.
- Risks: Data/concept drift; threshold misconfiguration causing alert fatigue.
- Instructions: Regenerate figures by re-running notebooks; API supports prediction and end-to-end training.
- Next steps: Monitoring dashboards, threshold reviews, periodic retraining cadence.
