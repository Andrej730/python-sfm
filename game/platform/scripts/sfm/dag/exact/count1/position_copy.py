#================= Copyright Andrej, All rights reserved. ==============================
#
# Purpose: 
#
#==================================================================================================

import pyperclip

position = sfm.GetPosition()
pyperclip.copy(';'.join([str(i) for i in position]))