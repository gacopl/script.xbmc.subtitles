# -*- coding: utf-8 -*- 

import os
import sys
import xbmc
import xbmcaddon

__addon__      = xbmcaddon.Addon()
__author__     = __addon__.getAddonInfo('author')
__scriptid__   = __addon__.getAddonInfo('id')
__scriptname__ = __addon__.getAddonInfo('name')
__cwd__        = __addon__.getAddonInfo('path')
__version__    = __addon__.getAddonInfo('version')
__language__   = __addon__.getLocalizedString

__cwd__        = xbmc.translatePath( __addon__.getAddonInfo('path') )
__profile__    = xbmc.translatePath( __addon__.getAddonInfo('profile') )
__resource__   = xbmc.translatePath( os.path.join( __cwd__.decode('utf-8'), u"resources", u"lib" ).encode('utf-8') )

sys.path.append (__resource__.decode('utf-8'))

# GENERAL STRINGS ENCODING CONSIDERATION TO BE USED IN THIS FILE
#   This file tries to adhere to pythons recommendations when handling strings:
#     "Software should only work with Unicode strings internally, converting
#      to a particular encoding on output."
#
#    THis means that excessive conversions will be done when getting
#    strings from xbmc modules (that return 'utf-8' strings) that are used
#    only to call xbmc modules. But this way we can be certain all strings are Unicode
#    and facilitates maintenance.
# General Hints:
#   * Decode all strings coming from XBMC calls (from ‘utf-8’). Not needed from Frodo and up.
#   * encode to utf-8 before calling xbmc modules.
#   * decode (if needed) file/path strings using fsEncoding.
#   * Most system calls allow Unicode strings.
#   * A practical exception to all this are the __strings__ that will remain str for convenience


#String encoding constants for unicode compatibility
fsEncoding = sys.getfilesystemencoding()


import gui
from utilities import log, pause, unpause, UserNotificationNotifier

if ( __name__ == '__main__' ):
  __unpause__ = False
  ui = gui.GUI( "script-XBMC-Subtitles-main.xml" , __cwd__ , "Default")
  if (ui.set_allparam()):
    notification = UserNotificationNotifier(__scriptname__, __language__(764), 2000)    
    if not ui.Search_Subtitles(False):
      __unpause__ = pause()
      ui.doModal()
    else:
      notification.close(__language__(765), 1000) 
  else:
    __unpause__ = pause() 
    ui.doModal()
        
  del ui
  if __unpause__:
    unpause()
  sys.modules.clear()

