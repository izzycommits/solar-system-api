from flask import Blueprint, abort, make_response
# from app.models.planet import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")



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


