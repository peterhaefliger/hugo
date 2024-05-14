import functools

# function which calculates and returns the set of all possible pairs of numbers
# from 1...N which satisfy the condition that their sum is in the targets set
def possible_pairings(N, targets):
  result_list = []
  for i in range(1, N+1):
    result_list.append([])
  for i in range(1, N+1):
    for j in range(1, N+1):
      if i != j and i + j in targets:
        result_list[i-1].append(j)
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
  if pos == N+1:
    global solution_count
    solution_count = solution_count + 1
    log = "After " + str(recursion_count) + " total calls to 'solve()': "
    log = log + "solution no " + str(solution_count) + ": "
    print(log)
    print(used_pairs)

  # if the current position in the circle has already been taken by the second
  # element of a pair placed earlier, then move on to the next position
  elif pos_taken[pos-1]:
    solve(pos+1)
  else:

    # else iterate over all possible pairs for the current position
    for paired_pos in possible_pairs[pos-1]:

      # if the position of the pair's second element is also available...
      if not pos_taken[paired_pos-1]:

        # ... then remember the currently used pair
        # and tentatively mark both positions in the circle.
        used_pairs.append([pos, paired_pos])
        pos_taken[pos-1] = True
        pos_taken[paired_pos-1] = True

        # The above three lines already simulate the current move; 
        # check its effects before actually making the move 
        # and stepping one level down the tree.

        # positive assumption: all future pairs reachable, i.e. for
        # every position not yet taken, there exists a pair position
        # not yet taken
        all_future_pos_reachable = True

        # for every future position, try to prove assumption wrong 
        for p in range(pos+1, N+1):
          if not pos_taken[p-1]:
                      
            # negative assumption: no more pair position available
            paired_p_reachable = False

            # try to prove assumption wrong 
            for paired_p in possible_pairs[p-1]:
              if not pos_taken[paired_p-1]:
                paired_p_reachable = True
                
            if not paired_p_reachable:
              all_future_pos_reachable = False

        if all_future_pos_reachable:        
          # move on to the next position
          solve(pos+1)

        # trace back by releasing the used pair 
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

log = "Calculating Rainbow Pairs for 1 ... " + str(N)
log = log + " for target set " + str(targets) + ":"
print(log)
print()
print("Possible partner positions for each position 1 ... " + str(N) + ":")
print(possible_pairs)
print()

li = list(map(lambda li: len(li), possible_pairs))
num_pos_pairs = round(functools.reduce(lambda a, b: a+b, li)/2)
print("Number of possible pairs: " + str(num_pos_pairs))

solve(1)

print()
log = "Calculation terminated. " + str(solution_count)
log = log + " solutions found with " + str(recursion_count)
log = log + " calls to recursive solver function."
print(log)
