#================= Copyright Andrej, All rights reserved. ==============================
#
# Purpose: 
#
#==================================================================================================
import pyperclip
log = lambda x: sfm.Msg(str(x)+'\n')

try:
	clipboard = pyperclip.paste()
	position = [float(i) for i in clipboard.split(';')]
except:
	log("Incorrect position in clipboard: " + clipboard)
else:
	dag = sfm.FirstSelectedDag()
	sfm.SetOperationMode("Record")   
	sfm.Move(position[0], position[1], position[2])
	sfm.SetOperationMode("Pass")