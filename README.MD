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

# /etc/shadow
O arquivo /etc/shadow no linux armazena as senhas hasheadas para cada usuário
do sistema.
 
O padrão da criptografia das entradas no arquivo /etc/shadow é o seguinte:

`<USER>:$<COD_FUNCAO_HASH>$<SALT>$<HASH>`

Salt é uma string aleatorizada que é somada à senha na hora de criar o hash. Com
esse método evita-se que uma senha comum, como 12345, tenha um hash igual e
não seja possível criar um dicionário de equivalência senha-hash.

## ENTRADAS DADAS:
Pimpolho:
$y$j9T$nFwHNF0c3SCbH6ESyzSKw.
$ph1Q6UMJnIyAU6O7ZLYH14H5C4.V1SJjcrjLqVQuG00:19472:0:99999:7:::

testeadm:
$y$j9T$5LImmws2fco9AeRmLSB2j0$fYPmdqu1Q/
FDiwPJgkCIW9wX76w12SNEiYAodUzafo5:19472:0:99999:7:::

   User  |              salt             |                  hash                      
-------- | ----------------------------- | -------------------------------------------
Pimpolho | $y$j9T$nFwHNF0c3SCbH6ESyzSKw  | ph1Q6UMJnIyAU6O7ZLYH14H5C4.V1SJjcrjLqVQuG00
testeadm | $y$j9T$5LImmws2fco9AeRmLSB2j0 | fYPmdqu1QFDiwPJgkCIW9wX76w12SNEiYAodUzafo5



