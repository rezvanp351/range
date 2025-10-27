# range_examples.py
# Practical examples of the Python range() function
# Reference: https://www.w3schools.com/python/ref_func_range.asp

# ----------------------------------------------
# 1️⃣ Basic range() — counting numbers from 0 to 4
# ----------------------------------------------
def range_basic():
    print("Example: range_basic()")
    # Counting from 0 to 4 (5 is not included)
    for i in range(5):
        print(f"Student number {i}")
    print("Total students: 5\n")


# ------------------------------------------------
# 2️⃣ range() with start and stop — numbering desks
# ------------------------------------------------
def range_with_start_stop():
    print("Example: range_with_start_stop()")
    # Desks in a classroom are numbered from 10 to 15 (16 not included)
    for desk_number in range(10, 16):
        print(f"Desk #{desk_number}")
    print("All desks labeled successfully!\n")


# ---------------------------------------------------------
# 3️⃣ range() with step — showing even numbers in mathematics
# ---------------------------------------------------------
def range_with_step():
    print("Example: range_with_step()")
    # Showing even numbers between 2 and 10
    for number in range(2, 11, 2):
        print(f"Even number: {number}")
    print("All even numbers displayed!\n")


# ------------------------------------------------------------------
# 4️⃣ range() with for...else — checking attendance completion
# ------------------------------------------------------------------
def range_with_for_else():
    print("Example: range_with_for_else()")
    # Simulate checking attendance for 4 students
    for student in range(4):
        print(f"Checked student #{student}")
    else:
        print("Attendance completed successfully!\n")


# ----------------------------------------------------------
# 5️⃣ range() with len() — printing items from a list (fruits)
# ----------------------------------------------------------
def range_with_list():
    print("Example: range_with_list()")
    fruits = ["apple", "banana", "cherry"]
    for i in range(len(fruits)):
        print(f"Fruit #{i + 1}: {fruits[i]}")
    print("All fruits have been displayed!\n")


# -----------------------------------------------------------------
# 6️⃣ range() with negative step — counting down for a timer
# -----------------------------------------------------------------
def range_countdown():
    print("Example: range_countdown()")
    # Countdown timer from 5 to 1
    for seconds in range(5, 0, -1):
        print(f"Countdown: {seconds}")
    print("Time’s up!\n")


# -----------------------------------------------------------------
# 7️⃣ range() used in a multiplication table (real classroom example)
# -----------------------------------------------------------------
def range_multiplication_table():
    print("Example: range_multiplication_table()")
    # Show the multiplication table of 3
    for i in range(1, 11):
        print(f"3 × {i} = {3 * i}")
    print("Multiplication table complete!\n")


# 🧠 Students can run each function separately:
# -------------------------------------------------
# range_basic()
# range_with_start_stop()
# range_with_step()
# range_with_for_else()
# range_with_list()
# range_countdown()
# range_multiplication_table()
