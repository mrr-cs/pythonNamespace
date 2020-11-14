Namespaces [in Python]
A namespace is a collection of currently defined symbolic names along with information about the object that each name references.

Perhaps an easier description is to think of a namespace as a dictionary in which the keys are the object names and the values are the objects themselves. 

Extra Reading:
If you read the Zen of Python you'll find this quote "Namespaces are one honking great idea—let’s do more of those!"
If you want to see the Zen if Python - open an immediate window for Python and type the following command:
>>> import this
and press enter


Global Namespace
The global namespace contains any names defined at the level of the main program.
Python creates the global namespace when the main program body starts, and it remains in existence until the interpreter terminates.


Local and Enclosed Namespaces
Functions don't exist on their own, the interpreter creates a new namespace whenever a function executes. That namespace is local to the function and remains in existence until the function terminates (and exists from memory).
see the functionsTest.py file and execute it

In this example, function g() is defined within the body of f(). Here’s what’s happening in this code:

Lines 1 to 12 define f(), the enclosing function.
Lines 4 to 7 define g(), the enclosed function.
On line 15, the main program calls f().
On line 9, f() calls g().

When the main program calls f(), Python creates a new namespace for f(). Similarly, when f() calls g(), g() gets its own separate namespace. The namespace created for g() is the local namespace, and the namespace created for f() is the enclosing namespace.
For each namespace will remain in existence until its respective function terminates. Python does not always immediately reclaim the memory (called garbage collection) allocated for those namespaces when their functions terminate, but all references to the objects they contain cease to be valid.

Scope
With multiple, distinct namespaces means several different instances of a particular name can exist simultaneously while a Python program runs. 
As long as each instance is in a different namespace, they’re all maintained separately and won’t interfere with one another.
However if you name blar in your code and blar exists in several namespaces, but does the Python interpreter know which one you are refering to?

To solve this the concept of scope has been created. The scope of a name is the region of a program in which that name has meaning.
The interpreter determines this at runtime based on where the name has been defined in code and where in the code the name is referenced.

If your code refers to the name blar then Python searches for blar in the following namespaces in the order shown:
    Local
      ↓
   Enclosing
      ↓
   Global
      ↓
   Built-in

Local: If you refer to blar inside a function, then the interpreter first searches for it in the innermost scope that’s local to that function.
Enclosing: If blar isn’t in the local scope but appears in a function that resides inside another function, then the interpreter searches in the enclosing function’s scope.
Global: If neither of the above searches is fruitful, then the interpreter looks in the global scope next.
Built-in: If it can’t find blar anywhere else, then the interpreter tries the built-in scope.

The interpreter searches for a name from the inside out, looking in the local, enclosing, global, and finally the built-in scope:

--------------------------                     
| | | |       |   |  |   |
| | | |       |   |  |   |
| | | | Local |   |  |   |              
| | | |--------   |  |   |                 
| | |    Enclosed |  |   |
| | -----------------|   |
| | |         Global |   |
| | ------------------   |
| | |            Builtin |
--------------------------

Builtin namespace [not required for exam but useful to be aware of]
The built-in namespace contains the names of all of Python’s built-in objects, such as print or __name__ or str
These are available at all times when Python is running. You can list the objects in the built-in namespace by openning an immediate window for Python and type the following command:
>>> dir(__builtins__)
and press enter


Extra Reading:
See this link for scope https://en.wikipedia.org/wiki/Scope_(computer_science)