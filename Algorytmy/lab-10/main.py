def lcs(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)

    tab = [[0 for _ in range(len_str2 + 1)] for _ in range(len_str1 + 1)]

    # Building the mtrix in bottom-up way
    for i in range(len_str1 + 1):
        for j in range(len_str2 + 1):
            if i == 0 or j == 0:
                tab[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                tab[i][j] = tab[i - 1][j - 1] + 1
            else:
                tab[i][j] = max(tab[i - 1][j], tab[i][j - 1])

    index = tab[len_str1][len_str2]

    lcs_algo = [""] * (index + 1)
    lcs_algo[index] = ""

    i = len_str1
    j = len_str2
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs_algo[index - 1] = str1[i - 1]
            i -= 1
            j -= 1
            index -= 1

        elif tab[i - 1][j] > tab[i][j - 1]:
            i -= 1
        else:
            j -= 1

    for x in tab:
        print(x)

    # Printing the sub sequences
    print(f"S1 : {str1}" + "\nS2 : " + str2)
    print("LCS: " + "".join(lcs_algo))


S1 = "ACADB"
S2 = "CBDA"
lcs(S1, S2)
