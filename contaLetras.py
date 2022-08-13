
#somente contar letras
text= input()
dict= {}
#para cada letra no texto, fazer...
for i in text:
  if i in dict:
    dict[i] +=1
  else:
    dict[i]=1
print(dict)    

###############################################################################################################
"""prog2"""
###############################################################################################################
#contar letras, output freq letras e a mais frequente.

def main():
     print(contaletras(input(":")))

     
def contaletras(s) :
     F={}   
      #para cada letra em string...
     for letra in s:
         if letra in F:
            F[letra] +=1
         else:
            F[letra]=1
     letramaisf=""
     maiorfreq=0
     for letra in F:
         if (F[letra]>maiorfreq):
          letramaisf=letra
          maiorfreq=F[letra]
     return F, letramaisf

main()          


###############################################################################################################
""""prog3"""
###############################################################################################################
##printar na tela em ordem, as palavras mais frequentes, seguido de seu número de repeticoes

