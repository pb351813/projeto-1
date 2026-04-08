# projeto-1
esse projeto calcula a mesada final, a media das mesadas e o valor acumulado com base na mesada inicial, no aumento mensal e numero de meses
este projeto e feito em linguagem c



#include<stdio.h>

int main(){

    float mesada_inicial;
    float mesada_final;
    float mesada_acumulada;
    float aumento;
    float media;
    int meses;
    
    printf("qual o valor inicial da mesada");
    scanf("%f", &mesada_inicial);

    printf("qual o aumento mensal da mesada");
    scanf("%f", &aumento);

    printf("qual o numero de meses");
    scanf("%d", &meses);
    
   float aumento_total=aumento*meses; 
   mesada_final=aumento_total+mesada_inicial;
   media=(mesada_final+mesada_inicial)/2;
   mesada_acumulada=(media*meses)/2;
   
   printf("o valor da mesada final e de %.2f \n", mesada_final);
   printf("o valor da media das mesadas e de %.2f \n", media);
   printf("o valor acumulado das mesadas e de %.2f \n", mesada_acumulada);
   
   
   return 0;
}
