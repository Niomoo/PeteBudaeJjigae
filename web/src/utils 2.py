import pymysql
from dbutils.pooled_db import PooledDB

POOL = PooledDB(
    creator = pymysql,
    maxconnections = 0, 
    mincached = 2,
    maxcached = 0,
    maxshared = 1,
    blocking = True,
    maxusage = None,
    setsession = [],
    ping = 0,
    host = 'remotemysql.com',
    port = 3306,
    user = '7laUVxPtp9',
    password = 'JBjmPdUTTM',
    database = '7laUVxPtp9',
)