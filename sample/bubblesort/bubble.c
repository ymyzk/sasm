#include <stdio.h>
#include <stdlib.h>

void bubble(int nums[], int length) {
    for (int i = length - 1; 0 < i; i--) {
        for (int j = 1; j <= i; j++) {
            if (nums[j] < nums[j - 1]) {
                int tmp = nums[j];
                nums[j] = nums[j - 1];
                nums[j - 1] = tmp;
            }
        }
    }
}

void bubble_asm(int nums[], int length) {
    int *i, *j;
    int tmp1, tmp2;
    length = length - 1;
    i = nums + length;

outer:
    j = nums + 1;
inner:
    tmp1 = *(j - 1);
    tmp2 = *j;
    if (tmp1 <= tmp2) goto noswap;
    *(j - 1) = tmp2;
    *j = tmp1;
noswap:
    j++;
    if (j <= i) goto inner;

    i--;
    if (nums < i) goto outer;
}

void print(int nums[], int length) {
    int i;
    for (i = 0; i < length; i++) {
        printf(" %d", nums[i]);
    }
}

int main(void) {
    int nums[100];
    int length = 100;
    int *n = nums;
    for (int i = 0; i < length; i++) {
        nums[i] = (int)(rand() * (1000 + 1.0) / (1.0 + RAND_MAX));
    }
    bubble_asm(nums, length);
    print(n, length);
    return 0;
}
