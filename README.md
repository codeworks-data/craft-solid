# craft-solid
Learn the SOLID principle by practice !


---

## S: single-responsibility principle

A class or function should have only one job. One reason to change.


Refactor the functions in S.py to respect this principle.


## O: Open/closed principle

Software entities (classes, modules, functions, etc.) should be open for extensions, but closed for modification.

This means that if we want to add specific behaviour to a preexisting code, we should be able to add it without 
changing what is already there.

Polymorphism is often used for this one.

Refactor the function in O.py to respect this principle and keep in mind that we may want to add more specific behaviour
in the near future.

## L: 

Liskov substitution principle.

You should be able to use a subclass instead of its parent without changing the logic of the program.

Refactor the function in L.py to respect this principle. (there is an issue with MentionPost)

## I

Interface segregation principle.

A client should not be forced to implement an interface that it does not use.

Refactor the classes in I.py to respect this principle.
In this example, the Circle and Square classes both have to implement a method that doesn't make sense for them.
You want to change that. Both Circle and Square should be able to print themselves without using empty methods.

## D