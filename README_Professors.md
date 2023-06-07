# Instruções para Professores e Monitores

Para utilizar esse projeto da forma que ele foi idealizado crie as atividades seguindo o [GitHub Classroom](https://classroom.github.com/).
Crie também uma nova organização associada ao seu usuário, para não misturar repositórios de exercícios de alunos com os seus próprios repositórios.
Ao criar uma `classroom` use a organização criada.

## Gratuidade do `GitHub Pro`

Caso não tenha conta do tipo profissional no `GitHub`, peça a gratuidade via [Docs-Github](https://docs.github.com/en/billing/managing-billing-for-your-github-account/discounted-subscriptions-for-github-accounts).
Não esqueça de fazer o pedido também para a organização criada, pois ela é considerada diferente da sua conta principal.

A gratuidade permite que os testes dos alunos sejam rodados em repositórios privados com um limite de até `2k` minutos por mês.

## `GitHub Classroom`

A documentação do `GitHub Classroom` pode ser encontrada [aqui](https://docs.github.com/en/education).


## Testes Automáticos

A parte da documentação referente ao uso de testes automatizados pode ser vista [aqui](https://docs.github.com/en/education/manage-coursework-with-github-classroom/teach-with-github-classroom/use-autograding).

De forma mais resumida, colocando como commando `python -m unittest` é o suficiente para rodar todos os testes dos exercícios.

Caso mais granularidade ao realizar os testes seja necessário, é possível rodar os testes individualmente.
Por exemplo, o comando `python -m unittest test.test_main` roda somente o arquivo `test_main.py` desse repositório.
O comando `python -m unittest test.test_example_module.TestExampleModule.test_soma` roda somente o método `test_soma` da classe `TestExampleModule` do arquivo `test_example_module.py` da pasta `test`.

Assim, é possível associar notas diferentes e pesos diferentes para cada teste individualmente.

## Rodar Localmente os Trabalhos

Para evitar rodar código diretamente na máquina é recomendável utilizar um container para isolar a execução do código dos alunos do restante da máquina.
Isso também resolve o problema de instalar dependências.

O requisito necessário é ter o [docker](https://www.docker.com/) instalado.

Para criar uma imagem do repositório basta fazer o comando no diretório raiz do repositório desejado:

```bash
docker build -t python-exercise-from-student .
```

Para rodar a imagem com o comando padrão `python main.py` basta fazer:

```bash
docker run --rm -it python-exercise-from-student
```

Para rodar um comando específico, por exemplo `python -m unittest` depois de criar a imagem:

```bash
docker run --rm -it --entrypoint python python-exercise-from-student -m unittest
```

## Limite de Minutos das Ações

Caso queira rodar as ações do GitHub mesmo depois dos minutos estourarem, existem duas possibilidades.

1. Tornar os repositórios públicos via `GitHub Classroom`.
2. Usar o [act](https://github.com/nektos/act) para rodar as ações localmente.