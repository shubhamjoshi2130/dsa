"""Younges common ancestory
We are given with a graph and we need to find youngest common ancestor
We will be given 2 decendents
"""


def getYoungestCommonAncestor(topAncestor, decendantsOne, decendantsTwo):
    depthOne = getDecendantDepth(decendantsOne, topAncestor)
    depthTwo = getDecendantDepth(decendantsTwo, topAncestor)
    if depthOne > depthTwo:
        return backtraceAncestralTree(decendantsOne, decendantsTwo, depthOne - depthTwo)
    else:
        return backtraceAncestralTree(decendantsTwo, decendantsOne, depthTwo - depthOne)


def getDecendantDepth(decendant, topAncestor):
    depth = 0
    while decendant != topAncestor:
        depth += 1
        decendant = decendant.ancestor
    return depth


def backtraceAncestralTree(lowerDecendent, higherDecendent, diff):
    if diff > 0:
        for i in range(diff):
            lowerDecendent = lowerDecendent.ancestor
            diff -= 1
    while lowerDecendent != higherDecendent:
        higherDecendent = higherDecendent.ancestor
        lowerDecendent = lowerDecendent.ancestor
    return lowerDecendent
