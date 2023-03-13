# python3


#def build_heap(inf):
#   swaps = []
#   size = len(inf)
#   for i in range(size//2,-1,-1)
#       SitaLieta(data, i, swaps)
#   return swaps

    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

#   return swaps

#def SitaLita(data, i, swaps):
#       size = len(inf)
#       min_data = i
#       oneanother = 2 * i + 1
#       twoanother = 2 * i + 2
#       if oneanother < size and inf[oneanother] < inf[min_data]:
#           min_data = oneanother
    

#def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
#   n = int(input())
#   data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
#   assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
#   swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
   #print(len(swaps))
   #for i, j in swaps:
   #   print(i, j)


#if __name__ == "__main__":
#  main()

#---------------------------------------------------------

# # def sift_down(arr, i, swaps):
#     n = len(arr)
#     min_idx = i
#     l = 2 * i + 1
#     if l < n and arr[l] < arr[min_idx]:
#         min_idx = l
#     r = 2 * i + 2
#     if r < n and arr[r] < arr[min_idx]:
#         min_idx = r
#     if i != min_idx:
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#         swaps.append((i, min_idx))
#       sift_down(arr, min_idx, swaps)

# def build_heap(arr):
#     n = len(arr)
#     swaps = []
#     for i in range(n // 2 - 1, -1, -1):
#         sift_down(arr, i, swaps)
#     return swaps

# n = int(input())
# arr = list(map(int, input().split()))

# swaps = build_heap(arr)

# print(len(swaps))
# for swap in swaps:
# print(swap[0], swap[1])

#------------------------------------

# python3
import os

def build_heap(data):
    swaps = []
    size = len(data)
    for i in range(size//2, -1, -1):
        SiftDown(data, i, swaps)
    return swaps

def SiftDown(data, i, swaps):
    size = len(data)
    min_index = i
    leftChild = 2 * i + 1
    rightChild = 2 * i + 2 
    if leftChild < size and data[leftChild] < data[min_index]:
        min_index = leftChild
    if rightChild < size and data[rightChild] < data[min_index]:
        min_index = rightChild
    if min_index != i:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        SiftDown(data, min_index, swaps)

def main():       
    text = input()
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))

        assert len(data) == n
        swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))

        print(len(swaps))
        for i, j in swaps:
            print(i, j)
            
    elif "F" in text:
        fileName = input()
        path = './tests/'    
        mape = os.path.join(path, fileName)
        if "a" in fileName:
            print("Faila nosaukumā ir kļūda:")
            return
            
        else:
            try:
                with open(mape, mode="r") as file:
                    n = int(file.readline())
                    parents = list(map(int, file.readline().split()))
            except Exception as error:
                print("Error", str(error))
                return
                  
    else:
        print("Ievadiet burtu 'I' vai 'F':")
        return

if __name__ == "__main__":
    main()