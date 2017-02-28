# selic
Selic Calculator
Starwars: http://www.kammerl.de/ascii/AsciiSignature.php

<pre>
   _______. _______  __       __    ______ 
    /       ||   ____||  |     |  |  /      |
   |   (----`|  |__   |  |     |  | |  ,----'
    \   \    |   __|  |  |     |  | |  |     
.----)   |   |  |____ |  `----.|  | |  `----.
|_______/    |_______||_______||__|  \______|
</pre>
                        
<br>

<hr>

Selic Calculator é uma experiencia com linguagem python, escrita para ser executado em terminal linux, para calcular a selic sobre o valor estimado no tempo definido. Uma estimativa de investimentos sobre o valor acumulado (juros em cima de juros).

# INSTRUÇÃO

#Para compilar local: 
<p>python selic.py -h</p>
<p>ou</p>
<p>chmod 777 selic.py</p>
<p>./selic.py -h</p>

#Para inserir na varivel de ambiente:
1. Copie/mova para a pasta selic [crie mkdir /usr/bin/selic] em /usr/bin/
2. Insira na variável $PATH : export PATH=$PATH:/usr/bin/nix/
3. Certifique-se que foi inserida: echo $PATH
4. Teste em qualquer diretrio digitando: ./selic.py -h ou python selic.py --help

Variaveis de ambiente permanentes:<br>
<p>sudo nano /etc/bash.bashrc</p>
<p>nano .bashrc</p>
<p>Ou dinamize isso conforme suas necessidades</p>

<hr>

#Comandos iniciais
<pre>
	   Selic Calculator sel 0.1 (c) 2017 Lameck
       https://github.com/lamecksf/selic

       usage: python selic.py [options]

       ##########################################
                     SELIC CALCULATOR:
       ##########################################

         --rate Interest rate per month
         --inv    Investment 
         --month Number of Month 
         --acc <n|y> Accumulative yes or no 

       python selic.py --rate 0.5 --inv 570 --month 12 --acc y 
</pre>


<hr>

#SUPORTE

V0.1:
O tempo e a selic estão transformados em valores mensais. É necessário confirmar a selic anual e divid-la para o tempo de cálculo 
Esta verso suporta apenas a moeda brasileira atual - real (R$)
A verso do retorno  português-br
