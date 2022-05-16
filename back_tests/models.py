class Category:
    def __init__(self, category_id: int, category_name: str):
        self.id = category_id
        self.name = category_name


class Tag:
    def __init__(self, tag_id: int, tag_name: str):
        self.id = tag_id
        self.name = tag_name


class Pet:
    def __init__(self, pet_id: int, category: Category = None, name: str = None, photo_urls: list = None,
                 tags: list = None, status: str = None):
        self.id = pet_id
        self.category = category if category is None else category.__dict__
        self.name = name
        self.photoUrls = photo_urls
        self.tags = tags if tags is None else [tag.__dict__ for tag in tags]
        self.status = status
