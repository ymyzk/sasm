#include <stdio.h>
#include <stdlib.h>

const int LAZY = 10;

void insertion(int nums[], int len) {
    for (int i = 1; i < len; i++) {
        int tmp = nums[i];
        if (nums[i-1] > tmp) {
            int j = i;
            do {
                nums[j] = nums[j-1];
                j--;
            } while (j > 0 && nums[j-1] > tmp);
            nums[j] = tmp;
        }
    }
}

void insertion_asmx(int nums[], int len) {
    int i = 1;
    int j;
    int temp1, temp2;

    for (; i < len;) {
        temp1 = nums[i];
        temp2 = nums[i - 1];
        if (temp2 > temp1) {
            j = i;
            do {
                nums[j] = temp2;
                j--;
                temp2 = nums[j - 1];
            } while (j > 0 && temp2 > temp1);
            nums[j] = temp1;
        }
        i++;
    }
}

void insertion_asm(int nums[], int len) {
    int i = 1;
    int j;
    int temp1, temp2;

insertion_outer:
    temp1 = nums[i];
    temp2 = nums[i - 1];

    if (temp2 <= temp1) goto insertion_if;

    j = i;

insertion_inner:
    nums[j] = temp2;
    j--;
    temp2 = nums[j - 1];
    if (j > 0 && (temp2 > temp1)) goto insertion_inner;

    nums[j] = temp1;

insertion_if:
    i++;
    if (i < len) goto insertion_outer;
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
    insertion_asm(nums, length);
    print(n, length);
    return 0;
}
