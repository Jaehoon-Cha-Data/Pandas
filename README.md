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


# df.set_index('name', inplace = True)
set name column to index

|  | grade | hours | 
| --- |---|--- |
| name | | |
| A   | 50 | 1 |
| B  | 60 | 2 |
| C  | 90 | 7 |

# df.reset_index(level=0, inplace = True)
index to column

| | name | grade | hours | 
| --- | --- |---|--- |
| 0  | A | 50 | 1 |
| 1  | B | 60 | 2 |
| 2  | C | 90 | 7 |

# df.index = [2,3,4]
set a new index list

| | name | grade | hours | 
| --- | --- |---|--- |
| 2  | A | 50 | 1 |
| 3  | B | 60 | 2 |
| 4  | C | 90 | 7 |

# df.reset_index(drop = True, inplace = True)
index begins from 0

| | name | grade | hours | 
| --- | --- |---|--- |
| 0  | A | 50 | 1 |
| 1  | B | 60 | 2 |
| 2  | C | 90 | 7 |
