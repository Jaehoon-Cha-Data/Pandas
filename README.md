# Pandas
 Pandas


# df

| | name | grade | hours | 
| --- | --- |---|--- |
| 0  | A | 50 | 1 |
| 1  | B | 60 | 2 |
| 2  | C | 90 | 7 |

# df.columns 
Index(['name', 'grade', 'hours'], dtype='object')

# df.head(2)
read first n columns, default is 5

| | name | grade | hours | 
| --- | --- |---|--- |
| 0  | A | 50 | 1 |
| 1  | B | 60 | 2 |

# df.tail(2), default is 5
read last n columns, default is 5

| | name | grade | hours | 
| --- | --- |---|--- |
| 1  | B | 60 | 2 |
| 2  | C | 90 | 7 |


# df['name']
read specific column

| | name | 
| --- | --- |
| 0  | A | 
| 1  | B | 
| 2  | C |



| 0  | A | 
| 1  | B | 
| 2  | C |
