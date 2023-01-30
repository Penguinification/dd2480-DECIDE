# DECIDE

A function used by a hypothetical anti-ballistic missile defense system

## How to use
To run the program, first ensure that you have Python 3.10 or later installed. Then, run the command:
```console
python main.py
```

Inputs are read from `stdin` in the same order they appear in the [specification](https://canvas.kth.se/courses/37918/files/6157550/download). Each input should be written on a new line. This includes individual matrix elements, which are read row-by-row. Coordinates are read as tuples following standard Python syntax, e.g. `(1, 1)`.

To run the unit tests, first make sure you have the `pytest` Python package installed. It can be installed using:
```console
pip install pytest
```

The tests can then be run using:
```console
pytest
```

## Way-of-Working
The group is currently in the *In use* stage. The criteria for the earlier stages are fulfilled as a general workflow has been established including the choice of platforms (GitHub for the remote repository and Discord for communication), commit formatting conventions, branching strategy and how the issue tracker and pull requests should be used. This general way-of-working is in use by some group members and being adapted to the group's needs. An example of this is a minor change to the branching strategy in which the issue-3 branch became a sort of intermediate branch between the development branches and the main branch for the lic functions specifically. The reason that the *In Place* stage has not been reached yet is that some group members still are getting used to and learning the general workflow, mostly related to using Git, GitHub and writing unit tests.

## Contributions
This project was developed as a part of the course DD2480 at the KTH Royal Institute of Technology by group 27.

The `lic_0`, `lic_1`, `lic_2`, `lic_5`, `pum` and `launch` functions and their unit tests were implemented by Elias.
The `lic_3`, `lic_4`, `lic_6`, `lic_7`, `fuv` and `validate_input` functions and their unit tests were implemented by Edit.
The `main` function was written collaborately by the group as a whole.
Contributions from the remaining group members will be added once they are pushed and merged.

