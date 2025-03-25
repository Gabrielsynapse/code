package code;

public class Java_newjavaconsole{
	private static String groupId;
	private static String artifactId;
	private static String version;
	private static String template_pom;
	private static String template_java;
	private static String path;
	private static String pwd;
	private static String srcPom;
	private static String srcJava;
	private static String src;

	private static void print(String str){
		System.out.println("[code] " + str);
	}
	public static void main(String[] args){
		pwd        = args[0];
		path       = args[1];
		groupId    = args[2];
		artifactId = args[3];
		version    = args[4];

		src = pwd + "/" + artifactId;
		srcPom = src + "/pom.xml";
		srcJava = src + "/src/main/java/" + groupId.replaceAll("\\.","/");
		template_pom  = FileUtil.readFile(path+"/template/javaconsole.xml");
		template_java = FileUtil.readFile(path+"/template/javaconsole.java");

		String pom = template_pom.
			replaceAll("%groupId",groupId).
			replaceAll("%artifactId",artifactId).
			replaceAll("%version",version);

		String mainJava = template_java.
			replaceAll("%groupId",groupId).
			replaceAll("%artifactId",artifactId).
			replaceAll("%version",version);

		print("Montando diretorio "+srcPom);

		FileUtil.makeDir(pwd+"/"+artifactId);

		print("Escrendo arquivo pom.xml em "+pwd+"/"+artifactId+"/pom.xml");
		FileUtil.writeFile(srcPom,pom);

		print("Montando diretorio dos arquivos Java em "+srcJava);
		FileUtil.makeDir(srcJava);

		print("Escrevendo arquivo Main em "+srcJava);
		FileUtil.writeFile(srcJava+"/Main.java",mainJava);

		//System.out.println(pom);
	}
}