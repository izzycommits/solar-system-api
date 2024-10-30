# place in a top-level file. call it something like seed.py
# no need to dwell on the `with my_app.app_context():`, other than to say
# that the `db` reference won't work unless it runs with an app context

from app import create_app, db
from app.models.planet import Planet

my_app = create_app()
with my_app.app_context():
    db.session.add(Planet(name="Mercury", description="The smallest planet")),
    db.session.add(Planet(name="Venus", description="Our closest neighbor")),
    db.session.add(Planet(name="Earth", description="The green planet")),
    db.session.add(Planet(name="Mars", description="The red planet")),
    db.session.add(Planet(name="Jupiter", description="The largest planet")),
    db.session.add(Planet(name="Saturn", description="A gas giant")),
    db.session.add(Planet(name="Uranus", description="A sideways planet")),
    db.session.add(Planet(name="Neptune", description="Has super sonic winds")),
    db.session.add(Planet(name="Pluto", description="The dwarf planet")),
    db.session.commit()