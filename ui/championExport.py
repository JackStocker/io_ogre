import bpy
import sys

sys.path.append('/home/jack/Documents/Projects/Champion/Scripts')
sys.path.append('E:/Projects/Champion/Scripts')
import championExport

def auto_register(register):
    yield champion_export
    yield ChampionExportOperator


class ChampionExportOperator(bpy.types.Operator):
    '''Exports the model and skeleton of the current selected object'''
    bl_idname = "champion.export"
    bl_label = "Export"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(self,context):
        return championExport.canExportObject(context.active_object)

    def invoke(self, context, event):
        championExport.championExport(context.active_object)

        return {'FINISHED'}


class champion_export(bpy.types.Menu):
    """ Exports the model and skeleton of the current selected object """
    bl_label = "Export"

    def draw(self, context):
        layout = self.layout
        layout.operator('champion.export', text="Export")

