# Python Fundamentals Repository

This repository covers the fundamentals of Python programming, organized into key topics.

## Contents

- **python_basics_!**: Explains the use and functionality of multiline strings in Python.
- **ClassFundamental**: Provides an introduction to Classes and Objects in Python.
- **PythonFundamental**: Covers key concepts about using getter & setter methods and Python's `@property` decorator.
- **Variable And Memory**: Explains Python's memory management, variable referencing, and object lifecycle.

---

## PythonBasics - Key Points to Remember

### Getter & Setter
1. **No Need for Getter & Setter by Default**  
   - Use getter and setter methods only when you need to implement custom logic for accessing or modifying attributes.
2. **Using @property and @<value>.setter**  
   - If you don't want to rewrite code to add getter and setter methods, use the `@property` decorator and its corresponding `@<value>.setter`.  
   - This approach allows you to encapsulate logic while preventing breaking existing code.

---

## Variable And Memory - Key Points to Remember

1. **Python Memory Manager**  
   - Storing and retrieving objects from the heap is managed by the Python Memory Manager.

2. **Variables as References**  
   - Variables are references to the memory address where the object is stored.

3. **Reference Count**  
   - The `ref_count` for a memory address increases whenever a variable references that memory address.
   - When the reference count hits `0`, the Memory Manager destroys the object and reclaims the memory.

4. **Circular Reference**  
   - Occurs when object A points to object B and object B points back to object A.
   - This can lead to memory leaks as the Memory Manager cannot clean up these objects.

5. **Reassignment**  
   - On reassignment, a variable is stored at a new memory location.

6. **Modifying Internal State**  
   - Changing the data inside an object is known as modifying its internal state.

7. **Mutable vs Immutable**  
   - **Mutable**: Objects whose internal state can be changed (e.g., `Lists`, `Sets`, `Dictionaries`, `User-Defined Classes`).
   - **Immutable**: Objects whose internal state cannot be changed (e.g., `Numbers`, `Strings`, `Tuples`, `Frozen Sets`, `User-Defined Classes`).

8. **Shared References**  
   - Two variables referencing the same object in memory is called shared references.
   - Example: If `a = 10` and `b = 10`, both variables share the same memory address. This is safe for immutable objects.

9. **Mutable Objects and Shared References**  
   - Python Memory Manager avoids shared references with mutable objects because changes by one variable would affect the other.

10. **Identity Check with `is`**  
    - The `is` operator checks if two variables point to the same memory address (`a is b`).
    - Note: It might return `False` in some cases even if the values are the same.

11. **`None` Variables**  
    - Variables set to `None` share the same memory address.

12. **Interning**  
    - Python reuses objects on-demand for performance.
    - Example: Integers in the range `[-5, 256]` are cached, and references to these integers will use the same memory address.




