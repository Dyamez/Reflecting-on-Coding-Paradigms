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

** What is used here is Functional Programming wherein we defined the 
    list and should not be able to change after it has been created. Variables
    defined here are thus immutable.


Is this solution a pure function? Why or why not?

** The output is purely dependent on what was hard coded in the list
        defined here as 'nested'. It is declarative.


Is this solution a higher order function? Why or why not?

**  It is higher-order function as it returns a function and accepts a function as
        an argument.


Would it have been easier to solve this problem using a different programming style?

** Maybe. For now, this seems to be the proper way of solving the programming problem.



Why in particular is functional programming a helpful paradigm when solving this problem?

** Functional Programming relies solely on what values were defined and should have no side effects.
    No changes after the output and is purely evaluated. In short, it is straightforward in approch.

'''
