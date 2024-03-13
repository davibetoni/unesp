#include <string.h>
#include <stdio.h>

int main(){
    char expressao[1001];
    char parenteses[1001];
    int i, j, tam;

    while(scanf("%s", &expressao) != EOF){
        tam = strlen(expressao);
        j = 0;
        
        for(i = 0; i < tam; i++){
            if(expressao[i] == '('){
                parenteses[j] = expressao[i];
                j++;
            } else if(expressao[i] == ')'){
                if(j > 0){
                    j--;
                }
                else {
                    break;
                }                
                
            }
        }

        if(i == tam && j == 0) {
            printf("correct\n");
        }
        else{
            printf("incorrect\n");
        }
    }

    return 0;
}