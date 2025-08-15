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

## Lifecycle Mapping

Goal → Stage → Deliverable

- Start Project + Plan → Problem Framing & Scoping (Stage 01) → Homework 1
- Start Project + Plan → Tooling Setup (Stage 02) → Homework 1
- Start Project + Plan → Python Fundamentals (Stage 03) → Homework 1
- <Goal D> → Data Acquisition/Ingestion (Stage 04) → <Deliverable A>
- <Goal E> → Data Storage (Stage 05) → <Deliverable B>
- <Goal F> → Data Preprocessing (Stage 06) → <Deliverable C>
- <Goal G> → Outlier Analysis (Stage 07) → <Deliverable D>
- <Goal H> → Exploratory Data Analysis (Stage 08) → <Deliverable E>
- <Goal I> → Feature Engineering (Stage 09) → <Deliverable F>
- <Goal J> → Modeling (Regression / Time Series / Classification) (Stage 10) → <Deliverable G>
- <Goal K> → Evaluation & Risk Communication (Stage 11) → <Deliverable H>
- <Goal L> → Results Reporting, Delivery Design & Stakeholder Communication (Stage 12) → <Deliverable I>
- <Goal M> → Productization (Stage 13) → <Deliverable J>
- <Goal N> → Deployment & Monitoring (Stage 14) → <Deliverable K>
- <Goal O> → Orchestration & System Design (Stage 15) → <Deliverable L>

stages with no goals or deliverables will be updated as soon as new homeworks are released

## Repo Plan

- /data will have the data
- /src will have useful functions and dir mapping
- /notebooks will have the notebooks to run the code
- /docs will have the documents to explain the code
