from distutils.core import setup
import py2exe

import numpy
import os
import sys
import psutil

# add any numpy directory containing a dll file to sys.path
def numpy_dll_paths_fix():
    paths = set()
    np_path = numpy.__path__[0]
    for dirpath, _, filenames in os.walk(np_path):
        for item in filenames:
            if item.endswith('.dll'):
                paths.add(dirpath)

    sys.path.append(*list(paths))

numpy_dll_paths_fix()

setup(windows = [{"script": "pronterface.py", "icon_resources": [(1, "pronterface.ico")]},
                 #{"script": "plater.py", "icon_resources": [(1, "plater.ico")]},
                 ],
      console = [{"script": "pronsole.py", "icon_resources": [(1, "pronsole.ico")]},
                 ],
      options = {"py2exe": {"bundle_files": 1,
                            "dll_excludes": ["w9xpopen.exe",
                            "API-MS-Win-Core-DelayLoad-L1-1-0.dll",
                            "API-MS-Win-Core-ErrorHandling-L1-1-0.dll",
                            "API-MS-Win-Core-File-L1-1-0.dll",
                            "API-MS-Win-Core-Heap-L1-1-0.dll",
                            "API-MS-Win-Core-Handle-L1-1-0.dll",
                            "API-MS-Win-Core-Interlocked-L1-1-0.dll",
                            "API-MS-Win-Core-IO-L1-1-0.dll",
                            "API-MS-Win-Core-LibraryLoader-L1-1-0.dll",
                            "API-MS-Win-Core-LocalRegistry-L1-1-0.dll",
                            "API-MS-Win-Core-Misc-L1-1-0.dll",
                            "API-MS-Win-Core-ProcessThreads-L1-1-0.dll",
                            "API-MS-Win-Core-Profile-L1-1-0.dll",
                            "API-MS-Win-Core-String-L1-1-0.dll",
                            "API-MS-Win-Core-Synch-L1-1-0.dll",
                            "API-MS-Win-Core-SysInfo-L1-1-0.dll",
                            "API-MS-Win-Core-ThreadPool-L1-1-0.dll",
                            "API-MS-Win-Security-Base-L1-1-0.dll",
                            "IPHLPAPI.DLL",
                            "NSI.dll",
                            "WINNSI.DLL",
                            "WTSAPI32.dll",],
                            "excludes": ['_ssl',
                            'pickle',
                            'calendar',
                            'Tkconstants',
                            'Tkinter',
                            'tcl',
                            'email',
                            'configparser',
                            'builtins',
                            'copyreg',
                            'cffi',
                            'importlib',
                            'multiprocessing',
                            'pkg_resources',
                            'winreg',
                            '_dummy_thread',
                            '_thread'],
                            "compressed": 1,
                            "optimize": 2
                            }
                 }
      )
