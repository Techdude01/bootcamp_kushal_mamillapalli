## To: NYU MSFE Bootcamp / Financial Institutions

## From: Kushal Mamillapalli

## Date: 08/14/2025

## SUBJECT: Stakeholder Memo: Fraud Predictor

## Project Summary

I am developing an open-source, real-time fraud detection system using Machine Learning to address the critical issue of financial fraud. This solution will detect fraudulent transactions immediately as they occur, preventing financial losses and maintaining user trust through proactive monitoring. Benefitting both users and financial institutions, this project has the ability to tackle credit card fraud as soon as it happens.

## Problem Statement

Fraud is a huge issue for financial institutions because it loses the trust of the user and temporarily or permanently removes money from the users account. Furthermore, detecting fraud generally happens after the user notices the issue themselves.

Therefore, I propose an open source solution that detects fraud immediately when it happens using Machine Learning. By using Anomaly detection Algorithms like simpler Isolation Forests or neural netowrks, the Fraud can be detected as soon as the model inferences on the User History after a transaction or during the transaction, and can notify the User in real time. Ideally, no money would be lost and the issue would take less time to be solved. Some featuers involved would be spend per category, frequency, and time of day.

## Stakeholders

The stakeholders for this projects are banks who offer cards to customers. They would be interested because fraud takes a lot of time and money to handle, and any event causes users to lose trust in the bank, hurting investments and account openings down the line. Not only does this project reduce fraud but also leverages the customer's memory to make sure that suspicious transactions are validated and the customer doesn't have to worry about the effects of fraud on their account.

## Proposed Solution And Deliverable

**Fraud Predictor** - A machine learning-based anomaly detection system that:

- Monitors transactions in real-time using user history analysis
- Employs machine learning algorithms such as Isolation Forests or Neural Networks
- Analyzes key fraud indicators and uses them as features. These include spending patterns, category analysis, frequency, and timing
- End of the line companies will be allowed to provide fraud alerts immediately as they happen and confirm with the user to take action
- Will reduce fraudulent transactions by stopping them as soon as they occur.
-

## Goals

- Creating an optimized machine learning model that is generalizable to the average consumer. This would offer decent results and can identify some transactions as they happen. A specific number for the goal is difficult without identifying the datasets, but I will set it to 50% of fraudulent transactions will be detected.
- If there is time, creating a GUI to add data, train, and add future transactions to classify.
