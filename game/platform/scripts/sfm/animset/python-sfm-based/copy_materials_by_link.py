"""Copy materials from animation set. Use paste_materials_by_link after."""
import json
import pyperclip

import python_sfm
reload(python_sfm)

def main():
	materials_dict = {}

	animset = sfm.GetCurrentAnimationSet()
	python_sfm.set_override_materials(True)
	animset = python_sfm.SFMAnimationSet(animset)
	materials = [mat.name for mat in animset.game_model.materials]

	materials_pack = (animset.name, materials)

	memory = json.dumps(
		materials_pack,
		sort_keys=True,
		indent=4
	)
	pyperclip.copy(memory)

main()