# variables for database and url configuration
from config import Config

from supabase import SupabaseClient, create


class SupabaseDB:
    """
    class instance for database connection to supabase

    :str: url: configuration for database url for data inside supafast project
    :str: key: configuration for database secret key for authentication
    :object: supabase: Supabase instance for connection to database environment
    """

    url: str = Config.URL
    key: str = Config.KEY
    supabase: SupabaseClient = create(url, key)
