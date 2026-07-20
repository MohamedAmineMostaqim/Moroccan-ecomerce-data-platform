"""
Moroccanization Engine

Transforms the Brazilian Olist dataset into a fictional
Moroccan e-commerce marketplace.
"""

import numpy as np
import pandas as pd

from config import ASSETS

from utils import (
    load_mapping,
    convert_currency,
    shift_dates,
    generate_zip_codes,
    generate_latitudes,
    generate_longitudes,
)
from config import (
    RAW_DATA,
    PROCESSED_DATA,
    CUSTOMERS_FILE,
    ORDERS_FILE,
    ORDER_ITEMS_FILE,
    PAYMENTS_FILE,
    PRODUCTS_FILE,
    SELLERS_FILE,
    REVIEWS_FILE,
    GEOLOCATION_FILE,
    CATEGORY_TRANSLATION_FILE,
    OUTPUT_CUSTOMERS,
    OUTPUT_ORDERS,
    OUTPUT_ORDER_ITEMS,
    OUTPUT_PAYMENTS,
    OUTPUT_PRODUCTS,
    OUTPUT_SELLERS,
    OUTPUT_REVIEWS,
    OUTPUT_GEOLOCATION,
    OUTPUT_CATEGORIES,
)

from utils import (
    load_csv,
    save_csv,
    log_transformation,
)

# LOAD MAPPINGS


CITY_MAPPING = load_mapping(
    ASSETS / "city_mapping.csv",
    "brazilian_city",
    "moroccan_city"
)

STATE_MAPPING = load_mapping(
    ASSETS / "state_mapping.csv",
    "brazilian_state",
    "moroccan_region"
)

PAYMENT_MAPPING = load_mapping(
    ASSETS / "payment_mapping.csv",
    "brazilian",
    "moroccan"
)

CATEGORY_MAPPING = load_mapping(
    ASSETS / "category_mapping.csv",
    "english_category",
    "moroccan_category"
)

#CUSTOMERS
def moroccanize_customers(customers: pd.DataFrame):

    customers = customers.copy()

    customers["customer_city"] = (
        customers["customer_city"]
        .str.lower()
        .map(CITY_MAPPING)
        .fillna("Casablanca")
    )

    customers["customer_state"] = (
        customers["customer_state"]
        .map(STATE_MAPPING)
        .fillna("Casablanca-Settat")
    )

    customers["customer_zip_code_prefix"] = generate_zip_codes(
        len(customers)
    )

    return customers

#SELLERS
def moroccanize_sellers(sellers: pd.DataFrame):

    sellers = sellers.copy()

    sellers["seller_city"] = (
        sellers["seller_city"]
        .str.lower()
        .map(CITY_MAPPING)
        .fillna("Casablanca")
    )

    sellers["seller_state"] = (
        sellers["seller_state"]
        .map(STATE_MAPPING)
        .fillna("Casablanca-Settat")
    )

    sellers["seller_zip_code_prefix"] = generate_zip_codes(
        len(sellers)
    )

    return sellers


#GEOLOCATION
def moroccanize_geolocation(geo: pd.DataFrame):

    geo = geo.copy()

    geo["geolocation_city"] = (
        geo["geolocation_city"]
        .str.lower()
        .map(CITY_MAPPING)
        .fillna("Casablanca")
    )

    geo["geolocation_state"] = (
        geo["geolocation_state"]
        .map(STATE_MAPPING)
        .fillna("Casablanca-Settat")
    )

    geo["geolocation_zip_code_prefix"] = generate_zip_codes(
        len(geo)
    )

    geo["geolocation_lat"] = generate_latitudes(
        len(geo)
    )

    geo["geolocation_lng"] = generate_longitudes(
        len(geo)
    )

    return geo

#ORDERS
def moroccanize_orders(orders: pd.DataFrame):

    orders = orders.copy()

    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]

    orders = shift_dates(
        orders,
        date_columns
    )

    return orders

#ORDER ITEMS
def moroccanize_order_items(order_items: pd.DataFrame):

    order_items = order_items.copy()

    order_items["price"] = convert_currency(
        order_items["price"]
    )

    order_items["freight_value"] = convert_currency(
        order_items["freight_value"]
    )

    return order_items

#PAYEMENTS
def moroccanize_payments(payments: pd.DataFrame):

    payments = payments.copy()

    payments["payment_type"] = (
        payments["payment_type"]
        .map(PAYMENT_MAPPING)
        .fillna("Bank Card")
    )

    payments["payment_value"] = convert_currency(
        payments["payment_value"]
    )

    return payments

#CATEGORIES
def moroccanize_categories(categories: pd.DataFrame):

    categories = categories.copy()

    categories["product_category_name_english"] = (
        categories["product_category_name_english"]
        .map(CATEGORY_MAPPING)
        .fillna(
            categories["product_category_name_english"]
        )
    )

    return categories


# PRODUCTS
def moroccanize_products(
    products: pd.DataFrame,
    categories: pd.DataFrame
):

    products = products.copy()

    category_dict = dict(
        zip(
            categories["product_category_name"],
            categories["product_category_name_english"]
        )
    )

    products["product_category_name"] = (
        products["product_category_name"]
        .map(category_dict)
    )

    return products

#VALIDATION
def validate_output(raw_df, transformed_df, name):
    if len(raw_df) != len(transformed_df):
        raise ValueError(
            f"{name}: row count mismatch."
        )

    print(f"✓ {name} validated ({len(raw_df):,} rows)")



#PIPELINE
# ==========================================================
# PIPELINE
# ==========================================================

def run_moroccanization():

    log_transformation("Loading datasets...")

    customers = load_csv(RAW_DATA / CUSTOMERS_FILE)
    orders = load_csv(RAW_DATA / ORDERS_FILE)
    order_items = load_csv(RAW_DATA / ORDER_ITEMS_FILE)
    payments = load_csv(RAW_DATA / PAYMENTS_FILE)
    products = load_csv(RAW_DATA / PRODUCTS_FILE)
    sellers = load_csv(RAW_DATA / SELLERS_FILE)
    reviews = load_csv(RAW_DATA / REVIEWS_FILE)
    geolocation = load_csv(RAW_DATA / GEOLOCATION_FILE)
    categories = load_csv(RAW_DATA / CATEGORY_TRANSLATION_FILE)

    log_transformation("Applying Moroccanization...")

    customers_m = moroccanize_customers(customers)
    sellers_m = moroccanize_sellers(sellers)
    orders_m = moroccanize_orders(orders)
    order_items_m = moroccanize_order_items(order_items)
    payments_m = moroccanize_payments(payments)
    geolocation_m = moroccanize_geolocation(geolocation)
    categories_m = moroccanize_categories(categories)
    products_m = moroccanize_products(
        products,
        categories_m
    )

    log_transformation("Running validation...")

    validate_output(customers, customers_m, "Customers")
    validate_output(orders, orders_m, "Orders")
    validate_output(order_items, order_items_m, "Order Items")
    validate_output(payments, payments_m, "Payments")
    validate_output(products, products_m, "Products")
    validate_output(sellers, sellers_m, "Sellers")
    validate_output(reviews, reviews, "Reviews")
    validate_output(geolocation, geolocation_m, "Geolocation")
    validate_output(categories, categories_m, "Categories")

    log_transformation("Saving processed datasets...")

    save_csv(customers_m, PROCESSED_DATA / OUTPUT_CUSTOMERS)
    save_csv(orders_m, PROCESSED_DATA / OUTPUT_ORDERS)
    save_csv(order_items_m, PROCESSED_DATA / OUTPUT_ORDER_ITEMS)
    save_csv(payments_m, PROCESSED_DATA / OUTPUT_PAYMENTS)
    save_csv(products_m, PROCESSED_DATA / OUTPUT_PRODUCTS)
    save_csv(sellers_m, PROCESSED_DATA / OUTPUT_SELLERS)
    save_csv(reviews, PROCESSED_DATA / OUTPUT_REVIEWS)
    save_csv(geolocation_m, PROCESSED_DATA / OUTPUT_GEOLOCATION)
    save_csv(categories_m, PROCESSED_DATA / OUTPUT_CATEGORIES)

    log_transformation("Moroccanization completed successfully.")

#MAIN
if __name__ == "__main__":
    run_moroccanization()