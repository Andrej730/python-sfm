"""Copy materials from animation set. Use paste_materials after."""

import json
import vs
import pyperclip

import PySide
import python_sfm
reload(python_sfm)

def main():
	try:
		sfm.GetCurrentAnimationSet().gameModel.materials
	except AttributeError:
		PySide.QtGui.QMessageBox.critical(
			None, 'ERROR - copy_materials.py',
			'Error! You need to add materials override first.\n\n'
			'Script will now try to override materials for you '
			'but you\'ll need to restart it anyway..\n\n'
			'PS Sorry, your custom material attributes were reset due SFM bug.')
		python_sfm.set_override_materials(True)
		return

	get_string_value = lambda v: ('String', v)
	get_color_value = lambda v: ('Color', (v.r(), v.g(), v.b(), v.a()))
	get_int_value = lambda v: ('Int', v)
	get_float_value = lambda v: ('Float', v)
	get_vector4_value = lambda v: ('Vector4', (v.x, v.y, v.z, v.w))

	supported_types = {
		str: get_string_value,
		vs.misc.Color: get_color_value,
		int: get_int_value,
		float: get_float_value,
		vs.mathlib.Vector4D: get_vector4_value
	}

	anim_set = python_sfm.SFMAnimationSet(sfm.GetCurrentAnimationSet())
	game_model = anim_set.game_model

	materials_dict = dict()
	attribute_filter = ['name']

	for material in game_model.materials:
		material_name = material.name
		attributes = material.attributes

		for attribute in attributes:
			if attribute.name in attribute_filter:
				continue

			attribute_type = type(attribute.value)

			if attribute_type in supported_types:
				attribute_value = supported_types[attribute_type](attribute.value)
				if material_name not in materials_dict:
					materials_dict[material_name] = dict()
				materials_dict[material_name][attribute.name] = attribute_value
		
	memory = json.dumps(
		materials_dict,
		sort_keys=True,
		indent=4
	)
	pyperclip.copy(memory)

main()
