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


## QUEBRANDO AS SENHAS
No diretório ex2, há um arquivo que usa um algoritmo de bruteforce para tentar 
quebrar alguma entrada no padrão da /etc/shadow. Usando esse arquivo, foi 
possível observar que usar bruteforce é computacionalmente muito custoso e é um
método extremamente limitado pela capacidade de processamento do computador.

Um dos testes seguiu os seguintes passos:
- Considerar somente números e letras minúsculas como caracteres válidos na 
senha, totalizando 36 caracteres disponíveis

- Tentar quebrar a senha "000", contida no arquivo pass_teste000

Para uma senha de tamanho n, o algoritmo precisa hashear e comparar todas as 
strings possíveis de tamanho 1 até n, sendo que o total de senhas pode ser
aproximado por:

`36¹ + 36² + 36³ + ... + 36^n`

Percebe-se que, por ser um cálculo exponencial, cada aumento da quantia de chars
por senha aumenta muito significativamente a quantia total de senhas testadas. 

Além disso, se for considerado letras maiúsculas e símbolos, o cálculo utilizaria
90 como base, e não 36, aumentando ainda mais a quantia de senhas possíveis.
Por exemplo, para uma senha com letras minúsculas e números com 5 caracteres, o
total de senhas testadas é aproximadamente 62 milhões

Outro problema desse algoritmo é que as senhas são armazenadas em hash do tipo
yescrypt, a execução da criptografia nesse padrão também é computacionalmente 
custosa, dessa forma, além do custo de gerar e comparar cada uma das senhas
possíveis, perde-se também um absurdo de tempo se comparado com outros métodos
de hasheamento

A senha "000" é a primeira string gerada com 3 caracteres, ou seja, antes dela
são testadas somente todas as de 1 caracter e todas de 2 caracteres. O total é 
de 1332 senhas, esse teste demorou 17 segundos para ser executado em um 
processador intel i7 de 7ª geração. Também foi testada a senha "0000" mas o 
teste foi interrompido antes do fim por causa da quantia de tempo que ficou 
executando sem sucesso.

Também foi realizado um teste sobre a entrada do usuário testeadmin, onde já se
sabia que a senha era "123admin", tendo 8 letras. O programa foi alterado para 
testar somente strings com 8 caracteres para acelerar o processo, mesmo assim, a
quantia de espaço em memória que o algoritmo ocupou com a geração de todos os 
combinatórios possíveis fez com que o sistema operacional matasse o processo

Com esses teste, é seguro dizer que uma senha com letras maiúsculas e minúsculas
, dígitos e símbolos com uma quantia razoável de caracteres (7 ou mais), é 
praticamente impossível de ser quebrada com um algoritmo bruteforce

# ARQUIVOS
Todos os arquivos desse trabalho estão disponíveis em:

`github.com/Guiusa/password-crack`
