# Moroccanization Documentation

## Purpose

The original Olist dataset contains Brazilian-specific information such as cities, states, payment methods, product categories, and currency. To create a realistic Moroccan e-commerce analytics platform, the dataset was adapted to represent the Moroccan market while preserving its structure and analytical value.

The objective of this transformation is to localize the dataset without modifying its business logic or introducing inconsistencies.

---

# Transformation Scope

The following datasets were transformed:

| Dataset         | Transformation                        |
| --------------- | ------------------------------------- |
| customers.csv   | Cities and regions                    |
| sellers.csv     | Cities and regions                    |
| geolocation.csv | Cities and regions                    |
| products.csv    | Product categories                    |
| payments.csv    | Payment methods and currency values   |
| order_items.csv | Price and freight currency conversion |

The remaining datasets required no localization and were kept unchanged.

---

# Applied Transformations

## Customer Locations

Brazilian cities were replaced with Moroccan cities.

Brazilian state abbreviations were replaced with Moroccan administrative regions.

**Example**

| Before         | After      |
| -------------- | ---------- |
| São Paulo      | Casablanca |
| Rio de Janeiro | Rabat      |
| Curitiba       | Marrakech  |

---

## Seller Locations

Seller locations were transformed using the same mapping strategy as customer locations to maintain geographic consistency.

---

## Geolocation

The geolocation dataset was updated to reflect Moroccan cities and regions while preserving latitude and longitude columns for future geographic analysis.

---

## Product Categories

Product category names were translated and adapted to terminology commonly used in Morocco.

Examples include:

* Electronics
* Fashion
* Furniture
* Health & Beauty
* Home Appliances

The purpose was to improve readability without changing the analytical meaning of each category.

---

## Payment Methods

Brazilian payment methods were mapped to equivalent payment methods commonly used in Morocco.

| Original    | Moroccan Equivalent |
| ----------- | ------------------- |
| credit_card | Bank Card           |
| debit_card  | Debit Card          |
| boleto      | Cash on Delivery    |
| voucher     | Mobile Wallet       |

---

## Currency Conversion

Financial values were converted from Brazilian Real (BRL) to Moroccan Dirham (MAD) using a fixed conversion factor.

The following columns were converted:

* price
* freight_value
* payment_value

Relative price differences between products were preserved.

---

# Validation

After the transformation, the following validation checks were performed.

| Validation                      | Result |
| ------------------------------- | ------ |
| Row count preserved             | ✅      |
| Duplicate records introduced    | ❌      |
| Missing values introduced       | ❌      |
| Primary keys modified           | ❌      |
| Referential integrity preserved | ✅      |

# Summary

The Moroccanization process successfully adapted the Brazilian Olist dataset to a Moroccan business context while preserving data quality, dataset structure, and analytical consistency.

The transformed dataset provides a realistic foundation for building an end-to-end e-commerce analytics platform using Data Engineering, Business Intelligence, and Machine Learning techniques.
