# config.py

DB_CONFIG = {
    "db_type": "postgresql",
    "user": "aieng_onl_en_290626_honey_layers",
    "password": "mialovesicecream",
    "host": "ds-sql-playground.c8g8r1deus2v.eu-central-1.rds.amazonaws.com",
    "port": "5432",
    "database": "postgres"
}

CONNECTION_STR = f"{DB_CONFIG['db_type']}://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"