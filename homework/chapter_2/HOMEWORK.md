## Exercises
1. Sellers (name) who have sold at least one of the top 10 selling parts (use CTE)

Solution:
```
 ```
%%sql

WITH seller_stats AS (
    SELECT 
        s.s_name AS seller_name,
        p.p_name AS part_name,
        SUM(l.l_quantity) AS part_total
    FROM prod.db.lineitem l
    JOIN prod.db.partsupp ps
    ON l.l_partkey = ps.ps_partkey AND l.l_suppkey = ps.ps_suppkey
    JOIN prod.db.supplier s
    ON ps.ps_suppkey = s.s_suppkey
    JOIN prod.db.part p
    ON ps.ps_partkey = p.p_partkey
    GROUP BY p.p_name, s.s_name
    ORDER BY part_total DESC
    LIMIT 10
)
SELECT seller_name
FROM seller_stats        
GROUP BY seller_stats.seller_name
```
