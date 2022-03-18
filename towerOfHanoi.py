def towerOfHanoi(disks, initial, transfer, target):
    if disks == 1:
        print("Move disk", disks, "from tower", initial, "to tower", target)
        return
    towerOfHanoi(disks - 1, initial, target, transfer)
    print("Move disk", disks, "from tower", initial, "to tower", target)
    towerOfHanoi(disks - 1, transfer, initial, target)

disks = int(input("Give me your number of disks: "))
towerOfHanoi(disks, "A", "B", "C")