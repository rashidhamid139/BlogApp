from django.db import connection
cursor  =connection.cursor()
cursor.execute("truncate table blog_like")