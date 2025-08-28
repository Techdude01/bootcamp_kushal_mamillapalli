# Stage 14: Deployment and Monitoring Reflection

## 1) Reflection (200-300 words)

### Risks if deployed:

**Model Performance Risks:**

- False negatives (missed fraud) could cost millions in undetected fraudulent transactions
- False positives (blocking legitimate transactions) damage customer experience and revenue
- Model drift as fraud patterns evolve, requiring retraining with F1-score monitoring
- Low recall (91.8%) means ~8% of fraud goes undetected in production

**Technical Risks:**

- Flask API single-threaded bottleneck under high transaction volume
- Model prediction latency causing transaction delays (current warnings suggest performance issues)
- Memory consumption with StandardScaler + LogisticRegression pipeline
- No load balancing or failover for the API endpoint

**Data Quality Risks:**

- Missing V1-V28 features (PCA components) if data pipeline changes
- Amount/Time feature drift as transaction patterns change
- Inconsistent feature scaling between training and inference

### Monitoring metrics across layers:

**Data Layer:**

- Feature distribution drift (KL divergence > 0.1 for V14, V17, V12 triggers alert)
- Missing feature rate < 1% (V1-V28, Amount, Time)
- Amount distribution p95 > $5000 indicates unusual patterns

**Model Layer:**

- Precision > 6% (current baseline), Recall > 90%, F1-score > 11%
- PR-AUC > 0.72 (current benchmark)
- Prediction latency p95 < 250ms triggers on-call notification
- Daily fraud detection rate between 0.1-0.3% (baseline range)

**System Layer:**

- API response time p95 < 500ms
- Error rate < 0.1% for /predict endpoint
- Memory usage < 2GB for Flask process
- CPU utilization < 80% during peak hours

**Business Layer:**

- Financial loss from missed fraud < $10K/day
- Customer complaint rate < 0.05% for blocked legitimate transactions
- Daily transaction approval rate > 99.5%

### Ownership & handoffs:

**Data Science Team:** Model retraining, performance monitoring, feature engineering
**Engineering Team:** API maintenance, scaling, infrastructure monitoring  
**Risk Team:** Business metric thresholds, fraud pattern analysis
**On-call rotation:** 24/7 for p95 latency > 250ms, error rate > 0.1%, or fraud detection drops below 0.1%
