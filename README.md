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

### Python Memory Management
1. **Heap Storage Management**  
   - Storing and retrieving objects in memory is managed by the **Python Memory Manager**.
2. **Variables as References**  
   - Variables in Python act as references pointing to the memory address where the actual object resides.
3. **Reference Count**  
   - Each time a variable references a memory address, the reference count for that memory address is incremented.
4. **Automatic Memory Reclamation**  
   - When the reference count of an object drops to zero, the Python Memory Manager automatically destroys the object and reclaims the memory.

