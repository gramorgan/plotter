import numpy as np

MATS = list(map(np.matrix, [

    # 0
    [
        [ 0,  0,  0],
        [ 0,  0,  0],
        [ 0,  0,  0],
    ],

    # 1
    [
        [ 0,  0,  1],
        [ 0,  0,  1],
        [ 1,  1,  0],
    ],

    # 2
    [
        [ 0,  0,  1],
        [ 0,  0,  1],
        [ 1,  0,  0],
    ],

    # 3
    [
        [ 0,  0,  1],
        [ 0,  0,  1],
        [ 1, -1,  0],
    ],

    # 4
    [
        [ 0,  0,  0],
        [ 0,  0,  0],
        [ 1, -1,  0],
    ],

    # 5
    [
        [ 0,  1,  2],
        [ 1,  0,  1],
        [ 2, -1,  0],
    ],

    # 6
    [
        [ 0,  1, -1],
        [ 1,  0, -2],
        [-1,  2,  0],
    ],

    # 7
    [
        [ 0,  1,  1],
        [ 1,  0,  1],
        [ 1,  1,  0],
    ],

    # 8
    [
        [ 0, -1,  3],
        [-1,  0,  3],
        [ 1,  1,  0],
    ],

    # 9
    [
        [ 0,  1,  1],
        [-1,  0,  3],
        [ 1,  1,  0],
    ],

    #10
    [
        [ 0,  1,  3],
        [-1,  0,  5],
        [ 1,  3,  0],
    ],

    #11
    [
        [ 0,  1, -1],
        [-1,  0,  1],
        [-1,  1,  0],
    ],

    #12
    [
        [ 0,  6, -4],
        [-3,  0,  5],
        [-1,  3,  0],
    ],

    # 13
    [
        [ 0,  1, -1],
        [ 1,  0, -3],
        [-1,  3,  0],
    ],
 
    # 14
    [
        [ 0,  3, -1],
        [ 3,  0, -1],
        [ 1,  1,  0],
    ],

    # 15
    [
        [ 0,  3, -1],
        [ 1,  0,  1],
        [ 3, -1,  0],
    ],

    # 16
    [
        [ 0, -1,  1],
        [ 2,  0, -1],
        [-2,  1,  0],
    ],

    # 17
    [
        [ 0,  2, -1],
        [-1,  0,  2],
        [ 2, -1,  0],
    ],

    # 18
    [
        [ 0,  0,  0],
        [ 0,  0, -1],
        [ 0,  1,  0],
    ],

    # 19
    [
        [ 0,  0,  0],
        [ 0,  0, -1],
        [ 0,  0,  0],
    ],

    # 20
    [
        [ 0,  0,  0],
        [ 0,  0,  1],
        [ 0,  1,  0],
    ],

    # 21
    [
        [ 0,  0, -2],
        [ 0,  0, -1],
        [-1, -1,  0],
    ],

    # 22
    [
        [ 0,  0, -1],
        [ 0,  0,  1],
        [-1,  1,  0],
    ],

    # 23
    [
        [ 0,  0,  1],
        [ 0,  0,  0],
        [ 1, -1,  0],
    ],

    # 24
    [
        [ 0,  0,  1],
        [ 0,  0,  0],
        [ 1,  1,  0],
    ],

    # 25
    [
        [ 0,  0, -2],
        [ 0,  0, -1],
        [-1,  0,  0],
    ],

    # 26
    [
        [ 0,  0, -1],
        [ 0,  0,  1],
        [-1,  0,  0],
    ],

    # 27
    [
        [ 0,  0, -1],
        [ 0,  0, -2],
        [-1,  0,  0],
    ],

    # 28
    [
        [ 0,  0, -1],
        [ 0,  0, -2],
        [-1,  1,  0],
    ],

    # 29
    [
        [ 0,  0, -1],
        [ 0,  0, -1],
        [ 0,  0,  0],
    ],

    # 30
    [
        [ 0,  0, -2],
        [ 0,  0, -1],
        [ 0,  0,  0],
    ],

    # 31
    [
        [ 0,  0, -1],
        [ 0,  0,  1],
        [ 0,  0,  0],
    ],

    # 32
    [
        [ 0,  0, -1],
        [ 0,  0,  0],
        [ 0, -1,  0],
    ],

    # 33
    [
        [ 0,  0, -1],
        [ 0,  0,  1],
        [ 1, -1,  0],
    ],

    # 34
    [
        [ 0, -1,  3],
        [-1,  0,  1],
        [ 3,  1,  0],
    ],

    # 35
    [
        [ 0,  3,  1],
        [ 3,  0,  1],
        [ 1,  1,  0],
    ],

    # 36
    [
        [ 0,  1, -1],
        [-3,  0,  1],
        [-1,  1,  0],
    ],

    # 37
    [
        [ 0,  1,  1],
        [-1,  0,  1],
        [ 1,  1,  0],
    ],

    # 38
    [
        [ 0,  1,  1],
        [-1,  0,  3],
        [ 1,  3,  0],
    ],

    # 39
    [
        [ 0, -1, -1],
        [ 1,  0,  1],
        [-1,  1,  0],
    ],

    # 40
    [
        [ 0,  1, -1],
        [ 1,  0, -1],
        [ 1,  1,  0],
    ],

    # 41
    [
        [ 0,  1, -1],
        [ 1,  0,  1],
        [ 1, -1,  0],
    ],

    # 42
    [
        [ 0,  1,  1],
        [ 1,  0,  1],
        [-1, -1,  0],
    ],

    # 43
    [
        [ 0,  1,  1],
        [-1,  0,  1],
        [-1, -1,  0],
    ],

    # 44
    [
        [ 0,  1,  1],
        [ 0,  0,  2],
        [ 0,  2,  0],
    ],

    # 45
    [
        [ 0, -1,  1],
        [ 0,  0, -1],
        [ 0,  1,  0],
    ],

    # 46
    [
        [ 0, -2,  2],
        [ 0,  0,  1],
        [ 0,  1,  0],
    ],
]))