if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    uni = set(arr)
    sort_uni = sorted(uni)
    print(sort_uni[len(sort_uni) - 2])

    # if sorted_arr[len(sorted_arr) -1] == sorted_arr[len(sorted_arr) - 2] :
    #     print(sorted_arr[len(sorted_arr)-3])
    # else :
    #     print(sorted_arr[len(sorted_arr)-2])

