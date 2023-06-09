def Tower_Of_Hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    Tower_Of_Hanoi(n-1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    Tower_Of_Hanoi(n-1, auxiliary, destination, source)

# Driver
n = 4
Tower_Of_Hanoi(n, 'A', 'B', 'C')