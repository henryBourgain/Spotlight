import bpy
from . import Lamp_target


class AddSpot(bpy.types.Operator):

    bl_idname = 'spotlight.add_spot'
    bl_label = 'Ma gross BIte'

    name = bpy.props.StringProperty()
    intensity = bpy.props.FloatProperty()
    light_type = bpy.props.EnumProperty(
        items=[
            ('SUN', 'sun', ''),
            ('SPOT', 'spot', ''),
            ('AREA', 'area', ''),
        ]
    )
    

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True  # Align
        layout.use_property_decorate = False
        layout.prop(self, 'name', text='Spot Name')
        layout.prop(self, 'intensity', text='Intensity')
        layout.prop(self, 'light_type', text='Light Type')


    # Methode pour dire ce qu'on fait quand on appel l'operateur
    def execute(self, context):

        if context.object:

            Lamp_target.main(self.name, self.intensity, context.collection, self.light_type)
            self.report({'INFO'}, 'chaine de caractere farouche')

            # Il attend un set comme {'FINISHED'} {'CANCELLED'} ou un autre
            return {'FINISHED'}

        else:

            self.report({'ERROR'}, 'ça va pas bien oh !') 
            return {'CANCELLED'}   


def register():
    bpy.utils.register_class(AddSpot)


def unregister():
    bpy.utils.unregister_class(AddSpot)
