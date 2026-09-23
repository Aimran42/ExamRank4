def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    grid = [['.'] * dim for _ in range(dim)]
    for r, c in stars:
        if 0 <= r < dim and 0 <= c < dim:
            grid[r][c] = '*'
    return [''.join(row) for row in grid]

# TESTS :
# if __name__ == "__main__":
#     out = []
#     expected = []

#     out.append(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
#     # Output
#     expected.append(['*..', '.*.', '..*'])

#     # Input
#     out.append(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3))
#     # Output
#     expected.append(['.*.', '***', '.*.'])


#     # Input
#     out.append(constellation_mapper([], 2))
#     # Output
#     expected.append(['..', '..'])


#     # Input
#     out.append(constellation_mapper([(0, 0), (0, 0), (1, 1)], 2))
#     # Output
#     expected.append(['*.', '.*'])


#     # Input
#     out.append(constellation_mapper([(0, 0), (5, 5)], 3))
#     # Output
#     expected.append(['*..', '...', '...'])


#     # Input
#     out.append(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3))
#     # Output
#     expected.append(['...', '***', '...'])

#     n = -1
#     [print(i) for i in out if( n := n + 1 )or expected[n] == i]
#     if out == expected:
#         print("All 6 test passed 100/100")