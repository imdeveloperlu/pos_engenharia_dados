# -*- coding: utf-8 -*-
"""Bibliotecas de manipulação e visualização de dados_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BpAdbzEP7EbF7R3tia86-2EVF0Nf9Qab
"""

#importando e colunas específicas e renomeando as mesmas
import pandas as pd
notas = pd.read_csv('Notas.csv', sep = ';',
                   usecols = [0, 1], names = ['NomeAluno', 'NotaD1'])
notas

notas = pd.read_csv('Notas.csv', sep = ';', usecols = ['Aluno', 'D3'])
notas

notas = pd.read_csv('Notas.csv', sep = ';')
notas
# Verificando linhas duplicadas
notas.duplicated()

# Removendo linhas duplicadas
notas.drop_duplicates(inplace = True)

notas

alunos = {'nome' : ['João', 'Maria', 'Carlos', 'Silvia', 'André', 'Juliana', 'Alex'],
          'RA': [1000, 2000, 3000, 4000, 2700, 6000, 1000],
          'sexo': ['M', 'F', 'M', 'F', 'M', 'F', 'M'],
          'nota': [80.0, 90.0, 75.0, 100.0, 96.5, 98.5, 90]
         }
df = pd.DataFrame(alunos)
df

# Verificando as linhas que possuem RA duplicado
df.duplicated(subset = ['RA'])

# Exibindo uma cópia do DataFrame as linhas que possuem RA duplicado
df.drop_duplicates(subset = ['RA'])

# Removendo as linhas que possuem RA duplicado
df.drop_duplicates(subset = ['RA'], inplace = True)
df

import pandas as pd
notas = pd.read_csv('Notas.csv', sep = ';')
#Exibindo somente as colunas Aluno e D3
notas[['Aluno', 'D3']]

#Exibindo os alunos que obtiveram nota D3 > 10
notas[(notas.D3 > 10)]

#Exibindo o nome dos alunos, e as notas D1 e D3,  para aqueles que obtiveram D3 maior que 10 e D1 menor que 10
notas[(notas['D3'] > 10) & (notas['D1'] < 10)][['Aluno', 'D3']]
#notas[(notas.D3 > 10) & (notas.D1 < 10)][['Aluno', 'D3']]

# Utilizando o método query
notas.query('D3 > 10 and D1 < 10')[['Aluno', 'D3']]

import pandas as pd
notas = pd.read_csv('Notas_Curso.csv')
# Ordenando os dados pelo nome do Aluno
notas.sort_values(by = 'Aluno')

# Ordenando os dados pelo nome do Aluno em ordem decrescente
#notas.sort_values(by = 'Aluno', ascending = False)

# Ordenando os dados pelo nome do Curso e do Aluno, em ordem crescente
notas.sort_values(by = ['Curso','Aluno'])

# Ordenando os dados pelo nome do Curso em ordem decrescente, e do Aluno, em ordem crescente
notas.sort_values(by = ['Curso','Aluno'], ascending = [False, True])

import pandas as pd
notas = pd.read_csv('Notas_Curso.csv')

# Quantidade de linhas por curso
notas['Curso'].value_counts()

# Quantidade de linhas por sexo
notas['Sexo'].value_counts()

# Quantidade de alunos por curso e sexo
notas.groupby(['Curso', 'Sexo'])['Aluno'].count()

# Média das notas por curso e sexo
notas.groupby(['Curso', 'Sexo']).mean()

import pandas as pd

notas = pd.read_csv('Notas.csv', sep = ';')

# Excluindo as linhas que possuem valores nulos somente na coluna D2
notasD2 = notas.dropna(subset = ['D2'])

# Removendo as linhas duplicadas
notasD2.drop_duplicates(inplace = True)

notasD2

# Gravando um DataFrame em um arquivo CSV
# Com a opção index = False, não será criada uma coluna para os índices do DataFrame
notasD2.to_csv('Copia_notas.csv', index = False)

# Importando dados a partir de uma url
import pandas as pd
temperatura = pd.read_csv('https://github.com/alanjones2/dataviz/raw/master/londonweather.csv')

temperatura

import pandas as pd

notas = pd.read_csv('Notas_Curso.csv')
notas

# Plotando gráfico de quantidade de alunos por Curso
#notas['Curso'].value_counts().plot()

notas['Curso'].value_counts().plot(kind = 'bar', title = 'Alunos por Curso').set(xlabel='Curso', ylabel='Qtd Alunos')

temp = pd.read_csv('Temperatura.csv', sep = ';')

temp.sample(5)

#temp.groupby('cidade')['temperatura'].mean().plot(kind = 'bar')

t = temp[(temp.cidade == 'Belo Horizonte') & (temp.data_coleta >= '21/01/2020') & (temp.data_coleta <= '25/01/2020')]

t.plot(kind='line',x='data_coleta',y='temperatura', title = 'Temperatura de BH').set(xlabel='Dia', ylabel='Temperatura')