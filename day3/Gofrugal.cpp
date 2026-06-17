#include <stdio.h>

int main() {
    int decimal_num;
    int binary_array[32]; 
    int index = 0;
    int count_ones = 0;
    printf("Enter a decimal number: ");
    if (scanf("%d", &decimal_num) != 1) {
        printf("Invalid input\n");
        return 0;
    }
    if (decimal_num <= 0) {
        printf("Invalid input\n");
        return 0;
    }

    int temp = decimal_num;
    while (temp > 0) {
        binary_array[index] = temp % 2;
        
        if (binary_array[index] == 1) {
            count_ones++;
        }
        
        temp = temp / 2;
        index++;
    }
    if (count_ones == 0) {
        printf("Invalid input\n");
        return 0;
    }
    printf("Binary representation: ");
    for (int i = index - 1; i >= 0; i--) {
        printf("%d", binary_array[i]);
    }
    printf("\n");
    printf("Count of 1's: %d\n", count_ones);

    return 0;
}
