import functools

# function which calculates and returns the set of all possible pairs of numbers 
# from 1...N which satisfy the condition that their sum is in the targets set
def possible_pairings(N, targets):
    result_list = []
    for i in range(1, N+1):
        result_list.append([i, []])
    for i in range(1, N+1): 
        for j in range(i+1, N+1):
            if i + j in targets:
                result_list[j-1][1].append([j, i])
    return result_list

# global counter to keep track of the number of solutions found
solution_count = 0

# global counter to keep track of the number of recursive solver calls
recursion_count = 0

# recursive solver procedure
def solve(pos):

    global recursion_count
    recursion_count = recursion_count + 1

    # if all positions in the circle have been taken,
    # a solution to the puzzle has been found
    if pos == 0:
        global solution_count
        solution_count = solution_count + 1
        print("After " + str(recursion_count) + " total calls to 'solve()': solution no " + str(solution_count) + ": ")
        print(used_pairs)

    # if the current position in the circle has already been taken by the second
    # element of a pair placed earlier, then move on to the next position
    elif pos_taken[pos-1]:
        solve(pos-1)
    else:

        # else iterate over all possible pairs for the current position
        for p in possible_pairs[pos-1][1]:
            paired_pos = p[1]

            # if the position of the pair's second element is also available...
            if not pos_taken[paired_pos-1]:

                # ... then remember the currently used pair
                # and mark both positions in the circle, ...
                used_pairs.append(p)
                pos_taken[pos-1] = True
                pos_taken[paired_pos-1] = True

                # ... move on to the next position and then...
                solve(pos-1)

                # ... trace back by releasing the used pair 
                # and unmarking the two positions in the circle
                used_pairs.pop()
                pos_taken[pos-1] = False
                pos_taken[paired_pos-1] = False

# upper bound N of the interval of numbers 1...N in the circle
N = 60

# set of target numbers for the pairs
targets = (9, 36, 49, 64, 81)

# the set of possible pairs which satisfy the target 
possible_pairs = possible_pairings(N, targets)

# list of the positions 1 ... N to keep track of 
# which are already taken and which are still unoccupied
pos_taken = []
for i in range(1, N+1):
    pos_taken.append(False)

# list of all the pairs currently used in the backtracking algorithm
used_pairs = []

print("possible pairs, ordered by lower number of the pair = ")
print(possible_pairs)
num_pairs = list(map(lambda li: len(li[1]), possible_pairs))
print("number of pairs per lower number of the pair = ")
print(num_pairs)
total_number = functools.reduce(lambda a, b: a+b, num_pairs)
print("total number of pairs = " + str(total_number) )

solve(60)

print()
print("No more solutions")
print("recursive method called " + str(recursion_count) + " times.")
