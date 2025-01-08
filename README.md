# PythonFundamental - Key Points to Remember

This repository provides concise notes on important concepts of Python, covering various topics like getter/setter methods, memory management, numeric types, function parameters, and first-class functions.

---

## 1. Getter & Setter
- **When to use:** Avoid using getters and setters unless logic needs to be implemented.
- **Alternative Approach:** Use `@property` and `@<value>.setter` decorators to prevent breaking the code while avoiding traditional getter/setter.

---

## 2. Variable and Memory - Key Points
1. **Memory Management:** Python Memory Manager handles storing and retrieving objects in the heap.
2. **Variables as References:** Variables reference the memory address where the object is stored.
3. **Reference Counting:** Incremented for a memory address whenever a variable points to it.
4. **Object Destruction:** When reference count hits 0, the object is destroyed, and memory is reclaimed.
5. **Circular Reference:** Occurs when objects reference each other, causing a memory leak.
6. **Re-assignment:** Creates a new memory location for the variable.
7. **State Modification:** Changing an object's data modifies its internal state.
8. **Mutability:**
   - Mutable: Lists, Sets, Dictionaries, User-Defined Classes.
   - Immutable: Numbers, Strings, Tuples, Frozen Sets, User-Defined Classes.
9. **Shared References:** Multiple variables referencing the same object in memory.
   - Safe for immutable objects.
   - Not applicable to mutable objects.
10. **Memory Address Check:** Use `is` to compare memory addresses, but results may vary.
11. **None References:** All variables assigned `None` share the same memory address.
12. **Interning:** Reusing objects in a specific range (e.g., integers `[-5, 256]`).

---

## 3. Numeric Types - Key Points
1. `floor()`: Returns the largest integer ≤ value.
2. `trunc()`: Extracts the integer portion of a number.
3. **Constrained Denominator:** Approximate fractions with a constrained denominator using `Fraction`.

---

## 4. Function Parameters - Key Points
1. **Unpacking:** Right-hand side (RHS) is evaluated first before assignments on the left-hand side (LHS).
2. **Unordered Types:** Dictionaries and Sets can't be unpacked.
3. **Tuples:** Defined by commas, not brackets.
4. **Selective Unpacking:** Use `*` to unpack a portion of an iterable.
5. **Single Use of `*`:** The `*` operator can only be used once in the LHS.

---

## 5. First-Class Functions - Key Points
1. **First-Class Objects:** Can be:
   - Passed to a function as arguments.
   - Returned from functions.
   - Assigned to variables or stored in data structures.
2. **Higher-Order Functions:** Functions that take another function as an argument or return one.
3. **Callables:**
   - Objects that can be called and return a value.
   - Includes built-in functions, methods, classes, class instances, and generators.
4. **`map` Function:**
   - Syntax: `map(func, *iterables)`
   - Applies a function to elements of iterables.
   - Stops when the shortest iterable is exhausted.
5. **Reducing Functions:** Combine elements of an iterable recursively to produce a single value.
6. **Deferred Execution:** 
   - Functions like `map`, `filter`, and `zip` return generators, not lists or tuples.
   - Calculations are deferred until needed, enabling efficient memory usage.
   - Generators are not reusable after iteration.

---

This document serves as a quick reference for Python developers to reinforce fundamental concepts and best practices. 🚀
