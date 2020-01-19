***************
Tmplcopy
***************

Interactive template file copier

Usage::

    python .\tmplcopy.py [-t <TEMPLATE_DIR>] [DESTINATION_DIR]
    python .\tmplcopy.py -h | --help
    python .\tmplcopy.py -v | --version

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

Requirements::

    Python3, docopt, tkinter


.. EOF
