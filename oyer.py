
def chain (*iterable) :
   output = []
   for it in iterable:
      for i in it:
         output.append(i)
   return output

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    output = []
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
        
def yamltemplategenerator (iterable_by_space) :
   iterlist = iterable_by_space.split(" ")
   output = "NEW :"
   for x in iterlist:
      output += "\n\t" + x + " : "
   return repr(output)