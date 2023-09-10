''' Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee. 

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

The result format is in the following example.

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+

Pandas Schema = data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['Id', 'Salary']).astype({'Id':'Int64', 'Salary':'Int64'})

Explanation : We need to find Nth highest salary where N is a dynamic argument from the input
Step1 : We will have to create a rank column which will rank the salaries of each employee in a descending order, we use rank function on dataframes to apply ranking and store in
        a new column
Step2 : We will have to filter the data based upon rank, where rank is equal to N
Step3 : Finally we will have to apply distinct on top of filtered data, as it can happen the Nth salary is same for more than 1 employee

Note : The column name wrt each N value should be dynamic as well, so while applying rename function I have concatednated string with N value
'''

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee['rank'] = employee\
                                .salary\
                                .rank(method = 'dense', ascending = False)\
                                .astype(int)
    result = employee[employee['rank'] == N]
    return result[['salary']]\
                              .drop_duplicates()\
                              .rename(columns = {'salary' : ''.join(['getNthHighestSalary(',str(N),')'])})
