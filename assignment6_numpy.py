"""
UCS420: Cognitive Computing
Assignment 6 - Numpy-II
"""

import numpy as np


# Q1. 
def q1():
    print("Q1. Sensor Readings")
    print("-" * 50)

    temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40])

    # a. 
    corrected = temperature + 2
    print("a. Corrected temperatures (+2°C):", corrected)

    # b. 
    fahrenheit = corrected * 9 / 5 + 32
    print("b. Temperatures in Fahrenheit:   ", fahrenheit)

    # c. 
    above_32 = corrected[corrected > 32]
    print("c. Readings greater than 32°C:   ", above_32)

    # d. 
    count_above_32 = np.sum(corrected > 32)
    print("d. Count of readings > 32°C:     ", count_above_32)

    # e. 
    print(
        "e. Vectorization applies an operation to an entire array at once\n"
        "   using low-level, compiled C loops instead of Python-level\n"
        "   for-loops, which removes interpreter overhead and makes\n"
        "   operations on large arrays much faster. Boolean indexing lets\n"
        "   us filter/select elements using a condition (e.g. temp > 32)\n"
        "   in a single expression instead of looping through every value\n"
        "   and checking it manually. Together they make data processing\n"
        "   more concise, less error-prone, and significantly faster than\n"
        "   explicit iteration, especially as data size grows."
    )
    print()


# Q2. 
def q2():
    print("Q2. Daily Steps Matrix")
    print("-" * 50)

    steps = np.array([
        [5000, 6200, 7100],
        [8000, 7500, 9000],
        [4500, 5100, 4800],
        [9000, 8500, 9500],
    ])

    # a. 
    total_steps = np.sum(steps)
    print("a. Total steps recorded:        ", total_steps)

    # b. 
    mean_steps = np.mean(steps)
    print("b. Mean number of steps:        ", mean_steps)

    # c. 
    max_steps = np.max(steps)
    min_steps = np.min(steps)
    print(f"c. Maximum steps: {max_steps}, Minimum steps: {min_steps}")

    # d. 
    total_per_day = np.sum(steps, axis=0)
    print("d. Total steps per day (axis=0):", total_per_day)

    # e. 
    total_per_user = np.sum(steps, axis=1)
    print("e. Total steps per user (axis=1):", total_per_user)

    # f. 
    flat_index = np.argmax(steps)
    user_idx, day_idx = np.unravel_index(flat_index, steps.shape)
    print(
        f"f. Max steps position -> User {user_idx + 1}, Day {day_idx + 1} "
        f"(value = {steps[user_idx, day_idx]})"
    )
    print()


# Q3. 
def q3():
    print("Q3. Array Operations")
    print("-" * 50)

    # a. 
    original = np.array([1, 2, 3, 4, 5, 6])
    print("a. original array:", original)

    # b. 
    subset = original[1:5]
    print("b. subset (original[1:5]):", subset)

    # c.
    subset[0] = 999
    print("c. After subset[0] = 999:")
    print("   original:", original, " <-- also changed! (subset is a view)")
    print("   subset  :", subset)

    # d. 
    original = np.array([1, 2, 3, 4, 5, 6])  
    subset_copy = original[1:5].copy()
    subset_copy[0] = 500
    print("d. After using .copy() and setting copied_subset[0] = 500:")
    print("   original     :", original, " <-- unaffected (independent copy)")
    print("   copied array :", subset_copy)

    # e. 
    matrix = np.arange(1, 13).reshape(3, 4)
    print("e. 3x4 matrix from np.arange(1, 13):\n", matrix)

    # f. 
    first_row = matrix[0]
    last_row = matrix[-1]
    second_column = matrix[:, 1]
    sub_block = matrix[0:2, 1:3]  
    print("f. First row             :", first_row)
    print("   Last row              :", last_row)
    print("   Second column         :", second_column)
    print("   Rows 1-2, Columns 2-3 :\n", sub_block)

    # g. 
    flat_flatten = matrix.flatten()
    flat_ravel = matrix.ravel()
    print("g. flatten():", flat_flatten)
    print("   ravel()  :", flat_ravel)

    # h. 
    flat_ravel[0] = 111
    print("h. After ravel_array[0] = 111:")
    print("   original matrix affected? YES ->\n", matrix)
    print("   (ravel() returns a view whenever possible, sharing memory)")

    # i. 
    matrix = np.arange(1, 13).reshape(3, 4)  # reset
    flat_flatten = matrix.flatten()
    flat_flatten[0] = 222
    print("i. After flatten_array[0] = 222:")
    print("   original matrix affected? NO  ->\n", matrix)
    print("   (flatten() always returns a copy, independent memory)")

    # j. 
    print("j. Shape:", matrix.shape, "| ndim:", matrix.ndim,
          "| size:", matrix.size, "| dtype:", matrix.dtype)
    print()


# Q4. 
def q4():
    print("Q4. Assistance Score Prediction (OLS)")
    print("-" * 50)

    X = np.array([
        [6, 70, 3],
        [5, 50, 6],
        [8, 80, 2],
        [4, 30, 8],
    ])
    y = np.array([40, 65, 30, 85])

    # a. 
    print("a. Shape of X:", X.shape, "| Dimensions (ndim):", X.ndim)

    # b. 
    X_T = X.T
    print("b. X.T (transpose):\n", X_T)
    print(
        "   The transpose flips rows and columns: each column of X.T\n"
        "   now represents one feature (sleep, activity, stress) across\n"
        "   all users, instead of one row per user. This layout is needed\n"
        "   for matrix operations like X.T @ X in linear regression."
    )

    # c. 
    XtX = X_T @ X
    print("c. X.T @ X:\n", XtX)

    # d. 
    XtX_inv = np.linalg.inv(XtX)
    print("d. Inverse of (X.T @ X):\n", XtX_inv)

    # e. 
    beta = XtX_inv @ X_T @ y
    print("e. Regression coefficients (beta):", beta)

    # f. 
    print(
        "f. Each coefficient in 'beta' represents the estimated change in\n"
        "   the assistance score for a one-unit increase in that feature,\n"
        "   holding the other two features constant:\n"
        f"     - Sleep hours coefficient  = {beta[0]:.4f}\n"
        f"     - Activity level coeff.    = {beta[1]:.4f}\n"
        f"     - Stress level coefficient = {beta[2]:.4f}\n"
        "   A positive coefficient means that feature increases the\n"
        "   predicted assistance score, while a negative coefficient\n"
        "   means it decreases it, in proportion to its magnitude."
    )

    # g. 
    new_user = np.array([5, 40, 7])
    predicted_score = new_user @ beta
    print("g. Predicted assistance score for new_user [5, 40, 7]:",
          round(predicted_score, 4))
    print()


if __name__ == "__main__":
    q1()
    q2()
    q3()
    q4()
