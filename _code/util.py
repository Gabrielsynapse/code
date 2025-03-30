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

def getTagPom(src,nametag):
	pom = readFile(src)
	return pom[pom.index(f"<{nametag}>"):pom.index(f"</{nametag}>")].replace(f"<{nametag}>","")

def getTag(pom,nametag):
	return pom[pom.index(f"<{nametag}>"):pom.index(f"</{nametag}>")].replace(f"<{nametag}>","")

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

def existDependency(_src,_groupId="",_artifactId="",_version=""):
	pom = readFile(_src)
	dependencies = pom[pom.index("<dependencies>"):pom.index("</dependencies>")+15].replace(" ","").replace("\t","").replace("\n","").split("</dependency>")
	dependencies.pop()
	res = False
	#para cada dependencia:
	for dependency in dependencies:
		#se tiver o groupId:
		if _groupId == getTag(dependency,"groupId") or _version == "":
			#se tiver o artifactId:
			if _artifactId == getTag(dependency,"artifactId") or _version == "":
				#se tiver o version
				if _version == getTag(dependency,"version") or _version == "":
					return True
	return False