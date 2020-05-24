
If you tried to write some Source Filmmaker scripts with python you've probably noticed that it's not so straightforward. That's why I've started working on this library.
At this point my friend is leaving SFM to continue work in UE and so do I. Hopefully some scripts or parts of code will be useful to make something useful out of SFM or just to learn and improve their own scripts.

What it does.
SFM Initialization (SourceFilmmaker\game\usermod\scripts\sfm\sfm_init.py):
- autosave - the script will save current session every n mins to separate file in usermod/elements/sessions/autosaves/ as it is the best way to survive SFM's habbit of unexpected crashes. Dont forget to clean up autosave folder from time to time.

Animation set rig menu (SourceFilmmaker\game\platform\scripts\sfm\animset):

- `rig_physics` - add sfmphys physics rig to object
- `run_sfmphys_Simulation` - start sfmphys simulation for objects with the rig
- `sfmphys_make_object_kinematic` - make sfmphys rigged object kinematic and remove some physics constraints. The purpose is to keep object's ability to interact with other sfmphys objects while adding your own animation to it. Example: you have an animated running man. You add rig_physics to it - it stops running and falls due gravity. You make all physic handles kinematic - it now stands still but still interacts with different objects. If you use sfmphys_make_object_kinematic it won't just make all handles kinematic - it will also remove some physics constraint. As result you will have the same running man you began with, except now it can interact with physics objects on it's way (f.e. bunch of boxes or cloth)



- `copy_materials` (LESS RELIABLE METHOD but could be useful) - copy all materials properties from one animation to `paste_masterials` on another. Useful when you need to copy textures, alpha, phong or some other properties from one model to bunch of the same models. Adds override materials to animation set (with some limitations). 
- `copy_materials_by_link` (MORE RELIABLE) - combined with `paste_materials_by_link` does exactly the same as `copy_materials` and `paste_masterials` but have less limitations and more reliable. Should be preffered.

- `lock_transforms` - locks transforms 
- `generate_docs` - saves some information about SFM methods to "SourceFilmmaker\game\help"

DAG Utilities Menu (SourceFilmmaker\game\platform\scripts\sfm\dag\exact\count1):
- `position_copy` / `position_paste` - copy position from one DAG and post to another, pretty straightforward.

SFM util library (SourceFilmmaker\game\sdktools\python\global\lib\site-packages\python_sfm.py):
Could be imported with `import python_sfm` and could be used for your own scripts. I've used it to summarize my knowledge about how can I interact with SFM using Python and make it less painful (to make scripts more readable and easier to write)

---

Installation:

Copy "game" folder into your SourceFilmmaker directory. Be careful because with overwriting your own scripts.
Some scripts are using https://pypi.org/project/pyperclip to copy and paste data to clipboard (included in this repository).

---

Mentions:
- physics module is fork from https://github.com/btdavis/sfmphys
- autosave feature is fork from someone from github (cant find exact repository, it might be deleted at this point)