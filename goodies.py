
def get_file_content(filename):
    d = {}
    #open text file
    with open(filename, "r") as f: 
        lines = f.readlines()
        #read every line and create a dictionary
        for line in lines:
            k, v = line.strip().split(":")
            d[k] = int(v)    
    return d


#function
def goodies(n, d):
    l = list(d.values()) # get only the prices 
    inv_d = {d[i]:i for i in d} # create an inverse-mapping for final display
    l.sort() # sort the prices 
    current_min = 100000000000
    current_box = -1
    # iterate through the price-list as  a window
    for i in range(len(l)-n):
        window = l[i:i+n] # pick the prices at that window
        diff = window[-1]-window[0] # since the list is sorted, difference is just the last minus first item

        # get the minimum price across the whole list
        if (diff<current_min):
            current_box = i
            current_min = diff
#  These will be the final prices with the criteria
    prices = l[current_box:current_box+n]
#  Given these prices, use the inverse-mapping to get the item-names.

    final_goodies = {}
    for price in prices:
        # print(inv_d[price] + ":" +str(price))
        final_goodies[inv_d[price]]  = price
    return final_goodies, current_min


def write_goodies(filename, goods, min_price):
    with open(filename, "w") as f:
        for k in goods:
            f.write(str(k) + " : " + str(goods[k]) + "\n")
        f.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(min_price))
    
        f.close()


n = int(input("Enter the number of employees: "))
d=get_file_content("goodies.txt")
final_goodies, min_price = goodies(n,d)



write_goodies("final_goodies.txt", final_goodies, min_price)