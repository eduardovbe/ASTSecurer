# ASTSecurer - Detecção de Vulnerabilidades em Contratos Inteligentes em Solidity

![Logo](image/logo.png)

O ASTSecurer é um programa desenvolvido em Python que permite detectar vulnerabilidades em contratos inteligentes escritos em Solidity, através da análise semântica da AST (Abstract Syntax Tree).

## Funcionalidades

- Identificação de vulnerabilidades conhecidas em contratos inteligentes em Solidity.
- Análise semântica da AST para encontrar padrões e comportamentos suspeitos nos contratos.
- Rapidez na analise de grandes volumes de dados.
- Fácil execução com um único comando.

## Requisitos

- Python 3.x
- Bibliotecas Python: Solidity Parser, AST Analysis, entre outras. (Listadas no arquivo `requirements.txt`)

## Como Executar

1. Clone este repositório para o seu ambiente local:

   ```shell
   git clone https://github.com/eduardovbe/AST_Vulnerabities_Checker
   ```

2. Acesse o diretório do projeto:

   ```shell
   cd AST_Vulnerabities_Checker
   ```

3. Instale as dependências:

   ```shell
   pip install -r requirements.txt
   ```

4. Execute o programa, passando o diretório do dataset como argumento:

   ```shell
   python astsecurer.py "diretorio_do_dataset"
   ```

   Certifique-se de substituir `"diretorio_do_dataset"` pelo caminho do diretório onde seus contratos inteligentes em Solidity estão localizados.

5. Aguarde até que a análise seja concluída. O ASTSecurer irá percorrer todos os contratos no diretório especificado em busca de vulnerabilidades.

6. Após a conclusão da análise, o programa irá exibir as vulnerabilidades detectadas, bem como informações relevantes sobre cada uma delas.


## Vulnerabilidades detectadas

| Código da Vulnerabilidade | Nome da Vulnerabilidade                  |
|--------------------------|-----------------------------------------|
| SWC-100                  | Function Default Visibility            |
| SWC-102                  | Outdated Compiler Version              |
| SWC-104                  | Unchecked Call Return Value            |
| SWC-108                  | State Variable Default Visibility      |
| SWC-111                  | Use of Deprecated Solidity Functions   |
| SWC-115                  | Authorization through tx.origin        |
| SWC-116                  | Block values as a proxy for time       |
| SWC-127                  | Arbitrary Jump with Function Type      |
| SWC-130                  | Right-To-Left-Override control char    |
| SWC-131                  | Presence of unused variables           |
| SWC-134                  | Message call with hardcoded gas amount |

Esses códigos e nomes de vulnerabilidades correspondem à lista de vulnerabilidades disponível no site [SWC Registry](https://swcregistry.io) que classifica e documenta as vulnerabilidades comuns em contratos inteligentes.


## Limitações

- O ASTSecurer não cobre todas as vulnerabilidades existentes em contratos em Solidity apenas as quais são possiveis a detectão atraves de uma analise semântica.
- A detecção de vulnerabilidades é baseada em padrões e comportamentos suspeitos, mas nem todos os casos podem ser detectados com 100% de precisão.
- É recomendável usar o ASTSecurer como uma ferramenta complementar à revisão manual dos contratos e a outras ferramentas de segurança.
