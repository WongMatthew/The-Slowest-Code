def generate_permutations(arr):
    if len(arr) == 1:
        return [arr]

    permutations = []
    for i in range(len(arr)):
        first = arr[i]
        rest = arr[:i] + arr[i+1:]
        for p in generate_permutations(rest):
            permutations.append([first] + p)
    return permutations

# the slowest way to generate permutations
generate_permutations([1,2,3])