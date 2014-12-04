import sys
import os
sys.path.insert(0, os.path.abspath('..\\'))

from eudtrg import *

LoadMap('outputmap/basemap/basemap.scx')

main = NextTrigger()

retval = f_dwread_epd(EPD(0x5993D4))  # Get address of STR section
retvt = retval.GetVTable()

main2 = Trigger(
    nextptr=retvt,
    actions=[
        retval.QueueAssignTo(EPD(0x58A364)),
        SetNextPtr(retvt, triggerend)
    ]
)

SaveMap('outputmap/readdword.scx', main)