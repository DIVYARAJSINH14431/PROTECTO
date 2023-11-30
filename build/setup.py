from distutils.core import setup
import py2exe

setup(
    windows=['signinpage.py'], # replace with the name of your main script
    options={
        'py2exe': {
            'packages': ['AddPass.py','alldirScan.py','antivirusgui.py','csOFF.py','csON.py','delpass.py','dirScan.py','getPass.py','Homepage.py','passMan.py','signup.py','updtPass.py'],
            'includes': ['tkinter', 'your_module'], # add the names of any other modules you import
            'bundle_files': 1,
            'optimize': 2,
            'compressed': True,
            'dll_excludes': ['tcl85.dll', 'tk85.dll'] # exclude any unnecessary DLL files
        }
    },
    zipfile=None
)
