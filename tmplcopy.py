__doc__ = """Interactive template file copier

Usage:
    {f} [-t <TEMPLATE_DIR>] [DESTINATION_DIR]
    {f} -h | --help
    {f} -v | --version

Arguments:
    DESTINATION_DIR  Destination directory (default: current directory)

Options:
    -h --help          Show this screen and exit.
    -t <TEMPLATE_DIR>  Template directory (default: SCRIPT_DIR\\templates)
    -v --version       Show version

Template file name syntax:
    %y  Year
    %m  Month (01..12)
    %d  Day (01..31)
    %H  Hour (00..23)
    %M  Minute (00..59)
    %S  Second (00:60)
""".format(f='python ' + __file__)

from docopt import docopt
from tkinter import Tk, messagebox, filedialog
import os
import sys
import shutil
import datetime

def abort(message):
  print('ERROR: %s' % message, file=sys.stderr)
  messagebox.showerror('ERROR', message)
  sys.exit(1)

def select_template_files(template_dir):
  file_name = filedialog.askopenfilename(initialdir = template_dir, title = 'Templates', multiple = 1)
  return file_name

def z2(number):
  return str(number).zfill(2)

def embed_datetime(text, tod):
  year = str(tod.year).zfill(4)
  month = z2(tod.month)
  day = z2(tod.day)
  hour = z2(tod.hour)
  minute = z2(tod.minute)
  second = z2(tod.second)
  return text.replace('%y', year).replace('%m', month).replace('%d', day).replace('%H', hour).replace('%M', minute).replace('%S', second)

def dest_path(src_path, dest_dir):
  src_file = os.path.basename(src_path)
  dest_file = embed_datetime(src_file, datetime.datetime.now())
  return os.path.join(dest_dir, dest_file)


# MAIN
if __name__ == '__main__':
  args = docopt(__doc__, version='1.0.0')
  
  root = Tk()
  root.withdraw()
  
  dest_dir = args.get('DESTINATION_DIR') or os.getcwd()
  abs_dest_dir = os.path.abspath(dest_dir)
  if(not os.path.isdir(abs_dest_dir)):
    abort('Invalid destination directory [%s]' % abs_dest_dir)
  
  default_template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
  template_dir = args.get('-t') or default_template_dir
  abs_template_dir = os.path.abspath(template_dir)
  if(not os.path.isdir(abs_template_dir)):
    abort('Invalid template directory [%s]' % abs_template_dir)
  
  sources = select_template_files(abs_template_dir)
  
  for source in sources:
    destination = dest_path(source, abs_dest_dir)
    if os.path.exists(destination):
      abort('Already exists [%s]' % destination)
    
    shutil.copyfile(source, destination)
  
  root.destroy()
  sys.exit(0)

# EOF

