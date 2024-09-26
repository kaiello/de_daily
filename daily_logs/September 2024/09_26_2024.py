# I had a string of databases from that I needed to extract the names of the databases from. I used the split method to split the string into a list of databases. I then used a for loop to iterate through the list and print out the names of the databases. I also used the strip method to remove any leading or trailing whitespace from the database names.

# String of databases paths to delete.Notice all the strings are separated by a new line. Also, the strings were not all formatted exactly the same. Some had additional prefixes at the end of the string.
databases_to_delete = """s3://database1.table1
s3://database1.table2
s3://database2.table1
s3://database2.table2
s3://database3.table1
s3://database3.table2
s3://database3.table2
s3://delta/database3.table1
s3://delta/database4.table1
"""

# Split the string into a list of databases and tables.
tables_to_delete_list = databases_to_delete.split("\n")

# Create lists to store the database names and table names.
db_names = [path.split("/")[-2] for path in tables_to_delete_list]
table_names = [path.split("/")[-1] for path in tables_to_delete_list]


