import psycopg2
import os
import sys

from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host="aws-0-us-east-1.pooler.supabase.com",
        port=5432,
        database="postgres",
        user="postgres.rzbwjavzsmpbkygilhfo",
        password="43759816JACK7",
        sslmode="require"
    )