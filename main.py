# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# STEP 2
# Replace None with your code
df_first_five = pd.read_sql(
    """
        SELECT employeeNumber,lastName
        FROM employees;
    """,
    conn,
)


# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql(
    """
        SELECT
        lastName,employeeNumber
        FROM employees;
    """,
    conn,
)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql(
    """
        SELECT 
        employeeNumber as ID, lastName 
        FROM employees;
    """,
    conn,
)


# STEP 5
# Replace None with your code
df_executive = pd.read_sql(
    """
    SELECT 
    CASE
        WHEN jobTitle = 'President' or jobTitle = 'VP Sales' or jobTitle = 'VP Marketing' THEN 'Executive'
        ELSE 'Not Executive'
    END as role
    FROM employees;
    """,
    conn,
)

# print(df_executive)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql(
    """
        SELECT 
        length(lastName) as name_length
        FROM employees;
   """,
    conn,
)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql(
    """
    SELECT 
    SUBSTRING(jobTitle, 1,2) as short_title
    FROM employees;
    """,
    conn,
)


# order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
# print("------------------Order Details Data------------------")
# print(order_details)
# print("----------------End Order Details Data----------------")

# STEP 8
# Replace None with your code
sum_total_price = (
    pd.read_sql(
        """
    SELECT ROUND(quantityOrdered * priceEach) AS total_price 
    FROM orderDetails
    """,
        conn,
    )
    .sum()
    .values
)

print(sum_total_price)

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql(
    """
    SELECT 
        orderDate,
        strftime('%d', orderDate) AS day,
        strftime('%m', orderDate) AS month,
        strftime('%Y', orderDate) AS year
    FROM orders
    """,
    conn,
)
