import python_sfm
reload(python_sfm)
import vs
reload(vs)
import PySide

shot = sfm.GetCurrentShot()
# attrs = shot.iterAttrs()
# print attrs

scene = shot.scene

animset = sfm.GetCurrentAnimationSet()
game_model = animset.gameModel
material = game_model.materials[0]
attribute = material.FirstAttribute()
# attrs = animset.iterAttrs()
# print attrs

# print action.dumpObjectInfo()
# print action.children()
# print type(action)
# print action.menu()
# print(dir(action))
# import inspect
# print inspect.getsource(game_model.__getattr__)
# print inspect.getsource(game_model._swig_getattr)

objects = [
	shot, scene, animset, animset.gameModel, game_model, # 1-5
	material, attribute,
	sfm, sfmApp, sfmClipEditor, sfmConsole, sfmUtils, 
	PySide, PySide.QtGui, PySide.QtCore,PySide.QtGui.QMessageBox,
	SFMStderrCatcher, SFMStdoutCatcher, StderrCatcher, StdoutCatcher]


python_sfm.docs_create_folders()
for i, o in enumerate(objects, 1):
	print str(i) + '.', o, type(o)
	python_sfm.docs_save_object(o)

PySide.QtGui.QMessageBox.information(
	None, 'generate_docs.py', 
	'Docs are saved to folder "SourceFilmmaker/game/help"')
