def find_max_min(list):
    # check for whether all list elements are equal using inbuilt all()
    # looping through all elements in the list

    if all(x == list[0] for x in list) == True:

        created_list = []

        created_list.append(len(list))
        return created_list
    else:

        maxi = max(list)

        mini = min(list)

        the_other_list = []  # the final empty list, the_other_list[] adds the minimum and maximum values respectively

        the_other_list.append(mini)
        the_other_list.append(maxi)

        return the_other_list