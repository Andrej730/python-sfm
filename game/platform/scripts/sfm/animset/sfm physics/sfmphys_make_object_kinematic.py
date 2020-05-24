import sfm
import PySide
import re
import python_sfm
reload(python_sfm)


def main():
    aset = sfm.GetCurrentAnimationSet()
    rc = aset.GetRootControlGroup()

    if not rc.HasChildGroup('Rigidbodies', False):
        PySide.QtGui.QMessageBox.critical(
            None, 'ERROR - sfmphys_make_object_kinematic.py',
            'Error! Could\'nt find Rigidbodies control group.\n\n'
            'Try to reapply rig with rig_physics.py again or report error to developer.')
        return

    # Remove constraints for all groups excep Rigidbodies and PhysConstraints
    other_control_groups = []
    for control_group in rc.GetValue('children'):
        control_group_name = control_group.GetName()
        if control_group_name not in ('Rigidbodies', 'PhysConstraints') and \
                control_group.GetValue('controls'):
            other_control_groups.append(control_group_name)
    sfm.ClearSelection()
    sfm.Select(*other_control_groups)
    sfm.RemoveConstraints()

    rigid_bodies = rc.FindChildByName('Rigidbodies', False)
    for child in rigid_bodies.GetValue('children'):
        # child is DmeControlGroup
        name = child.GetName()
        controls = child.GetValue('controls')
        for control in controls:
            if control.GetName().startswith('Handle'):
                handle = control
            elif control.GetName().startswith('Kinematic'):
                kinematic = control

        # set kinematic = 1 all the way
        kinematic = python_sfm.SFMControl(kinematic)
        ch = kinematic.channels[0]
        ch.values = [1 for i in ch.values]

        # create parent constraint: original control -> physical handle
        handle_name = handle.GetName()
        original_control_name = re.findall(r'Handle \((.+)\)$', handle_name)[0]
        sfm.ParentConstraint(
            original_control_name,
            handle.GetName(),
            mo=True
        )

if __name__ == '__main__':
    main()