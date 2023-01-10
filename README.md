# SincronizacaoProcessos


Esta atividade é para resolver a programação concorrente,questão de acesso por processos,
memória compartilhada, que por sua vez é a chamada de sessão crítica.
A sessão crítica tem a possibilidade de gerar certas duplicidades nos resultados, pois
ao mesmo tempo que uma thread escreve em um local da memória, outra lê este local,buscando
muitas vezes o dado desatualizado.
Uma das formas de correção para isso é a utilização do semáforo,uma variável capaz de 
informar se a sessão crítica está sendo utilizada por um processo ou não.Neste caso, 
apenas quando estiver livre que outro processo poderá utilizá-la.

![Semaphore ERRO](https://user-images.githubusercontent.com/88063740/211684313-0a949b46-cb12-46a0-8fda-ef35367c6df5.png)


![Semaphore Resolvido](https://user-images.githubusercontent.com/88063740/211684329-295ce2b1-191a-425f-b24d-989f8a165bc3.png)
