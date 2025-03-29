# Comando `code`

## Usage: `code` [-options] [args...]

Este comando oferece funcionalidades para auxiliar no desenvolvimento, com opções específicas para projetos Maven.
Este comando foi feito para linux.

### Considerações importantes
* Primeiro crie uma pasta com o nome do projeto.
* navegue até a pasta usando `cd`.
* as opções `-newfilejava` e `-deletefilejava` não funcionam se o projeto nao for criado antes nem se não tiver pom.xml no diretório atual.

### Opções

#### `-javaconsole`
Cria um novo projeto Java Console com a estrutura básica.

**Uso:** `code -javaconsole <package> <name_project> <version> <dependencies...>`

**Parâmetros:**

* `<package>`: Endereço do pacote Java para o projeto (ex: `com.example.app`).
* `<name_project>`: Nome do projeto Java (ex: `MeuProjetoConsole`).
* `<version>`: Versão inicial do projeto (ex: `1.0.0`).
* `<dependencies...>` : Endereço do pacote de dependencia para o projeto (ex: `groupId:artifactId:version`)
**Exemplo:**

Para criar um novo projeto Java Console com o pacote `com.meuapp`, nome `Calculadora` e versão `0.1.0`, execute:

```code -javaconsole com.meuapp Calculadora 0.1.0```

Para adcionar dependencias ao projeto adcione os argumentos:

```groupId:artifactId:version```

#### `-jar`
Cria um novo projeto Jar

**Uso:** `code: -jar <groupId> <artifactId> <version> <dependencies...>`

**Parâmetros:**

* `<groupId>`: Endereço do pacote Java para o projeto (ex: `com.example.app`).
* `<artifactId>`: Nome do projeto Java (ex: `MeuProjetoConsole`).
* `<version>`: Versão inicial do projeto (ex: `1.0.0`).
* `<dependencies...>` : Endereço do pacote de dependencia para o projeto (ex: `groupId:artifactId:version`)

Para criar um novo projeto Jar com o groupId `com.meuapp`, artifactId `Calculadora` e version `0.1.0`, execute:

```code -jar com.meuapp Calculadora 0.1.0```

Para adcionar dependencias ao projeto adcione os argumentos:

```groupId:artifactId:version```

#### `-newfilejava`
Cria um ou varios novo(s) arquivo(s) Java com a estrutura básica

**Uso:** `code -newfilejava <package...>`

**Parâmetros:**

* `package`: Endereço do pacote Java ou Pasta. (ex: `com.pacote.Main`)
> * `obs`: cria o pacote na pasta main e test se tiver em test

#### `-deletefilejava`
Deleta um ou varios arquivo(s) java ou pasta

**Uso:** `code -deletefilejava <package...>`

**Parâmetros:**

* `package`: Endereço do pacote Java ou Pasta. (ex: `com.pacote.Main` ou `com` deleta a pasta com)
> * `obs`: deleta o pacote na pasta main e test

# Instalação

Para instalar o comando code, siga os passos abaixo:

## Atenção
1. O comando será instalado em `/bin`

## Instalando o comando
1. **Abra o terminal e execute o seguinte comando para clonar o repositório:**
`git clone git@github.com:Gabrielsynapse/code.git`

2. **Navegue até a pasta:**
`cd code`

3. **de permisão para o script de instalação:**
`chmod +xrw install.sh`

4. **Execute o script de instalação:**
`./install.sh`

5. **Se o passo anterior mostrar permisão não definida execute:**
`bash install.sh`

6. **Por fim digite:**
`code --version`

7. **Se retornar comando não encontrado, provávelmente o diretorio `/bin` não está na variavél de ambiente PATH. para inserir digite:**
`export PATH+=":/bin"`

8. **insira essa linha em um arquivo que faz parte da inicialização do sistema.**

## para desinstalar o comando siga os passos anteriores usando o arquivo de desinstação *unistall.sh*

