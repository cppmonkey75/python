import copy

def generate_all_subsets(initial_set):
    list_of_sets=[set()]
    for item in initial_set:
        new_subsets=[]
        for subset in list_of_sets:
            new_subsets.append({*subset,item})
        list_of_sets.extend(new_subsets)
    return list_of_sets

initial_set={1,2,3}
subsets=generate_all_subsets(initial_set)
for subset in subsets:
    print(subset)
