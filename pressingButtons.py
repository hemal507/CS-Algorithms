def pressingButtons(buttons):
    num_dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    recur_list = []
    for n in buttons:
        recur_list = [i + j for i in recur_list or [""] for j in num_dict[n] ]
    return recur_list
print(pressingButtons("8888"))
