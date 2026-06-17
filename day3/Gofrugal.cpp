#include <stdio.h>

int main() {
    int decimal_num;
    int binary_array[32]; // Array to store binary digits
    int index = 0;
    int count_ones = 0;

    // Prompt user for input
    printf("Enter a decimal number: ");
    if (scanf("%d", &decimal_num) != 1) {
        printf("Invalid input\n");
        return 0;
    }

    // If the number is 0 or negative, it will not contain any 1's in standard positive binary
    if (decimal_num <= 0) {
        printf("Invalid input\n");
        return 0;
    }

    // Convert decimal to binary
    int temp = decimal_num;
    while (temp > 0) {
        binary_array[index] = temp % 2;
        
        // Count the number of 1's
        if (binary_array[index] == 1) {
            count_ones++;
        }
        
        temp = temp / 2;
        index++;
    }

    // Final safety check: if count of 1's is somehow 0
    if (count_ones == 0) {
        printf("Invalid input\n");
        return 0;
    }

    // Print the binary representation (in reverse order)
    printf("Binary representation: ");
    for (int i = index - 1; i >= 0; i--) {
        printf("%d", binary_array[i]);
    }
    printf("\n");

    // Print the count of 1's
    printf("Count of 1's: %d\n", count_ones);

    return 0;
}
