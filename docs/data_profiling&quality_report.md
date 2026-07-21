# Data Profiling & Quality Report

## Project

**Moroccan E-Commerce Data Platform**

---

# Purpose

This report summarizes the quality assessment of the raw Olist datasets before any transformations are applied.

The objective is to identify potential data quality issues that may affect downstream ETL processes, analytics, or machine learning models.

---

# Data Quality Assessment

The following quality checks were performed on all datasets:

- Dataset profiling
- Missing value analysis
- Duplicate record detection
- Primary key validation
- Foreign key validation
- Data type inspection
- Date validation
- Business rule validation
- Categorical value inspection

---

# Assessment Results

## Primary Key Validation

Primary keys were validated for all major tables.

| Dataset | Primary Key | Status |
|----------|-------------|--------|
| Customers | customer_id | ✅ Valid |
| Orders | order_id | ✅ Valid |
| Products | product_id | ✅ Valid |
| Sellers | seller_id | ✅ Valid |
| Reviews | review_id | ✅ Valid |
| Order Items | order_id + order_item_id | ✅ Valid |

No duplicate primary keys were detected.

---

## Foreign Key Validation

Relationships between datasets were verified.

The following relationships were checked:

- Orders → Customers
- Order Items → Orders
- Order Items → Products
- Order Items → Sellers
- Payments → Orders
- Reviews → Orders

No broken relationships were identified.

---

## Missing Values

Missing values were analyzed across all datasets.

### Main observations

- Product dimensions contain missing values.
- Product weight contains missing values.
- Some review fields are empty because customers did not leave comments.
- Delivery timestamps are missing for orders that were not delivered or were cancelled.

These missing values are consistent with the business process and will be handled during the transformation phase.

---

## Duplicate Records

Duplicate records were checked in every dataset.

No unexpected duplicate records requiring removal were identified.

The geolocation dataset contains repeated ZIP code prefixes, which is expected because multiple coordinates may exist for the same postal area.

---

## Date Validation

Timestamp columns were inspected.

Checks included:

- Earliest purchase date
- Latest purchase date
- Missing delivery dates
- Timestamp consistency

No invalid timestamp formats were detected.

---

## Business Rule Validation

The following business rules were verified:

- Product prices are non-negative.
- Freight values are non-negative.
- Payment values are non-negative.
- Review scores are limited to values between 1 and 5.

No violations were detected.

---

## Categorical Data Inspection

The following categorical attributes were reviewed:

- Order status
- Payment methods
- Customer states
- Seller states
- Product categories

The values are consistent and suitable for transformation.

---

# Summary

The raw datasets are of good overall quality and suitable for ETL processing.

The main quality issues identified involve:

- Missing product attributes
- Missing delivery timestamps for incomplete orders
- Missing review comments
- Duplicate geolocation ZIP code prefixes (expected)

These issues do not prevent further processing and will be addressed during the transformation stage.

---

# Next Phase

The next step is to build the Moroccanization Engine.

This phase will transform the Brazilian marketplace into a realistic Moroccan e-commerce platform by:

- Mapping cities and states to Moroccan locations
- Converting prices to Moroccan Dirhams (MAD)
- Replacing payment methods with Moroccan equivalents
- Shifting the calendar to a recent analysis period
- Preparing clean datasets for the PostgreSQL data warehouse