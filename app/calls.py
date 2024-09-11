from data import conn
import sys
# add other folders to path for easy access of functions and variables.
sys.path.insert(0, '/Users/willd/PyCharmProjects/storeStats/data')

import pandas as pd

# pulls the total sales based on each age group.
salesByAge = pd.read_sql("SELECT sum(sales), age from customer JOIN sales ON"
                         " customer.customer_id = sales.customer_id group by age order by age", con=conn.engine)
print(salesByAge)

# products that have the highest discount.
ProductsWithMostDiscount = pd.read_sql("SELECT count(product.product_id), discount FROM product JOIN sales ON"
                                       " product.product_id = sales.product_id GROUP BY discount ORDER BY discount DESC", con=conn.engine)
ProductsWithMostDiscount


# Finds the most popular shopping category based on age.
MostPopularCatByAge = pd.read_sql("SELECT age, category FROM (SELECT age, category, ROW_NUMBER() OVER (PARTITION BY age) AS row_number"
                                  " FROM (SELECT COUNT(category) as pcount ,category, age FROM customer JOIN sales ON customer.customer_id = sales.customer_id JOIN product ON"
                                  " sales.product_id = product.product_id GROUP BY age, category ORDER by age)) WHERE row_number = 1 ORDER BY age", con=conn.engine)
MostPopularCatByAge