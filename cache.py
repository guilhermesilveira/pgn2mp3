import hashlib
import os

class Cache:
    def __init__(self, cache_path:str):
        self.cache_path = cache_path
        # create folders to cache path
        os.makedirs(self.cache_path, exist_ok=True)
    
    def get(self, key, extension):
        # if file with key name exists, return its path
        # otherwise, return None
        file_path = self.get_key_path(key, extension)
        if os.path.exists(file_path):
            return file_path
        return None

    def check_dir(self, path):
        os.makedirs(f"{self.cache_path}/{path}", exist_ok=True)
    
    def get_key_path(self, key, extension):
        return f"{self.cache_path}/{key}.{extension}"
