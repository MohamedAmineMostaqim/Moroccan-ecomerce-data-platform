# Data Cleaning Documentation

## Overview

Following the Moroccanization process, the datasets were cleaned and standardized to improve consistency and ensure they were ready.

The cleaning process focused on validating data quality, standardizing formats, and handling invalid values while preserving the integrity of the original datasets.

---

# Objectives

The main objectives of this phase were to:

* Standardize textual data.
* Convert columns to appropriate data types.
* Validate business rules.
* Handle invalid numerical values.
* Remove duplicate records.
* Produce clean and consistent datasets for downstream analytics.

---

# Datasets Processed

The following datasets were cleaned:

| Dataset         | Description            |
| --------------- | ---------------------- |
| customers.csv   | Customer information   |
| orders.csv      | Order information      |
| order_items.csv | Order line items       |
| payments.csv    | Payment information    |
| products.csv    | Product catalog        |
| reviews.csv     | Customer reviews       |
| sellers.csv     | Seller information     |
| geolocation.csv | Geographic information |

---

# Cleaning Operations

## Column Standardization

All column names were standardized using the following rules:

* Converted to lowercase.
* Removed leading and trailing spaces.
* Replaced spaces with underscores.
* Ensured consistent naming conventions.

---

## Text Standardization

Text columns were standardized by:

* Removing unnecessary whitespace.
* Collapsing multiple consecutive spaces.
* Converting city names to Title Case.
* Converting region codes to uppercase.
* Standardizing payment method names.
* Standardizing product category names.

---

## Datetime Conversion

Order timestamp columns were converted to the appropriate datetime format.

The following columns were processed:

* order_purchase_timestamp
* order_approved_at
* order_delivered_carrier_date
* order_delivered_customer_date
* order_estimated_delivery_date

This enables accurate time-based analysis and feature engineering.

---

## Duplicate Records

Duplicate records were identified and removed where necessary.

---

## Numerical Validation

Numerical columns were validated to detect invalid values.

The following checks were performed:

* Negative payment values.
* Negative product prices.
* Negative freight values.
* Invalid product dimensions.
* Invalid product weights.

Invalid values were replaced with missing values (`NaN`) rather than being silently corrected to preserve data integrity.

---

## Review Score Validation

Customer review scores were validated to ensure that values remained within the expected range of **1 to 5**.

Invalid review scores were replaced with missing values (`NaN`).

---

# Validation Summary

The following validation checks were completed after cleaning.

| Validation                     | Result |
| ------------------------------ | ------ |
| Column names standardized      | ✅      |
| Text standardized              | ✅      |
| Datetime conversion completed  | ✅      |
| Duplicate records checked      | ✅      |
| Numerical validation completed | ✅      |
| Review scores validated        | ✅      |
| Date consistency validated     | ✅      |

---

# Output

The cleaned datasets overwrite the existing files in:

```text
data/
└── processed/
```

These datasets serve as the official source for the remaining stages of the project.

