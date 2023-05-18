# QUEBRANDO HASHED PASSWORDS COM PYTHON USANDO DICIONÁRIO

## ALGORITMO

Para cada linha do dicionário, é usada a biblioteca *hashlib* do python para
codificar a palavra em md5, depois, compara-se com a hash da senha a ser
quebrada e, se forem iguais, o programa é finalizado.

## EFICIÊNCIA

Se o tamanho da senha original for sabido, é possível acelerar o processo
conforme o código:

```
for word in dictionary
	if len(word) == size
		if(word.hashed == password)
			return
```

Nesse caso, realizar a operação hash é mais pesado do que comparar o tamanho
da palavra, então vale a pena testar o tamanho antes de codificar cada palavra.
Para o caso do problema, sabendo que a senha tem 5 caracteres foi possível
atingir um speedup de aproximadamente 40x.

## USO DO SCRIPT

O script python pode ser executado com
`python breakpass.py`
Mas ele foi escrito pra receber até 3 parâmetros:

`python breakpass.py [-d --dictionary] [-s --size] [-p --password]`

**dictionary** especifica o caminho para o arquivo texto com o dicionário.
Por padrão, dictionary procura pelo arquivo "dic.txt" no diretório corrente

**size** especifica o tamanho da senha.
Por padrão, esse tamanho é 0 e faz com que o script teste todas as palavras no
dicionário

**password** especifica o caminho do arquivo que contém a senha hasheada.
Por padrão, password procura pelo arquivo "pass" no diretório corrente

