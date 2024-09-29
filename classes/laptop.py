from classes.product import Product

class Laptop(Product):
    def __init__(self, id=None, name=None, url=None, processor_name=None, processor_brand=None, 
                 ram_capacity=None, storage_type=None, storage_capacity=None, screen_size=None, reviews=None):
        self.id = id
        self.name = name
        self.url = url
        self.processor_brand = processor_brand
        self.processor_name = processor_name
        self.ram_capacity = ram_capacity
        self.storage_type = storage_type
        self.storage_capacity = storage_capacity
        self.screen_size = screen_size
        self.reviews = reviews
    
    def features_to_md_text(self):
        return f"""
        **Laptop ID**: {self.id} 
        **Laptop Name**: {self.name} 
        **Processor Brand**: {self.processor_brand}  
        **Processor Name**: {self.processor_name}  
        **RAM**: {self.ram}  
        **Storage Type**: {self.storage_type}  
        **Screen Size**: {self.screen_size}  
        **Storage Capacity**: {self.storage_capacity}
        """.strip()

     