def info(message):
	print(f"[code] {message}")

def readFile(src):
	arq = open(src,"r")
	res = arq.read()
	arq.close()
	return res

def writeFile(src,string):
	arq = open(src,"w")
	arq.write(string)
	arq.close()

def getDependency(link):
	l = link.split(":")
	groupId    = l[0]
	artifactId = l[1]
	version    = l[2]
	res        = ""
	res += "<dependency>\n"
	res += "			<groupId>"+groupId+"</groupId>\n"
	res += "			<artifactId>"+artifactId+"</artifactId>\n"
	res += "			<version>"+version+"</version>\n"
	res += "		</dependency>\n";
	return res;
