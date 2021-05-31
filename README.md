Simply run the file from the commandline:

./scan_windows_def.py <filename>

This will start up a docker container with Windows Defender, scan the file and return a boolean value (0=not infected, 1=infected). 
It will then stop the docker container and clean it up.
  
Dep: HTTPie
