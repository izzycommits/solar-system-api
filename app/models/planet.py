from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from typing import Optional

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] 
    description: Mapped[str]
    number_moons: Mapped[Optional[int]]
    color: Mapped[Optional[str]]

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            number_moons=self.number_moons,
            color=self.color
        )
    
    @classmethod
    def from_dict(cls, planet_data): 
        return cls(
            name=planet_data["name"], 
            color=planet_data["color"], 
            description=planet_data["description"], 
            number_moons=planet_data["number_moons"]
        )
