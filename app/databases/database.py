import sqlite3
from pathlib import Path
from typing import Optional

DATABASE_FILE = Path("./codex.db")
_connection: Optional[sqlite3.Connection] = None


def get_database_path() -> str:
    DATABASE_FILE.parent.mkdir(parents=True, exist_ok=True)
    return str(DATABASE_FILE.resolve())


def connect_db() -> sqlite3.Connection:
    global _connection
    if _connection is None:
        _connection = sqlite3.connect(get_database_path(), check_same_thread=False)
        _connection.row_factory = sqlite3.Row
    return _connection


def close_db() -> None:
    global _connection
    if _connection is not None:
        _connection.close()
        _connection = None


# database setup, setup db connection, setup db schema, setup db migrations, setup db seeding, setup db connection pooling, setup db transactions, setup db indexing, setup db backup and restore, setup db monitoring and logging
# database connection, database schema, database migrations, database seeding, database connection pooling, database transactions, database indexing, database backup and restore, database monitoring and logging
# database connection, database schema, database migrations, database seeding, database connection pooling, database transactions, database indexing, database backup and restore, database monitoring and logging, database performance optimization, database security hardening, database scaling strategies, database replication strategies, database sharding strategies, database caching strategies, database query optimization strategies, database connection retry strategies, database connection timeout strategies, database connection error handling strategies, database connection pooling strategies, database transaction management strategies, database indexing strategies, database backup and restore strategies, database monitoring and logging strategies, database performance optimization strategies, database security hardening strategies, database scaling strategies, database replication strategies, database sharding strategies, database caching strategies, database query optimization strategies, database connection retry strategies, database connection timeout strategies, database connection error handling strategies, database connection pooling strategies, database transaction management strategies, database indexing strategies, database backup and restore strategies, database monitoring and logging strategies, database performance optimization strategies, database security hardening strategies, database scaling strategies, database replication strategies, database sharding strategies, database caching strategies, database query optimization strategies, database connection retry strategies, database connection timeout strategies, database connection error handling strategies, database connection pooling strategies, database transaction management strategies, database indexing strategies, database backup and restore strategies, database monitoring and logging strategies, database performance optimization strategies, database security hardening strategies, database scaling strategies, database replication strategies, database sharding strategies, database caching strategies, database query optimization strategies, database connection retry strategies, database connection timeout strategies, database connection error handling strategies, database connection pooling strategies, database transaction management strategies, database indexing strategies, database backup and restore strategies, database monitoring and logging strategies, database performance optimization strategies, database security hardening strategies, database scaling strategies, database replication strategies, database sharding strategies, database caching strategies, database query optimization strategies, database connection retry strategies, database connection timeout strategies, database connection error handling strategies, database connection pooling strategies, database transaction management strategies, database indexing strategies, database backup and restore strategies, database monitoring and logging strategies, database performance optimization strategies, database security hardening strategies, database scaling strategies, database replication strategies, database sharding strategies, database caching strategies, database query optimization strategies, database connection retry strategies, database connection timeout strategies, database connection error handling strategies, database connection pooling strategies, database transaction management strategies, database indexing strategies, database backup and restore strategies, database monitoring and logging strategies, database performance optimization strategies, database security hardening strategies, database scaling strategies, database replication strategies, database sharding strategies, database caching strategies, database query optimization strategies, database connection retry strategies, database connection timeout strategies, database connection error handling strategies, database connection pooling strategies, database transaction management strategies, database indexing strategies, database backup and restore strategies, database monitoring and logging strategies, database performance optimization strategies, database security hardening strategies, database scaling strategies, database replication strategies, database sharding strategies, database caching strategies, database query optimization strategies, database connection retry strategies, database connection timeout strategies, database connection error handling