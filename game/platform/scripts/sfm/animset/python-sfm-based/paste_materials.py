"""Paste materials to animation set. Use copy_materials first."""

import pyperclip
import json
import vs

import PySide
import python_sfm
reload(python_sfm)

class SFMAttr:
	def __init__(self, add_attr, get_sfm_value):
		self.add_attr = add_attr
		self.get_sfm_value = get_sfm_value

StringType = {
	'add_attr': lambda material: material.AddAttributeAsString,
	'get_sfm_value': lambda v: v.encode('utf-8')
}

ColorType = {
	'add_attr': lambda material: material.AddAttributeAsColor,
	'get_sfm_value': lambda v: vs.misc.Color(*v)
}

IntType = {
	'add_attr': lambda material: material.AddAttributeAsInt,
	'get_sfm_value': lambda v: v
}

FloatType = {
	'add_attr': lambda material: material.AddAttributeAsFloat,
	'get_sfm_value': lambda v: v
}

Vector4Type = {
	'add_attr': lambda material: material.AddAttributeAsVector4,
	'get_sfm_value': lambda v: vs.mathlib.Vector4D(*v)
}

supported_types = {
	'String': SFMAttr(**StringType),
	'Color': SFMAttr(**ColorType),
	'Int': SFMAttr(**IntType),
	'Float': SFMAttr(**FloatType),
	'Vector4': SFMAttr(**Vector4Type)
}


def main():
	try:
		materials_dict = json.loads(pyperclip.paste())
	except ValueError:
		PySide.QtGui.QMessageBox.critical(
			None, 'ERROR - copy_materials.py',
			'Error! Your clipboard contains invalid json code.\n\n'
			'Try to copy_materials again or report error to developer.')
		return


	animSet = sfm.GetCurrentAnimationSet()
	python_sfm.set_override_materials(True)
	gameModel = animSet.gameModel

	for material in gameModel.materials:
		material_name = material.GetValue('name')

		if material_name in materials_dict:
			attributes_dict = materials_dict[material_name]

			for attribute in attributes_dict:
				# encoding is workaround for NotImplementedError
				attribute = attribute.encode('utf-8')
				attribute_type_s = attributes_dict[attribute][0]
				attr_type_func = supported_types[attribute_type_s]


				attribute_value = attributes_dict[attribute][1]
				attribute_value = attr_type_func.get_sfm_value(attribute_value) 

				# if not material.HasAttribute('$basetexture'):
				# 	material.AddAttributeAsString('$basetexture')
				# material.SetValue('$basetexture', 'basetexture')

				if not material.HasAttribute(attribute):
					attr_type_func.add_attr(material)(attribute)
				material.SetValue(attribute, attribute_value)

main()
