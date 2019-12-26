import pandas as pd

# Saving csv file as dataframe and finding top of a tree
df1 = pd.read_csv("employee.csv")
top_manager = df1.query("managerid == 'Nan'")
print("{}-{}".format(top_manager.name.values[0],top_manager.id.values[0]))

# Recursive function used to parse data in the form a tree
def tree(manager,flag):
    new_manager = df1.query("managerid == {}".format(manager.id.values[0]))
    if len(new_manager) == 0:
        flag -= 1
        return
    elif len(new_manager) == 1:
        flag += 1
        print("\t"*flag+"{}-{}".format(new_manager.name.values[0],new_manager.id.values[0]))
        tree(new_manager, flag)
        flag -=1
        return
    elif len(new_manager) > 1:
        flag+=1
        for i in range(len(new_manager)):
            print("\t"*flag+"{}-{}".format(new_manager.name.values[i], new_manager.id.values[i]))
            tree(new_manager.query("id == {}".format(new_manager.id.values[i])), flag)

# Calling of function
tree(top_manager,0)
