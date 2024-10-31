from flask import Blueprint, abort, make_response, request
from ..db import db
from app.models.planet import Planet
# from app.models.planet import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    number_moons = request_body["number_moons"]
    color = request_body["color"]

    new_planet = Planet(name=name, description=description,number_moons=number_moons,color=color)

    db.session.add(new_planet)
    db.session.commit()

    response = new_planet.to_dict()
    return response, 201

@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet)
    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    number_moons_param = request.args.get("number_moons")  
    if number_moons_param:
        query = query.where(Planet.number_moons >= 95 ) 

    query=query.order_by(Planet.id)
    planets = db.session.scalars(query)
    planets_response = [planet.to_dict() for planet in planets]
    
    return planets_response

    
@planets_bp.get("/<planet_id>")
def get_single_planet(planet_id):
    planet = validate_planet(planet_id)

    return planet.to_dict()

# @planets_bp.put("/<planet_id>")
# def update_planet(planet_id):
#     pass
    # request_body = request.get_json()

    # planet.name = request

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError: 
        abort(make_response({"message":f"Planet id {planet_id} is invalid"}, 400))

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        abort(make_response({"message":f"Planet id {planet_id} is not found"}, 404))

    return planet


# @planets_bp.get("")
# def get_all_planets():
#     planets_response = []
#     for planet in planets: 
#         planets_response.append(planet.to_dict())   
#     return planets_response

# @planets_bp.get("/<planet_id>")
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)
#     return planet.to_dict(), 200

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError: 
#         abort(make_response({"message":f"Planet id {planet_id} is invalid"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"message":f"Planet id {planet_id} is not found"}, 404))