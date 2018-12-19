import pprint


def count_matrix(result_arr, i, j, k, l):
    count = 0
    for raw in range(i, k+1):
        for col in range(j, l+1):
            if result_arr[raw][col] == 1:
                count += 1
            else:
                return 0
    return count


if __name__ == '__main__':
    result_arr = []

    try:
        while True:
            i = input()
            sub_arr = list(map(int, i.strip().split(' ')))
            result_arr.append(sub_arr)
    except EOFError:
        pass
    except ValueError:
        pass
    max_arr = []
    # 暴力统计所有子矩阵情况
    for i in range(len(result_arr)):
        for j in range(len(result_arr[0])):
            for k in range(i, len(result_arr)):
                for l in range(j, len(result_arr[0])):
                    max_arr.append(count_matrix(result_arr, i, j, k, l))

print(max(max_arr))