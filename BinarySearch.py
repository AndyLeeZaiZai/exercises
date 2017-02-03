def BSearch(list, key):
    low = 0
    high = len(list) - 1
    while(low<=high):
        mid = low + (high - low) / 2
        if(list[mid] < key):
            low = mid + 1
        elif(list[mid] > key):
            high = mid - 1
        else:
            return mid

if __name__ == "__main__":
    list = [1,3,4,5,6,7,8,9,10]
    print list
    print BSearch(list, 2)
