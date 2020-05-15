"""
    This module contains tools to create light (docstring)
"""


import bpy



def main(name, power, coll, light_type): 
    """
        Create spotlight
    """

    target_object = bpy.context.object
    
    # Create spot
    spot_obj = create_spot_object(name, power, coll, light_type)
    
    # Place spot
    place_spot_object(spot_obj, target_object)
    
    # Add contrain to the spot
    create_track_constraint(spot_obj, target_object)
    
    
def create_spot_object(name, power, coll, light_type):
    
    # Create data
    spot_data = bpy.data.lights.new(name + "_data", light_type)
    
    # Change value of energy
    spot_data.energy = power
    
    # Create object
    spot_obj = bpy.data.objects.new(name, spot_data)
    
    # Link to scene collection
    coll.objects.link(spot_obj)
    
    return spot_obj


def place_spot_object(spot_obj, target_obj):
    
    # Translation of 4 on the Z axis
    spot_obj.location = target_obj.location    
    spot_obj.location.z = target_obj.location.z + 6


def create_track_constraint(spot_obj, target_object):
    
    # Create constraint type 'Track to'
    constr = spot_obj.constraints.new('TRACK_TO')
    
    # Set Target on choosen object
    constr.target = target_object
    
    # Set axis constraint To -Z
    constr.track_axis = 'TRACK_NEGATIVE_Z'
    
    # Set axis constraint Up Y
    constr.up_axis = 'UP_Y' 
