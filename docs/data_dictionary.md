# Data Dictionary

## Overview

This document describes the structure of the raw datasets used in the Moroccan E-Commerce Data Platform project.

The source data comes from the Olist Brazilian E-Commerce Dataset and will later be transformed into a Moroccan marketplace dataset through the ETL pipeline.

---

# Dataset Overview

| Dataset | Description | Primary Key |
|----------|-------------|-------------|
| customers | Customer information | customer_id |
| orders | Customer orders | order_id |
| order_items | Products included in each order | order_id + order_item_id |
| products | Product catalog | product_id |
| sellers | Marketplace sellers | seller_id |
| payments | Payment transactions | order_id |
| reviews | Customer reviews | review_id |
| geolocation | Geographic locations | geolocation_zip_code_prefix |
| category_translation | Product category translations | product_category_name |

---

# customers

Stores customer information.

| Column | Type | Description |
|---------|------|-------------|
| customer_id | string | Unique customer identifier |
| customer_unique_id | string | Customer identifier across multiple orders |
| customer_zip_code_prefix | integer | ZIP code prefix |
| customer_city | string | Customer city |
| customer_state | string | Customer state |

---

# orders

Stores information about customer orders.

| Column | Type | Description |
|---------|------|-------------|
| order_id | string | Unique order identifier |
| customer_id | string | Customer who placed the order |
| order_status | string | Order status |
| order_purchase_timestamp | datetime | Purchase timestamp |
| order_approved_at | datetime | Payment approval timestamp |
| order_delivered_carrier_date | datetime | Carrier pickup date |
| order_delivered_customer_date | datetime | Delivery date |
| order_estimated_delivery_date | datetime | Estimated delivery date |

---

# order_items

Stores purchased products.

| Column | Type | Description |
|---------|------|-------------|
| order_id | string | Order identifier |
| order_item_id | integer | Item number within an order |
| product_id | string | Product identifier |
| seller_id | string | Seller identifier |
| shipping_limit_date | datetime | Shipping deadline |
| price | decimal | Product price |
| freight_value | decimal | Shipping cost |

---

# products

Stores product information.

| Column | Type | Description |
|---------|------|-------------|
| product_id | string | Product identifier |
| product_category_name | string | Product category |
| product_name_lenght | integer | Product name length *(original dataset spelling)* |
| product_description_lenght | integer | Product description length *(original dataset spelling)* |
| product_photos_qty | integer | Number of product photos |
| product_weight_g | integer | Product weight (grams) |
| product_length_cm | decimal | Product length (cm) |
| product_height_cm | decimal | Product height (cm) |
| product_width_cm | decimal | Product width (cm) |

---

# sellers

Stores marketplace seller information.

| Column | Type | Description |
|---------|------|-------------|
| seller_id | string | Seller identifier |
| seller_zip_code_prefix | integer | ZIP code prefix |
| seller_city | string | Seller city |
| seller_state | string | Seller state |

---

# payments

Stores payment information.

| Column | Type | Description |
|---------|------|-------------|
| order_id | string | Order identifier |
| payment_sequential | integer | Payment sequence |
| payment_type | string | Payment method |
| payment_installments | integer | Number of installments |
| payment_value | decimal | Payment amount |

---

# reviews

Stores customer reviews.

| Column | Type | Description |
|---------|------|-------------|
| review_id | string | Review identifier |
| order_id | string | Associated order |
| review_score | integer | Rating from 1 to 5 |
| review_comment_title | string | Review title |
| review_comment_message | string | Review message |
| review_creation_date | datetime | Review creation date |
| review_answer_timestamp | datetime | Review response timestamp |

---

# geolocation

Stores geographic information.

| Column | Type | Description |
|---------|------|-------------|
| geolocation_zip_code_prefix | integer | ZIP code prefix |
| geolocation_lat | decimal | Latitude |
| geolocation_lng | decimal | Longitude |
| geolocation_city | string | City |
| geolocation_state | string | State |

---

# category_translation

Maps Portuguese product categories to English.

| Column | Type | Description |
|---------|------|-------------|
| product_category_name | string | Portuguese category |
| product_category_name_english | string | English category |