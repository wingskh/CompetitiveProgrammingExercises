#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	int numOfCases, i, numOfStone, j, colorA, colorB;
    FILE * fp = fopen ("./alchemy_input.txt", "r");
    char color;

    if(fp != NULL){
        fscanf(fp, "%d\n", &numOfCases);
        for(i = 0; i < numOfCases; i++){
            fscanf(fp, "%d\n", &numOfStone);
            colorA = 0;
            colorB = 0;
            for(j = 0; j < numOfStone; j++){
                fscanf(fp, "%c", &color);
                if(color == 'A'){
                    colorA++;
                }else if(color == 'B'){
                    colorB++;
                }
            }
            if(abs(colorB-colorA) == 1){
                printf("Case #%d: Y\n", i+1);
            }else{
                printf("Case #%d: N\n", i+1);
            }
        }
    }


    fclose(fp);
	return 0;
}