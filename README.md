# Python Fundamentals Repository

This repository serves as a comprehensive guide to Python fundamentals, designed for programmers of all levels to strengthen their understanding of core concepts.

## Contents
1. [Python Basics](#python-basics)
2. [Class Fundamentals](#class-fundamentals)
3. [Python Fundamentals](#python-fundamentals)
4. [Variables and Memory](#variables-and-memory)
5. [Numeric Types](#numeric-types)
6. [Function Parameters](#function-parameters)
7. [First Class Functions](#first-class-functions)

---

## Python Basics

### Multiline Strings
- Learn the functionality and use of multiline strings in Python.

---

## Class Fundamentals

- Introduction to Classes and Objects in Python.
- Understand how to define and use getter and setter methods with the `@property` decorator.

---

## Python Fundamentals

### Key Points on Getter & Setter
1. **No Need for Getter & Setter by Default**
   - Use them only when custom logic is needed.
2. **Using @property and @<value>.setter**
   - The `@property` decorator simplifies getter and setter implementation without breaking existing code.

---

## Variables and Memory

### Key Concepts
1. **Memory Management**
   - Python Memory Manager handles the heap where objects are stored.
2. **Variable Referencing**
   - Variables are references to memory addresses.
3. **Reference Count**
   - `ref_count` increases when an object is referenced; it is destroyed when the count drops to zero.
4. **Circular References**
   - Occurs when two objects reference each other, leading to memory leaks.
5. **Mutable vs Immutable**
   - **Mutable**: Objects whose state can change (`Lists`, `Dictionaries`).
   - **Immutable**: Objects whose state cannot change (`Numbers`, `Strings`, `Tuples`).

---

## Numeric Types

### Key Points to Remember
1. **floor()**
   - Returns the largest integer less than or equal to a value.
2. **trunc()**
   - Returns the integer portion of a number, truncating any decimal.
3. **Constrained Denominator**
   - Given a `Fraction` object, approximate it with a constrained denominator.

---

## Function Parameters

### Key Points to Remember
1. **Unpacking**
   - Unpacking occurs because the RHS is first evaluated, then assignments are made to the LHS.
2. **Unordered Types**
   - Dictionaries and sets are unordered types and cannot be unpacked.
3. **Tuples by Comma**
   - Tuples are defined by commas, not parentheses.
4. **Partial Unpacking**
   - Use the `*` operator to unpack part of an iterable, assigning the remainder to another variable.
5. **`*` Usage**
   - The `*` operator can only be used once in the LHS.

---

## First Class Functions

### Key Points to Remember
1. **First Class Objects**
   - Functions can be passed as arguments, returned from other functions, assigned to variables, or stored in data structures.
2. **Higher-Order Functions**
   - Functions that take another function as an argument or return a function.
3. **`map` Function**
   - Takes a function and a variable number of iterable objects.
   - Returns an iterator that applies the function to each element.
   - Stops when the shortest iterable is exhausted.

---
