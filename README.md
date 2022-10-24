# AirBnB clone - The console #

![This is an image](https://repository-images.githubusercontent.com/520063788/a91abf2d-82e3-40e6-96d7-75043c684ff3)

## Table of Contents

- [Description of the Project](https://github.com/Giogap/holbertonschool-AirBnB_clone/blob/main/README.md#description-of-the-project/)
- [Description of the command interpreter](https://github.com/Giogap/holbertonschool-AirBnB_clone/blob/main/README.md#description-of-the-command-interpreter).
- [How to Start It](https://github.com/Giogap/holbertonschool-AirBnB_clone/blob/main/README.md#how-to-start-it)
- [How to Use It](https://github.com/Giogap/holbertonschool-AirBnB_clone/blob/main/README.md#how-to-use-it)
- [Examples](https://github.com/Giogap/holbertonschool-AirBnB_clone/blob/main/README.md#examples)
- [Authors](https://github.com/Giogap/holbertonschool-AirBnB_clone/blob/main/README.md#authors).


## Description of the Project

**First step: Write a command interpreter to manage your AirBnB objects.**

This is the first step towards building your first full web application: the **AirBnB clone.** This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration… 

Each task is linked and will help you to:

    - put in place a parent class (called BaseModel) to take care of the initialization, serialization and          deserialization of your future instances
    - create a simple flow of serialization/deserialization:
        - Instance <-> Dictionary <-> JSON string <-> file
    - create all classes used for AirBnB that inherit from BaseModel
        - User
        - State
        -City
        - Place ..
    - create the first abstracted storage engine of the project: 
        - File storage.
    - create all unittests to validate all our classes and storage engine

## Description of the command interpreter

The console will be used for access of the functionalities offered by our components.
In our case, we want to be able to manage the objects of our project:

    - Create a new object (ex: a new User or a new Place)
    - Retrieve an object from a file, a database etc…
    - Do operations on objects (count, compute stats, etc…)
    - Update attributes of an object
    - Destroy an object

## How to Start It
Execution
```
Your shell should work like this in interactive mode:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

![This is an image](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20221024%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221024T183930Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=14fe1066cf4b091e1bc67957b95248e2e3d069d492a21efc8977ede18b441193)

## How to Use It

## Examples


## Authors
### This file lists all individuals having contributed content to the repository.
- Giovanni Pérez <5187@holbertonstudents.com>
- Silvana Jaramillo <5211@holbertonstudents.com>

