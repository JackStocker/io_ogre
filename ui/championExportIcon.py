import bpy
import sys

sys.path.append('/home/jack/Documents/Projects/Champion/Scripts')
sys.path.append('E:/Projects/Champion/Scripts')
import championRenderIcons

def auto_register(register):
    yield champion_export_icon
    yield ChampionExportIconOperator


class ChampionExportIconOperator(bpy.types.Operator):
    '''Render an icon of the current selected object'''
    bl_idname = "champion.export_icon"
    bl_label = "Export Icon"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(self,context):
        return championRenderIcons.canRenderIcon(context.active_object)

    def invoke(self, context, event):
        championRenderIcons.renderObjectIcon(context.active_object)

        return {'FINISHED'}


class champion_export_icon(bpy.types.Menu):
    """ Render an icon of the current selected object """
    bl_label = "Export Icon"

    def draw(self, context):
        layout = self.layout
        layout.operator('champion.export_icon', text="Export Icon")

