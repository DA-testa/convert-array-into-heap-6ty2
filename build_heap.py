# python3


def build_heap(inf):
    swaps = []
    size = len(inf)
    for i in range(size//2,-1,-1)
        SitaLieta(data, i, swaps)
    return swaps

    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    return swaps

def SitaLita(data, i, swaps):
        size = len(inf)
        min_data = i
        oneanother = 2 * i + 1
        twoanother = 2 * i + 2
        if oneanother < size and inf[oneanother] < inf[min_data]:
            min_data = oneanother
    

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
