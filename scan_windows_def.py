#!/usr/bin/env python3

import sys
import subprocess
import re

def get_p():
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("",0))
        s.listen(1)
        port = s.getsockname()[1]
        s.close()
        return port

sport = get_p()

#sport = sys.argv[1]

drun_cmd = "docker run -l %s -d --security-opt seccomp=seccomp.json -p %s:3993 malice/windows-defender web" %(sport,sport)
lscont_cmd =  "docker container ls -aq --filter label=%s" %(sport)
dprune_cmd = "docker container prune -f"

fpath = sys.argv[1]
scmd = "http -f localhost:%s/scan malware@%s" %(sport,fpath)

if __name__ == "__main__":
	process = subprocess.run(drun_cmd.split(), stdout=subprocess.PIPE, check=True)

	print("Scanning file: '" + fpath + "' with Windows Defender AV")
	process = subprocess.run(scmd.split(), stdout=subprocess.PIPE, check=True)
	output = process.stdout
#	print(output)
	
	if ("false" in str(output)):
		print("0")
	elif ("true" in str(output)):
		print("1")

	process = subprocess.run(lscont_cmd.split(), stdout=subprocess.PIPE, check=True)
	con_id = process.stdout
	con_id = str(con_id)[2:14]
	dstop_cmd = "docker container stop %s" %(con_id)

	process = subprocess.run(dstop_cmd.split(), stdout=subprocess.PIPE, check=False)
	process = subprocess.run(dprune_cmd.split(), stdout=subprocess.PIPE, check=True)
