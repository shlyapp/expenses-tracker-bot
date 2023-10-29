from typing import List

from database.db import fetchall


class Categories:
    def __init__(self):
        self._categories = self._load_categories()

    def _load_categories(self) -> List[str]:
        categories_raw = fetchall("category", "name".split())
        categories = []
        for category in categories_raw:
            categories.append(str(category['name']))
        return categories

    def get_all_category(self):
        return self._categories
