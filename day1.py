
def main():
    with(open("day1_data.txt", "r")) as f:
        items = f.readlines()
        elfs_totals = []
        elfs_load = []
        for i in items:
           if len(i) > 1:
               # print("found load from an elf")
               elfs_load.append(int(i))
           else:
               # print("elf is empty, let's sync up!")
               elfs_totals.append(sum(elfs_load))
               elfs_totals.append(0)
               elfs_load.clear()
        
        elfs_totals.sort(reverse=True)
        print("Top elf: ", elfs_totals[0])
        print("Sum of top 3 elves: ", sum(elfs_totals[0:3]))

if __name__=='__main__':
    main()
