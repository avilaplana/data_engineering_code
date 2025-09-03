## Exercises
1. Write a query that shows the number of items returned for each region name

Solution:
```
%%sql
    
SELECT 
    r.r_name AS region_name,
    SUM(l.l_quantity) AS return_item_total
FROM prod.db.lineitem l
JOIN prod.db.partsupp ps
ON l.l_partkey = ps.ps_partkey AND l.l_suppkey = ps.ps_suppkey
JOIN prod.db.supplier s
ON ps.ps_suppkey = s.s_suppkey
JOIN prod.db.nation n
ON s.s_nationkey = n.n_nationkey    
JOIN prod.db.region r
ON n.n_regionkey = r.r_regionkey
WHERE l.l_shipinstruct = 'TAKE BACK RETURN'   
GROUP BY r.r_name 
 
```
2. List the top 10 most selling parts (part name)

Solution:
```
%%sql

SELECT 
    p.p_name AS part_name,
    SUM(l.l_quantity) AS item_total
FROM prod.db.lineitem l
JOIN prod.db.partsupp ps
ON l.l_partkey = ps.ps_partkey -- AND l.l_suppkey = ps.ps_suppkey
JOIN prod.db.part p
ON ps.ps_partkey = p.p_partkey
GROUP BY p.p_name
ORDER BY item_total DESC
LIMIT 10
```

3. Sellers (name) who have sold at least one of the top 10 selling parts

Solution:
```
%%sql
SELECT 
        s.s_name AS supplier_name, 
        SUM(l.l_quantity) AS item_total
FROM prod.db.lineitem l
JOIN prod.db.partsupp ps
ON l.l_partkey = ps.ps_partkey AND l.l_suppkey = ps.ps_suppkey
JOIN prod.db.supplier s
ON ps.ps_suppkey = s.s_suppkey
GROUP BY s.s_name, ps.ps_partkey
ORDER BY item_total DESC
LIMIT 10
```

4. Number of items returned for each order price bucket. The definition of order price
bucket is shown below.
```
CASE
    WHEN o_totalprice > 100000 THEN 'high'
    WHEN o_totalprice BETWEEN 25000 AND 100000 THEN 'medium'
    ELSE 'low'
END AS order_price_bucket
```

Solution:
```
%%sql
SELECT o.order_price_bucket,
       SUM(l.l_quantity) AS return_item_total
FROM     
    (SELECT 
    o_orderkey,
    CASE
        WHEN o_totalprice > 100000 THEN 'high'
        WHEN o_totalprice BETWEEN 25000 AND 100000 THEN 'medium'
        ELSE 'low'
END AS order_price_bucket
FROM prod.db.orders) AS o
JOIN prod.db.lineitem l
ON o.o_orderkey = l.l_orderkey
WHERE l.l_shipinstruct = 'TAKE BACK RETURN'   
GROUP BY o.order_price_bucket
ORDER BY return_item_total DESC
```
5. Average time (in days) between receiptdate and shipdate for each nation (name)

Solution:
```
%%sql
SELECT 
    n.n_name AS name,
    AVG(l.days) as avg_day
FROM    
    (SELECT 
        l.l_partkey, 
        l.l_suppkey,
        DATEDIFF(l.l_receiptdate, l.l_shipdate) AS days
    FROM prod.db.lineitem l) AS l
JOIN prod.db.partsupp ps
ON l.l_partkey = ps.ps_partkey AND l.l_suppkey = ps.ps_suppkey
JOIN prod.db.supplier s
ON ps.ps_suppkey = s.s_suppkey
JOIN prod.db.nation n
ON s.s_nationkey = n.n_nationkey    
GROUP BY n.n_name
ORDER BY avg_day DESC
```
