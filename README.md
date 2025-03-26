# Comando `code`

## Usage: `code` [-options] [args...]

Este comando oferece funcionalidades para auxiliar no desenvolvimento, com opções específicas para projetos Maven.

### Opções

#### `-javaconsole`
Cria um novo projeto Java Console com a estrutura básica.

**Uso:** `code -javaconsole <package> <name_project> <version> <dependency...>`

**Parâmetros:**

* `<package>`: Endereço do pacote Java para o projeto (ex: `com.example.app`).
* `<name_project>`: Nome do projeto Java (ex: `MeuProjetoConsole`).
* `<version>`: Versão inicial do projeto (ex: `1.0.0`).
* `<dependency>` : Endereço do pacote de dependencia para o projeto (ex: `groupId:artifactId:version`)
**Exemplo:**

Para criar um novo projeto Java Console com o pacote `com.meuapp`, nome `Calculadora` e versão `0.1.0`, execute:

```code -javaconsole com.meuapp Calculadora 0.1.0```

Para adcionar dependencias ao projeto adcione os argumentos:

```groupId:artifactId:version```
