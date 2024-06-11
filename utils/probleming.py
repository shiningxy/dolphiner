# Description: This file contains the functions that are used to solve the problems
# Contains the following functions:
# - get_ship_potential_optimizations: Get the potential optimizations of the ship


import json


def get_ship_potential_optimizations(mmsi: int) -> str:
    """Get the potential optimizations of the ship.

    This function reads the potential optimizations of the ship from a JSON file and returns it as a string.

    Tips:
        Ship can sailing as low speed as possible to save fuel, but it will take more time to reach the destination.
        Ship also can sailing as high speed as possible to save time, but it will consume more fuel.
        After each waypoint of the ship, the ship can adjust the speed.
        So, the potential optimizations of the ship are the potential speed of the ship at each waypoint.
        Therefore, many potential optimizations can be generated directly for the ship.

    Args:
        mmsi (int): The MMSI (Maritime Mobile Service Identity) of the ship.

    Returns:
        str: A string containing the potential optimizations of the ship in JSON format.
    """
    with open("data/potential_optimizations.json") as file:
        data = json.load(file)
        return json.dumps(data[mmsi])
