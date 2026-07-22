# Feature Engineering Documentation

## Overview

Feature engineering transforms cleaned data into meaningful, reusable business attributes that improve analytics, creates new variables derived from existing information while preserving the original data.

Only **row-level features** were created during this phase.
---

# Objectives

The objectives of this phase are to:

* Create reusable business features.
* Improve data readability.
* Simplify downstream SQL queries.
* Support dashboard development.
* Prepare datasets for machine learning.
* Preserve the original business meaning of the data.

---

# Datasets Enriched

| Dataset     | Engineered Features            |
| ----------- | ------------------------------ |
| Orders      | Temporal and delivery features |
| Products    | Physical product features      |
| Payments    | Payment behavior features      |
| Reviews     | Customer satisfaction features |
| Order Items | Cost-related features          |

No additional features were created for the **Customers**, **Sellers**, or **Geolocation** datasets because they do not contain sufficient row-level information. Their business metrics will be calculated later when multiple datasets are combined.

---

# Order Features

The following temporal and delivery features were created:

* Purchase year
* Purchase month
* Purchase month name
* Purchase day
* Purchase hour
* Purchase weekday
* Delivery duration
* Estimated delivery duration
* Shipping duration
* Delivery delay
* Delivery status

These features support:

* Sales trend analysis
* Seasonal analysis
* Delivery performance monitoring
* Customer purchasing behavior analysis

---

# Product Features

Physical product characteristics were transformed into analytical attributes.

Features include:

* Product volume (cm³)
* Product size category
* Product weight category

These features improve logistics analysis, inventory reporting, and product segmentation.

---

# Payment Features

Payment information was enriched with customer payment behavior features.

Features include:

* Installment indicator
* Installment category
* Payment value category
* Rounded payment value

These attributes simplify financial reporting and payment behavior analysis.

---

# Review Features

Customer ratings were converted into business-friendly categories.

Features include:

* Review sentiment
* Satisfaction level
* Recommendation indicator

These features improve customer satisfaction reporting and simplify dashboard visualizations.

---

# Order Item Features

Order item records were enriched with derived cost metrics.

Features include:

* Total item cost

These features provide additional insight into product-level costs and shipping expenses.

---