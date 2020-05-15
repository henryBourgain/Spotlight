import bpy

# Create a property group
class AddonGroup(bpy.types.PropertyGroup):
    
    name: bpy.props.StringProperty(default='Light')  # Create a property of type "String"
    intensity: bpy.props.FloatProperty(
        default=10.0,
        unit='POWER'
    )
    light_type: bpy.props.EnumProperty(
        items=[
            ('SUN', 'sun', ''),
            ('SPOT', 'spot', ''),
            ('AREA', 'area', '')
        ]
    )

#  Get the property group "spotlight" who contains properties: name, intensity, light_type
def get_props():
    return bpy.context.scene.spotlight



def register():
    bpy.utils.register_class(AddonGroup)
    bpy.types.Scene.spotlight = bpy.props.PointerProperty(type=AddonGroup)

def unregister():
    bpy.utils.unregister_class(AddonGroup)
    del bpy.types.Scene.spotlight