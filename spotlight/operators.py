import bpy
from . import Lamp_target, properties


class AddSpot(bpy.types.Operator):

    bl_idname = 'spotlight.add_spot'
    bl_label = 'Operator'

    # Method called to say what to do when the operator is called
    def execute(self, context):

        props = properties.get_props()
    
        if context.object: 

            if not props.name:
                props.name = 'Light'

            energy = props.intensity

            if props.light_type == 'SUN':
                energy /= 100

            Lamp_target.main(props.name, energy, context.collection, props.light_type)
            self.report({'INFO'}, 'chaine de caractere farouche')

            # Wait for a "set" like {'FINISHED'}, {'CANCELLED'} or else
            return {'FINISHED'}

        else:

            self.report({'ERROR'}, 'Select 1 object') 
            # No need to do Ctr Z many times after several executions
            return {'CANCELLED'}   


def register():
    bpy.utils.register_class(AddSpot)


def unregister():
    bpy.utils.unregister_class(AddSpot)
