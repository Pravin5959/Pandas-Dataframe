'''
Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store1      | int     |
| store2      | int     |
| store3      | int     |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
If the product is not available in a store, the price will be null in that store's column.

Write a solution to rearrange the Products table so that each row has (product_id, store, price). If a product is not available in a store, do not include a row with that product_id and store combination in the result table.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input: 
Products table:
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |
+------------+--------+--------+--------+
Output: 
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 0          | store1 | 95    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store1 | 70    |
| 1          | store3 | 80    |
+------------+--------+-------+
Explanation: 
Product 0 is available in all three stores with prices 95, 100, and 105 respectively.
Product 1 is available in store1 with price 70 and store3 with price 80. The product is not available in store2.

pandas schema :
data = [[0, 95, 100, 105], [1, 70, None, 80]]
products = pd.DataFrame(data, columns=['product_id', 'store1', 'store2', 'store3']).astype({'product_id':'int64', 'store1':'int64', 'store2':'int64', 'store3':'int64'})

Explanation:
Step1 : Rearrangement of dataframe can be done in two ways in PANDAS, by using PIVOT (Columanize) or MELT(Row Extension)
Step2 : We need to extend the rows based apon the dataframe columns, so we will use melt, it takes two main arguments i.e. id_vars 
        which will be present as column itself from the existing to new dataframe, value_vars which takes the list of columns from 
        existing dataframe and convert them in rows, finally the data inside the existing dataframe will be considered as values

Please find refrence for MELT function : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html
'''

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return pd\
             .melt(products,\
                   id_vars = ['product_id'],\
                   value_vars = ['store1', 'store2', 'store3'],\
                   var_name = 'store',\
                   value_name = 'price')\
             .dropna()
