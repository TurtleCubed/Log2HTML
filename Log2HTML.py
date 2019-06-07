import sys

"""
Provides a script that converts a .log file to a .HTML file.  Input the file name as a parameter from the terminal.
"""

# check if the file name is valid
if len(sys.argv) != 2:
    raise ValueError("Invalid parameters")
fileName = str(sys.argv[1])
ext = fileName[fileName.index("."):]
trunc = fileName[:fileName.index(".")]
fileNamehtml = trunc + ".html"
if ext != ".log":
    raise ValueError("Unrecognized file type")

# open file i/o
try:
    readFile = open(fileName, "r")
    writeFile = open(fileNamehtml, "w")
except IOError:
    print("An error occurred trying to open the files")


# html head
writeFile.write("<head>\n<style>\ntable, th, td {\n  border: 1px solid black;\n}\n</style>\n</head>\n\n")

# first row of table
writeFile.write("<table>\n<tr>\n<th>Subsystem Tag</th><th>Timestamp</th><th>Log Tag</th>")
writeFile.write("<th>Component Name</th><th>Data</th><th>Duration</th>\n</tr>")

# parse each line into lists of strings
for line in readFile:
    words = line.split()
    subsystemTag = words[0]
    timeStamp = words[1] + " " + words[2]
    logTag = words[3]
    componentName = words[5][:-1]
    data = ""
    duration = ""
    # handles different types of input differently
    if words[5] == "Main:":
        continue
    if words[6] == "connected":
        for word in words[6:]:
            data = data + word + " "
    else:
        start = 6
        end = words.index("in")
        for n in range(start, end):
            word = words[n]
            data = data + word + " "
        duration = words[end + 1] + "ms"

    # writing data to file
    writeFile.write("<tr>\n")
    writeFile.write("<td>" + subsystemTag + "</td>")
    writeFile.write("<td>" + timeStamp + "</td>")
    writeFile.write("<td>" + logTag + "</td>")
    writeFile.write("<td>" + componentName + "</td>")
    writeFile.write("<td>" + data + "</td>")
    writeFile.write("<td>" + duration + "</td>")
    writeFile.write("\n</tr>\n")

# close table and files
writeFile.write("\n</table>\n")
readFile.close()
writeFile.close()



