def minDistance(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    lcs_matrix = [[0 for i in range(len1+1)] for j in range(len2+1)]
    for i in range(len2):
        row_index = i + 1
        for j in range(len1):
            column_index = j + 1
            if word2[i] == word1[j]:
                lcs_matrix[row_index][column_index] = lcs_matrix[row_index-1][column_index-1] + 1
            else:
                lcs_matrix[row_index][column_index] = max(lcs_matrix[row_index-1][column_index],lcs_matrix[row_index][column_index-1])
    return len1 + len2 - lcs_matrix[-1][-1] * 2

word1 = '13456778'
word2 = '357486782'
minDistance(word1,word2)