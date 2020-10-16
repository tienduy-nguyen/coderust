def permute_string(str):
    res = []
    dfs(str, "", res)
    return res


def dfs(str, path, res):
    if not str:
        res.append(path)
        return res
    for i in range(len(str)):
        dfs(str[:i] + str[i + 1 :], path + str[i], res)


print(permute_string("abc"))
