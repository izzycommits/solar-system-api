import uuid

class Planet: 
    def __init__(self, id, name, description): 
        # id = int(uuid.uuid4()) if not id else id
        self.id = id
        self.name = name
        self.description = description 


planets = [
    Planet(1, "Mars", "The red planet"),
    Planet(2, "Earth", "The green planet"), 
    Planet(3, "Jupiter", "The largest planet")
]
