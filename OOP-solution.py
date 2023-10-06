

def flatten_and_sort(lst):
    out = []
    for item in lst:
        for i in item:
            out.append(i)
    return sorted(out)


nested = [0, -2, 5, 4, [5, 4, 122, 343], [325, 33344221]]

out = flatten_and_sort(nested)

print(out)
print(nested)
