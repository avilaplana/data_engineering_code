## Exercises
1. Write a query on the orders table that has the following output:
- order_month,
- o_custkey,
- total_price,
- three_mo_total_price_avg
- consecutive_three_mo_total_price_avg: The consecutive 3 month average
   of total_price for that customer. Note that this should only include months that
   are chronologically next to each other.
   
Hint: Use CAST(strftime(o_orderdate, '%Y-%m-01') AS DATE) to cast order_month to
date format.

Hint: Use the INTERVAL format shown above to construct the window function to compute
   consecutive_three_mo_total_price_avg column.

Solution:
```
%%sql

WITH orders_with_order_month AS (
    SELECT 
        o_custkey,
        o_totalprice,
        trunc(o_orderdate, 'MM') AS order_month
    FROM prod.db.orders
    ), order_total_price_month AS (
        SELECT 
            o_custkey,
            order_month,
            SUM(o_totalprice) AS month_totalprice
        FROM orders_with_order_month
        GROUP BY o_custkey, order_month        
    )

SELECT 
    order_month,
    o_custkey,
    month_totalprice,
    AVG(month_totalprice) OVER (PARTITION BY o_custkey ORDER BY order_month ROWS BETWEEN 3 PRECEDING AND CURRENT ROW) AS three_mo_total_price_avg,
    AVG(month_totalprice) OVER (PARTITION BY o_custkey ORDER BY order_month RANGE BETWEEN INTERVAL 2 MONTHS PRECEDING AND CURRENT ROW) AS consecutive_three_mo_total_price_avg
FROM order_total_price_month
```

2. From the orders table get the 3 lowest spending customers per day

Hint: Figure out the PARTITION BY column first, then the ORDER BY column and finally the
FUNCTION to use to compute running average.

Solution:
```
%%sql
WITH order_customer_per_date AS (
    SELECT 
     o_custkey,
     o_orderdate,
     COUNT(1) AS num_transaction_date,
     SUM(o_totalprice) AS total_price_date
    FROM prod.db.orders
    GROUP BY o_custkey, o_orderdate
), rank_customer AS (
    SELECT 
       o_custkey,
       o_orderdate,
       total_price_date,
       ROW_NUMBER() OVER (PARTITION BY o_orderdate ORDER BY total_price_date ASC) AS row_num  
    FROM order_customer_per_date
)

SELECT 
    * 
FROM rank_customer
WHERE row_num <= 3
```

3. Write a SQL query using the orders table that calculates the following columns:
- o_orderdate: From orders table
- o_custkey: From orders table
- o_totalprice: From orders table
- totalprice_diff: The customers current day’s o_totalprice - that same customers
most recent previous purchase’s o_totalprice

Hint: Start by figuring out what the PARTITION BY column should be, then what the ORDER
BY column should be, and then finally the function to use.

Hint: Use the LAG(column_name) ranking function to identify the prior day’s revenue.

Solution:
```
%%sql
WITH order_customer_per_date AS (
    SELECT 
     o_custkey,
     o_orderdate,
     COUNT(1) AS num_transaction_date,
     SUM(o_totalprice) AS total_price_date
    FROM prod.db.orders
    GROUP BY o_custkey, o_orderdate
), order_with_previous_purchase_enriched AS (
    SELECT 
        o_custkey,
        o_orderdate,
        total_price_date,
        LAG(total_price_date) OVER (PARTITION BY o_custkey ORDER BY o_orderdate) AS total_price_date_previous
    FROM order_customer_per_date
)
SELECT 
    *, 
    ABS(total_price_date - COALESCE(total_price_date_previous, 0)) AS totalprice_diff
    FROM order_with_previous_purchase_enriched
ORDER BY o_custkey,o_orderdate

```