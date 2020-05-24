"""Paste materials to animation set. Use copy_materials_by_link first."""

import pyperclip
import json

import PySide
import python_sfm
reload(python_sfm)

def main():
	try:
		materials_pack = json.loads(pyperclip.paste())
	except ValueError:
		PySide.QtGui.QMessageBox.critical(
			None, 'ERROR - copy_materials.py',
			'Error! Your clipboard contains invalid json code.\n\n'
			'Try to copy_materials_by_link again or report error to developer.')
		return

	to_animset = python_sfm.SFMAnimationSet(sfm.GetCurrentAnimationSet())
	python_sfm.set_override_materials(True)
	to_materials = to_animset.game_model.materials
	to_materials_dict = dict(zip([material.name for material in to_materials], to_materials))

	from_animset = python_sfm.getAnimationSetByName(materials_pack[0])
	from_materials = from_animset.game_model.materials
	from_materials_dict = dict(zip([material.name for material in from_materials], from_materials))

	for material_name in materials_pack[1]:
		if material_name in to_materials_dict:
			from_material = from_materials_dict[material_name]
			to_material = to_materials_dict[material_name]
			from_material.copy_attributes_to_material(to_material)

main()