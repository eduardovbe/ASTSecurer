# ASTSecurer - Detecção de Vulnerabilidades em Contratos Inteligentes em Solidity

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

## Contribuição

As contribuições para aprimorar o ASTSecurer são bem-vindas! Caso você queira adicionar novas vulnerabilidades ou melhorar a detecção existente, sinta-se à vontade para enviar um pull request.

## Limitações

- O ASTSecurer ainda está em desenvolvimento e pode não cobrir todas as vulnerabilidades existentes em contratos em Solidity.
- A detecção de vulnerabilidades é baseada em padrões e comportamentos suspeitos, mas nem todos os casos podem ser detectados com 100% de precisão.
- É recomendável usar o ASTSecurer como uma ferramenta complementar à revisão manual dos contratos e a outras ferramentas de segurança.
