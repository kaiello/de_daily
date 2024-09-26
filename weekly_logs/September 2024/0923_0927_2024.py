# 09_26_2024.py 

#  Extract database names from a string of database paths.

# String of database paths to delete, separated by new lines. Some have additional prefixes.
databases_to_delete = """s3://datasource/database1/table1
s3://datasource/database1/table2
s3://datasource/database2/table1
s3://datasource/database2/table2
s3://datasource/database3/table1
s3://datasource/database3/table2
s3://datasource/database3/table2
s3://datasource/delta/database3/table1
s3://datasource/delta/database4/table1
"""

# Split the string into a list of databases and tables.
tables_to_delete_list = databases_to_delete.split("\n")

# print(tables_to_delete_list)

# Create lists to store the database names and table names.
# db_names = [path.split("/")[-2] for path in tables_to_delete_list]
table_names = [path.split("/")[-1] for path in tables_to_delete_list]

# print(db_names)
# # print(table_names)