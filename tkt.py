from itertools import combinations as comb

## input: 2 lists X and Y of arbitrary length
def truncatedKendallTau(X, Y, similarity=True):
    SI = [x for x in X if x in Y] ## intersection - list to keep the order as in X
    SX = set(X).difference(SI)    ## in X only
    SY = set(Y).difference(SI)    ## in Y only
    tau = 0
    ## SI: pairs in intersection
    l = len(SI)
    y = [Y.index(z) for z in SI]
    s = sum([a<b for a,b in comb(y,2)])
    tau += 2*s - l*(l-1)/2 ## pos-neg pairs a la Kendall-tau.
    ## SX, resp. SY and SI: one element in intersection
    x = [X.index(z) for z in SX]
    y = [Y.index(z) for z in SY]
    i = [X.index(z) for z in SI]
    s = 2*sum([a>b for a in x for b in i]) - len(x)*len(i)
    tau += s
    s = 2*sum([a>b for a in y for b in i]) - len(y)*len(i)
    tau += s
    ## the rest
    tau -= len(SX)*len(SY)
    tau += l*(l+1)/2
    tau /= (len(X)*len(Y))
    if similarity:
        return (tau+1)/2
    else:
        return tau
