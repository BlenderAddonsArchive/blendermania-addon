import bpy

from ..properties.Functions import *
from ..utils.Constants import MAP_OBJECT_ITEM, MAP_OBJECT_BLOCK
from ..utils.Functions import get_global_props, get_obj_potential_item_path

def on_update_map_obj_props(self, context):
    tm_props = get_global_props()
    obj = tm_props.PT_map_object.object_item
    if obj:
        if obj.tm_map_object_kind:
            tm_props.PT_map_object.object_type = obj.tm_map_object_kind
            tm_props.PT_map_object.object_path = obj.tm_map_object_path
            tm_props.PT_map_object.object_item_animphaseoffset = obj.tm_map_object_animphaseoffset
            tm_props.PT_map_object.object_item_difficultycolor = obj.tm_map_object_difficultycolor
            tm_props.PT_map_object.object_item_lightmapquality = obj.tm_map_object_lightmapquality
        else:
            if tm_props.PT_map_object.object_type == MAP_OBJECT_BLOCK:
                tm_props.PT_map_object.object_path = ""
            else:
                tm_props.PT_map_object.object_path = get_obj_potential_item_path(obj)
    else:
        tm_props.PT_map_object.object_path = ""

def on_update_map_obj_kind(self, context):
    tm_props = get_global_props()
    tm_props.PT_map_object.object_path = ""

class MapObjectProperties(bpy.types.PropertyGroup):
    object_item: bpy.props.PointerProperty(type=bpy.types.Object, update=on_update_map_obj_props)
    object_type: bpy.props.EnumProperty(
        items=(
            (MAP_OBJECT_BLOCK, "Block", ""),
            (MAP_OBJECT_ITEM, "Item", ""),
        ),
        name="Use link to Item or Block",
        default=MAP_OBJECT_ITEM,
        update=on_update_map_obj_kind
    )
    object_path: bpy.props.StringProperty(name="Name/path of Item or Block", search=get_ingame_vanilla_item_names, subtype="FILE_PATH")
    object_item_animphaseoffset: bpy.props.EnumProperty(items=get_animphaseoffset_values(), name="AnimPhaseOffset")
    object_item_difficultycolor: bpy.props.EnumProperty(items=get_difficultycolor_values(), name="DifficultyColor")
    object_item_lightmapquality: bpy.props.EnumProperty(items=get_lightmapquality_values(), name="LightmapQuality")