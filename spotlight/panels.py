import bpy

from . import operators, properties

# Create a panel
class MyPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tools"

    bl_label = 'my panel'


    def draw(self, context):
        
        props = properties.get_props()  # Get the default properties (bpy.context.scene.spotlight)

        layout = self.layout

        layout.label(text=self.bl_label)

        layout.prop(
            props,
            'name',
            text='name'
        )
        layout.prop(
            props,
            'intensity'
        )
        layout.prop(
            props,
            'light_type'
        )


        # Places a button into the layout to call an Operator
        # When the button is activated, Call invoke() (who calls execute() by default)
        layout.operator(operators.AddSpot.bl_idname)

def register():
    bpy.utils.register_class(MyPanel)


def unregister():
    bpy.utils.unregister_class(MyPanel)
