***************
Tmplcopy
***************

Interactive template file copier

======================
How to use
======================

With a dialog, select template files.
Then the files are copied to your specified directory.

Command Line options
------------------------

Usage::

    .\tmplcopy.py [-t <TEMPLATE_DIR>] [DESTINATION_DIR]
    .\tmplcopy.py -h | --help
    .\tmplcopy.py -v | --version

Arguments::

    DESTINATION_DIR  Destination directory (default: current directory)

Options::

    -h --help          Show this screen and exit.
    -t <TEMPLATE_DIR>  Template directory (default: SCRIPT_DIR\templates)
    -v --version       Show version

Template file name syntax::

    %y  Year
    %m  Month (01..12)
    %d  Day (01..31)
    %H  Hour (00..23)
    %M  Minute (00..59)
    %S  Second (00:60)


==================
Setup
==================

Requirements
---------------

Python3, docopt, tkinter


Registering to Windows Context Menu
--------------------------------------

1. With Registory Editor, create a new key under HKEY_CLASSES_ROOT\\Directory\\Backgroundshell.

    :name: tmplcopy
    :value: Templates

2. Create a sub key under tmplcopy.

    :name: command
    :value: \\path\\to\\pythonw.exe \\path\\to\\tmplcopy.py -t \\path\\to\\templates "%V"


==================
License
==================

Public Domain


.. EOF
