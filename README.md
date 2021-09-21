# Projeto 1: Parte A
Durante o primeiro handout nós desenvolvemos o Get-it com as funcionalidades de listagem e criação de anotações. No Desafio CSS você implementou um possível estilo para a página. No segundo handout, você aprendeu (ou aprenderá, dependendo de quando estiver lendo este enunciado) a armazenar e recuperar dados de um banco de dados SQLite. Agora, no Projeto 1A, o seu objetivo é aplicar o que aprendeu nos handouts e no desafio para adicionar as seguintes funcionalidades ao sistema:

1. Estilo da página (utilizando o CSS que você já fez ou adicionando um novo estilo);
2. Editar anotações
3. Apagar anotações
4. Armazenamento em banco de dados SQLite ao invés de um arquivo texto

Ao final do Projeto 1A será possível criar uma anotação, ler os dados de anotações armazenadas no arquivo (que simula o banco de dados), atualizar uma anotação e apagar uma anotação. Esse é um conjunto de operações bastante comum em sistemas e é conhecido como CRUD (Create, Read, Update, Delete).

É comum ouvirmos no ambiente de trabalho que será necessário montar um CRUD. E agora você sabe o que isso quer dizer! Ao final deste semestre você deve ser capaz de montar CRUDs sem que isso seja um grande trauma. Esse conhecimento será necessário antes mesmo de se formarem: nas disciplinas de Computação em Nuvem e Megadados, ambas no 6o semestre, os professores assumirão que vocês são capazes de colocar um CRUD no ar sem muito esforço. Por isso, é importante que vocês se empenhem nas atividades de Tecnologias Web.

Rubrica
As 4 tarefas a serem realizadas são:

1. Implementar o estilo da página (de todas, caso sejam feitas páginas adicionais);
2. Permitir a edição de anotações existentes (você pode escolher se vai fazer uma nova página para isso ou fazer tudo na mesma página - já aviso que é mais difícil);
3. Permitir que o usuário apague uma anotação (o comentário do item anterior também vale aqui);
4. Implementar a persistência dos dados com SQLite (você deve escrever o SQL na mão, ou seja, não pode utilizar bibliotecas de ORM ou similares).

# Projeto 1: Parte B

Na parte A você implementou o servidor em Python sem a ajuda de nenhum framework. Nesta segunda parte, o objetivo é reimplementar as funcionalidades da parte A utilizando o Django. Além disso, vamos expandir as funcionalidades do sistema, utilizar um banco de dados mais robusto do que o SQLite e finalmente publicar o nosso sistema. Dependendo de quando você estiver lendo este enunciado, você ainda não saberá como fazer todas essas coisas, mas nós teremos alguns handouts para te auxiliar nesse processo.

## Reimplementando Projeto 1A usando Django

Reimplementar o CRUD da parte A em Django, ou seja, implementar as funcionalidades de criação, listagem, edição e remoção de anotações.

Para esta etapa o ideal é utilizar a estrutura que o framework dispõe. Como discutido na aula 08, utilize mais de uma rota para mapear as diferentes requisições que o cliente pode enviar ao servidor.

## Sistema de tags

Na parte B você deve implementar um sistema de tags para as anotações. Cada anotação pode ter no máximo uma tag (pode não ter nenhuma).

No formulário de criação/edição de anotações deve haver um campo de texto adicional para o usuário digitar o nome da tag. No backend (no view.py), se essa tag já existir, você deve associar a anotação a ela, senão, crie uma nova tag no banco de dados e associe à anotação.

Você também precisa criar mais duas páginas: uma com a lista com todas as tags existentes e outra com as anotações de uma determinada tag. A lista das tags deve mostrar apenas os nomes das tags com um link para a sua respectiva página de detalhes. A página de detalhes de uma tag deve mostrar o nome da tag e todas as anotações com aquela tag específica.

Rubrica
As tarefas a serem realizadas são:

1. Reimplementar o CRUD da parte A em Django, ou seja, implementar as funcionalidades de criação, listagem, edição e remoção de anotações aplicando o mesmo estilo (css);
2. Utilizar o PostgreSQL (em um container Docker) ao invés do SQLite;
3. Implementar o sistema de tags para as anotações;
4. Publicar a página.