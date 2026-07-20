"""
Global configuration for the Moroccan E-Commerce Data Platform.
"""

from pathlib import Path


# PROJECT PATHS


PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA = PROJECT_ROOT / "data" / "raw"
INTERIM_DATA = PROJECT_ROOT / "data" / "interim"
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"

ASSETS = PROJECT_ROOT / "assets"

LOGS = PROJECT_ROOT / "logs"


# FILE NAMES


CUSTOMERS_FILE = "olist_customers_dataset.csv"
ORDERS_FILE = "olist_orders_dataset.csv"
ORDER_ITEMS_FILE = "olist_order_items_dataset.csv"
PAYMENTS_FILE = "olist_order_payments_dataset.csv"
PRODUCTS_FILE = "olist_products_dataset.csv"
SELLERS_FILE = "olist_sellers_dataset.csv"
REVIEWS_FILE = "olist_order_reviews_dataset.csv"
GEOLOCATION_FILE = "olist_geolocation_dataset.csv"
CATEGORY_TRANSLATION_FILE = "product_category_name_translation.csv"


# OUTPUT FILES


OUTPUT_CUSTOMERS = "customers.csv"
OUTPUT_ORDERS = "orders.csv"
OUTPUT_ORDER_ITEMS = "order_items.csv"
OUTPUT_PAYMENTS = "payments.csv"
OUTPUT_PRODUCTS = "products.csv"
OUTPUT_SELLERS = "sellers.csv"
OUTPUT_REVIEWS = "reviews.csv"
OUTPUT_GEOLOCATION = "geolocation.csv"
OUTPUT_CATEGORIES = "categories.csv"


# MOROCCANIZATION SETTINGS


# Fixed exchange rate used throughout the project
BRL_TO_MAD = 2.10

# Move dataset from 2017 → 2025
YEAR_OFFSET = 8

# Used whenever random values are generated
RANDOM_SEED = 42

# Moroccan ZIP code range
ZIP_MIN = 10000
ZIP_MAX = 99999

# Morocco latitude range
LAT_MIN = 21.0
LAT_MAX = 36.0

# Morocco longitude range
LON_MIN = -17.0
LON_MAX = -1.0