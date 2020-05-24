import vs

import python_sfm
reload(python_sfm)

def main():
    aset = sfm.GetCurrentAnimationSet()
    rc = aset.GetRootControlGroup()
    scene = sfm.GetCurrentShot().scene

    anim_set = python_sfm.SFMAnimationSet(sfm.GetCurrentAnimationSet())
    game_model = anim_set.game_model

    # dag = game_model._original
    # vs.CDmAnimUtils.SetOverrideParent(dag, scene, True, True)

    children = game_model.attributes_dict['children'].value
    for child in children:
        sfm_child = python_sfm.SFMElement(child)
        dag = sfm_child._original
        vs.CDmAnimUtils.SetOverrideParent(dag, scene, True, True)

    return

if __name__ == '__main__':
	main()