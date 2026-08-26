#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* my_string, int** queries, size_t queries_rows, size_t queries_cols) {
    // 1. 문자열의 길이를 구합니다.
    size_t len = strlen(my_string);
    
    // 2. 결과를 반환할 메모리를 동적 할당하고(널 문자 공간 +1 포함), 내용을 복사합니다.
    char* answer = (char*)malloc(len + 1);
    strcpy(answer, my_string);
    
    // 3. queries의 각 행을 순회합니다.
    for (size_t i = 0; i < queries_rows; i++) {
        int s = queries[i][0];
        int e = queries[i][1];
        
        // 4. s부터 e까지의 구간을 서로 교환하며 뒤집습니다.
        while (s < e) {
            char temp = answer[s];
            answer[s] = answer[e];
            answer[e] = temp;
            s++;
            e--;
        }
    }
    
    return answer;
}