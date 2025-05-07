# **_🚀 OOP & Python Essentials: Assignment Portfolio 🚀_**

Welcome to your **comprehensive** collection of **21 mini-projects** covering core Python OOP concepts, special methods, decorators, error handling, and more! Clone this repo, explore each folder, and run the examples to see the magic in action.

---

## **_1. Using `self`_**  
**Objective:** Create a **`Student`** class with **instance attributes** `name` & `marks`, initialized via `self`. Add a **`display()`** method.

---

## **_2. Using `cls`_**  
**Objective:** Build a **`Counter`** class that tracks how many instances are created. Use a **class variable** & a **`@classmethod`** with `cls`.

---

## **_3. Public Variables & Methods_**  
**Objective:** Define a **`Car`** class with a **public** variable `brand` and method **`start()`**. Instantiate and access both externally.

---

## **_4. Class Variables & Class Methods_**  
**Objective:** Implement a **`Bank`** class with **class variable** `bank_name`. Add `@classmethod change_bank_name(cls, name)`—show it updates all instances.

---

## **_5. Static Methods_**  
**Objective:** Create **`MathUtils`** with a **`@staticmethod add(a, b)`**. No instance/class variables.

---

## **_6. Constructors & Destructors_**  
**Objective:** Craft a **`Logger`** class that prints on **creation** (`__init__`) and on **destruction** (`__del__`).

---

## **_7. Access Modifiers_**  
**Objective:** Design an **`Employee`** class with:  
- **public** `name`  
- **protected** `_salary`  
- **private** `__ssn`  
Attempt to access each and document the results.

---

## **_8. The `super()` Function_**  
**Objective:** Make a base **`Person`** (sets `name`) and subclass **`Teacher`** (adds `subject`), invoking the parent constructor via **`super()`**.

---

## **_9. Abstract Classes & Methods_**  
**Objective:** Use the **`abc`** module to define an abstract **`Shape`** with `@abstractmethod area()`. Implement **`Rectangle`** subclass.

---

## **_10. Instance Methods_**  
**Objective:** Write a **`Dog`** class with `name`, `breed`, and an instance method **`bark()`** that says “Woof! I am {name}.”

---

## **_11. Class Methods_**  
**Objective:** Create a **`Book`** class with class variable **`total_books`** and `@classmethod increment_book_count()`.

---

## **_12. Static Methods_**  
**Objective:** Implement **`TemperatureConverter`** with `@staticmethod celsius_to_fahrenheit(c)` and `fahrenheit_to_celsius(f)`.

---

## **_13. Composition_**  
**Objective:** Define an **`Engine`** class and a **`Car`** class that takes an **`Engine`** instance in its constructor. Call engine methods via car.

---

## **_14. Aggregation_**  
**Objective:** Create a **`Department`** class holding references to independent **`Employee`** objects.

---

## **_15. MRO & Diamond Inheritance_**  
**Objective:** Set up classes **`A`** → **`B(A)`**, **`C(A)`**, **`D(B, C)`**, each overriding `show()`. Instantiate **`D`** and call `show()` to observe MRO.

---

## **_16. Function Decorators_**  
**Objective:** Write `log_function_call` decorator to print “Function is being called” before running any function. Apply to **`say_hello()`**.

---

## **_17. Class Decorators_**  
**Objective:** Create `add_greeting` class decorator to inject `greet()` returning “Hello from Decorator!” into any class. Apply to **`Person`**.

---

## **_18. Property Decorators_**  
**Objective:** Build a **`Product`** class with private `_price`. Use `@property`, `@price.setter`, `@price.deleter` to manage it.

---

## **_19. `callable()` & `__call__()`_**  
**Objective:** Build a **`Multiplier`** class whose constructor sets a factor. Implement `__call__()` to multiply input by that factor. Test with **`callable()`** and by calling the instance.

---

## **_20. Custom Exception_**  
**Objective:** Define **`InvalidAgeError`**. Write `check_age(age)` that raises it if `< 18`. Handle with **`try…except`**.

---

## **_21. Custom Iterable_**  
**Objective:** Create a **`Countdown`** class taking a start number. Implement **`__iter__()`** & **`__next__()`** to count down to 0 in a `for` loop.

---

Good luck, and happy coding! 🎉  
