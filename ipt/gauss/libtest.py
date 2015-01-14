#!/usr/bin/python3

import gauss;

mat = [
        [ 1, 0, 0, 1 ],
        [ 0, 1, 0, 2 ],
        [ 0, 0, 1, 3 ]
      ]

gauss.matrix.output(mat)
comp = gauss.triangularize(mat, 3)
base = gauss.base(3, comp)
if not gauss.solve(mat, base, 3):
    print("No solution.")
else:
    gauss.output_results(base)

