/*John is working in a diamond mine, trying to extract the highest number of diamond "<>". He must exclude all sand particles found "."
in this process and after a diamond can be extracted, new diamonds can be formed. If he has as an input. <... << .. >> ....> .... >>>. 
three diamonds are formed. The first is taken from <..> resulting. <... <> ....> .... >>>. The second diamond is then removed, 
leaving. <.......> .... >>>. The third diamond is then removed, leaving at the end ..... >>>. without the possibility of 
extracting new diamonds.

Input
Read an integer N that is the number of test cases. Then follows N lines each up to 1000 characters, including "<" ,">" and "."

Output
You must print the amount of diamonds that can be extrated in each test case.*/

#include <stdio.h>
#include <string.h>

int main() {
    int n, i, j, diamonds;
    int k = 0;
    char end[1001];
    char str[1001];

    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        scanf("%s", str);
        diamonds = 0;
        for (j = 0; j < strlen(str); j++) {
            if(str[j] == '<'){
                k++;
            }
            else if(str[j] == '>' && k > 0){
                end[k] = '>';
                diamonds++;
                k--;
            }
        }
        printf("%d\n", diamonds);
        k = 0;
    }
    return 0;
}
