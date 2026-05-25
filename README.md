---
DESAFIO NA COZINHA:

  Este repositório contém a solução para o trabalho prático "Desafio na Cozinha" da disciplina de Algoritmos e Estruturas de Dados II. O objetivo do sistema é organizar o acervo culinário de um restaurante, permitindo buscas eficientes, recomendação de menus a partir do tempo e nota de preparo e um sistema de verificação da integridade dos dados das receitas.

    Link do Repositório: https://github.com/gmgass/AED2_DesafioNaCozinha


ESTRUTURA DE DADOS E ALGORITMOS IMPLEMENTADOS:
  TABELA HASH:
    - Foi aplicada como armazenamento principal das receitas do sistema.
    - Foi escolhida por oferecer complexidade de tempo média de busca e inserção rápida, ideal para o cadastro e recuperação de receitas utilizando identificadores únicos (IDs).

  TRIE:
    - Foi utilizada nos índices dos nomes das receitas para executar buscas rápidas.
    - Foi escolhida pela praticidade em buscas por prefixo. Permite que o usuário digite parte do nome do prato e o sistema encontre todas as ocorrências sem precisar verificar todo o livro de receitas.

  ALGORITMO GULOSO:
    - Foi utilizado no Modo CHefe, mais especificamente, no sistema de recomendação de menus sob restrição de tempo.
    - O critério guloso prioriza ordenar e escolher receitas de forma decrescente com base no seu custo-benefício. Isso garante que o Chef Jacquin sempre fará os pratos mais bem avaliados possíveis que caibam no tempo limite do expediente, ignorando pratos muito demorados de baixa nota.


MODO INVESTIGAÇÃO:
  Para garantir a integridade dos dados sem a necessidade de bibliotecas criptográficas pesadas, a classe Receita gera uma "assinatura de segurança" no momento em que é instanciada, baseada no seu conteúdo principal (Nome, Tempo e Nota). O sistema possui uma rotina que varre o Livro de Receitas recriando essas assinaturas e comparando-as com as originais. Se houver divergência, o sistema alerta sobre a adulteração do prato em memória.


FONTE DE DADOS:
  Para facilitar a execução e demonstração deste projeto, a fonte de dados utilizada é uma base de dados estática internalizada no próprio arquivo de testes (main.py). Os dados são instanciados diretamente via código através de uma lista de objetos Receita, contendo informações fictícias essenciais (ID, Nome, Tempo de Preparo e Avaliação) para validar perfeitamente a execução do Algoritmo Guloso e a verificação de hash.


COMO EXECUTAR:
  1. É necessário ter Python instalado.
  2. Faça o clone do repositório ou baixe os arquivos para o seu computador.
  3. Abra o terminal na raiz da pasta do projeto e execute o comando:

    Bash
    python main.py

  O console exibirá a inicialização do sistema, a recomendação do Modo Chef (Algoritmo Guloso) limitando o menu a 60 minutos, e a detecção de uma receita corrompida simulada para testar o Modo Investigação.
---