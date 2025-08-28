## 1) Reflection (200–300 words)

**Risks if deployed:**
The fraud detection model faces four critical failure modes:

- (1) Schema Changes - if the data structure changes (new columns, different V1-V28 features), the model will fail completely because it expects specific features.
- (2) Concept Drift - as fraud patterns evolve over time, the model's understanding becomes outdated and it misses new fraud types, reducing recall below 90%.
- (3) Latency spikes - if the API becomes slow, legitimate transactions get blocked, damaging customer experience and revenue.
- (4) Silent degradation - the model appears stable on surface metrics but secretly gets worse at detecting expensive fraud, leading to increased financial losses without obvious warning signs.

**Monitoring metrics across four layers:**

- **Data Layer**: Schema Changes using Schema Hash Mismatches; this is importnat to makes ure the data is the same and does not change, or have other columns that mess up the model.
- **Model Layer**: Concept Drift would be monitored with Rolling MAE to make sure the old patterns are still being observed in the data and predictions.
- **System Layer**: Latency spikes would be monitored with p95 latency in miliseconds to make sure there are no issues accessing the API or the timeliness
- **Business Layer**: Silent degradation would be handled with Calibration and business KPI shift, meaning that the hard to see worsened performance can be fixed with business metrics being a sign and Calibration working to make sure the model's Confidence is actually good.

**Ownership and handoffs:**

- Data Science team owns model retraining, seen with probelms in the Model layer (concept drift) or from the business end due to silent degradation. Also, the Data Science team also onws managing the data layer to make sure the schema matches throughout usage.
- The platform/system team holds the repsonsibility of making sure there are no latency spikes and access ig all good.
- The Business team would use their metrics to make sure the model isn't actually missing fraud cases to cause huge losses, and send that data to Data Science for them to fix.
