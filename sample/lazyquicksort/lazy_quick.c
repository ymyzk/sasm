#include <stdio.h>
#include <stdlib.h>

const int LAZY = 10;

void lazy_quick(int nums[], int len) {
    int left = 0, stack[100], pos = 0;
    for ( ; ; ) {
        if ((len - left) > LAZY) {
            for (; left + 1 < len; len++) {
                int pivot = nums[left];
                stack[pos++] = len;
                for (int right = left - 1; ; ) {
                    while (nums[++right] < pivot);
                    while (pivot < nums[--len]);
                    if (right >= len) break;
                    int temp = nums[right];
                    nums[right] = nums[len];
                    nums[len] = temp;
                }
            }
        }
        if (pos == 0) break;
        left = len;
        len = stack[--pos];
    }
}

void lazy_quick_asm(int nums[], int len) {
    int left = 0;
    int right;
    int stack[100];
    int *bp = stack;
    int *sp = bp;
    int pivot;
    int temp1, temp2;

loop_a:
    temp1 = len - left;
    temp2 = LAZY;
    if (temp1 <= temp2) goto loop_b_out;
loop_b:
    temp1 = left;
    temp1++;
    if (len <= temp1) goto loop_b_out;

    // Pivot
    pivot = nums[left];
    // Push
    *sp = len;
    sp++;
    right = left - 1;
loop_c:
loop_d1:
    right++;
    temp1 = nums[right];
    if (temp1 < pivot) goto loop_d1;
loop_d2:
    len--;
    temp2 = nums[len];
    if (pivot < temp2) goto loop_d2;

    if (len <= right) goto loop_c_out;

    nums[right] = temp2;
    nums[len] = temp1;
    goto loop_c;
loop_c_out:
    len++;
    goto loop_b;
loop_b_out:
    if (bp == sp) goto loop_a_out;
    left = len;
    // Pop
    sp--;
    len = *sp;
    goto loop_a;
loop_a_out:
    return;
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
    lazy_quick_asm(nums, length);
    print(n, length);
    return 0;
}
