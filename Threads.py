def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n
 
 
def main(args):
    n= sys.argv[1]   #extraimaos o parâmetro de entrada
     
     
     
    saida= []        #nesta lista iremos inserir a série calculada
           
    print ('Espere- calculando...')
    tamanho= int(n)  # o parâmetro veio como string, trasnformamos em inteiro
         
       
    for i in range(tamanho):     # calculamos todos os parâmetros
        saida.append(rec_fib(i))     # e inserimos na lista
     
    valores_csv = ','.join(map(str, saida))  #convertemos os itens na lista em strings
    print (valores_csv)  #imprimimos a string resultante
  
     
    return 0
 
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))