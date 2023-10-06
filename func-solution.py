def flatten_and_sort(lst):
    out = []
    for item in lst:
        if type(item) == list:
            for i in item:
                out.append(i)
        else:
            out.append(item)

    return sorted(out)


nested = [0, -2, 5, 4, [5, 4, 122, 343], [325, 33344221]]

out = flatten_and_sort(nested)

print(out)
print(nested)


'''
How does this solution ensure data immutability?


Is this solution a pure function? Why or why not?


Is this solution a higher order function? Why or why not?


Would it have been easier to solve this problem using a different programming style?


Why in particular is functional programming a helpful paradigm when solving this problem?



'''
