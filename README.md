# 📘 Python `range()` Function — Educational Examples

This repository explains the `range()` function in Python in a **clear and structured way** for students, following the **W3Schools** style with added explanations.

---

## 🧠 What is `range()`?

The `range()` function in Python returns a sequence of numbers, starting from **0** by default, and increments by **1** (by default), and stops **before** a specified number.

**Syntax:**
```python
range(start, stop, step)
```

| Parameter | Description |
|------------|-------------|
| `start` | Optional. The starting number of the sequence. Default is 0. |
| `stop` | Required. The end of the sequence (excluded). |
| `step` | Optional. The increment between numbers. Default is 1. |

---

## 🧩 Examples and Explanations

### 🔹 Example 1 — Basic usage
```python
for x in range(6):
    print(x)
```
**Explanation:**  
Generates numbers from **0 to 5** (the `stop` value `6` is not included).

---

### 🔹 Example 2 — Start and Stop
```python
for x in range(2, 6):
    print(x)
```
**Explanation:**  
Starts from `2` and stops before `6`.

---

### 🔹 Example 3 — With Step Value
```python
for x in range(2, 12, 2):
    print(x)
```
**Explanation:**  
Generates even numbers from **2 to 10**, increasing by `2`.

---

### 🔹 Example 4 — Convert to List
```python
numbers = list(range(5))
print(numbers)
```
**Explanation:**  
Converts the sequence into a list → `[0, 1, 2, 3, 4]`.

---

### 🔹 Example 5 — Reverse Counting
```python
for x in range(10, 0, -2):
    print(x)
```
**Explanation:**  
Counts backward from `10` to `2` in steps of `-2`.

---

### 🔹 Example 6 — Conditional Example
```python
for x in range(10):
    if x % 2 == 0:
        print(f"{x} is even")
```
**Explanation:**  
Prints only even numbers between `0` and `9`.

---

## 📚 Source
Based on examples from **[W3Schools Python range()](https://www.w3schools.com/python/ref_func_range.asp)**, with additional educational explanations for students.

---

## 🧑‍💻 Author
**Rezvan Panah** — Educational version for students learning Python fundamentals.
