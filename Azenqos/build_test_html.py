import os
import sys
import subprocess

def runcommand (cmd):
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True,
                            universal_newlines=True)
    std_out, std_err = proc.communicate()
    return proc.returncode, std_out, std_err

path = os.path.dirname(os.path.abspath(__file__))
htmlString = "<html>"
htmlString += "<body>"

files = []
for file in os.listdir(path):
    if file.startswith("test_") and file.endswith(".py"):
        print(sys.executable + " " + os.path.join(path,file))
        (ret, out, err) = runcommand(sys.executable + " " + os.path.join(path,file))
        if ret == 0:
            htmlString += "&#9989; " + file
        else:
            htmlString += "&#9940; " + file
            htmlString += "<br /><span style='color:red'>============<pre><code>"
            htmlString += err
            htmlString += "============</code></pre></span>"
        htmlString += "<br />"

htmlString += "</body>"
htmlString += "</html>"

buildPath = os.path.join(path,'build')
if not os.path.exists(buildPath):
    os.makedirs(buildPath)

f = open(os.path.join(buildPath,'index.html'), "w")
f.write(htmlString)
f.close()