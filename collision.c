#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

char *generate_random_string(int length) {
    static char charset[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    char *randomString = NULL;

    if (length > 0) {
        randomString = malloc(length + 1);

        if (randomString) {
            for (int i = 0; i < length; i++) {
                int key = rand() % (sizeof(charset) - 1);
                randomString[i] = charset[key];
            }
            randomString[length] = '\0';
        }
    }

    return randomString;
}

unsigned long make_sum(void){

  char *key = generate_random_string(20);

  char s1[5] = {key[0],key[1],key[2],key[3],'\0'};
  char s2[5] = {key[4],key[5],key[6],key[7],'\0'};
  char s3[5] = {key[8],key[9],key[10],key[11],'\0'};
  char s4[5] = {key[12],key[13],key[14],key[15],'\0'};
  char s5[5] = {key[16],key[17],key[18],key[19],'\0'};


    unsigned int v1 = strtol(s1,NULL,40);
    unsigned int v2 = strtol(s2,NULL,40);
    unsigned int v3 = strtol(s3,NULL,10);
    unsigned int v4 = strtol(s4,NULL,10);
    unsigned int v5 = strtol(s5,NULL,10);

    unsigned long value = v1 + v2 + v3 + v4 + v5;

  return value;
}

int main(){

  unsigned long key = 568134124;
  unsigned long test = 0;

  while(1){
    unsigned long sum = 0;
    sum = make_sum();
    printf("Suma: %lu \n",sum);
    if(sum == key){
      printf("THE KEY IS %lu",sum);
      break;
    }
  }
return 0;
}
