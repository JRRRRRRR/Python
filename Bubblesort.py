# Bubblesort

def bubblesort(data):
    for i in range(len(data)-1):
        for idx in range(len(data)-1):
            if data[idx] > data[idx+1]:
                temp = data[idx]
                data[idx] = data[idx+1]
                data[idx+1] = temp
        print("data is now", data)
