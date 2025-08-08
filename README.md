[![tsrange-intervals](https://github.com/ajponte/tsrange_intervals/actions/workflows/python-app.yml/badge.svg)](https://github.com/ajponte/tsrange_intervals/actions/workflows/python-app.yml)

# Range Query Intervals

This project is an example of how to use a [Range Tree](https://en.wikipedia.org/wiki/Range_tree)
to find overlapping intervals, where each interval represent a start and end epoch value.

In Postgres, this can be implemented in a fairly straightforward way using [tsrange](https://www.postgresql.org/docs/current/rangetypes.html).

## Range Interface
A range's interface can be thought of as a [relation](https://en.wikipedia.org/wiki/Relation_(mathematics) of a [partially ordered set](https://en.wikipedia.org/wiki/Partially_ordered_set).
The (infimum)[https://en.wikipedia.org/wiki/Infimum_and_supremum] of the set should be a direct mapping to `models.partial_interval`.

For instance, on the set with keys `(K1, K2, ...Kn)`, where `K1 <= K2 <=...<=Kn`, and values `(V1, V2, ...Vn)`, a relation would
be a mapping `R(k): k -> v`.

The relation is encapuslated in `PartialInverval` through the `open_interval` and `label` values.

## Package Management
### Poetry
This project uses `poetry` for package management.

### Tox Automation
This project includes a `tox.ini` file to automate tasks such as
* invoking pytest
* linting
* formatting
* type-checking
* distribution building.

A fresh `tox` build can be invoked via `tox -r`, which whill invoke each task.
See https://github.com/tox-dev/tox for more info.

### Distribution
A local distribution of the package can be created either through
```shell
 poetry build
```
or
```shell
 tos -e dist
```
Since the build is dependent on `poetry`, the commands are equivalent.

## Unit Tests
This project uses `pytest`. You can invoke tests in a poetry environment, via
```shell
 poetry run pytest tests
```

## Formatting
This project uses `black` to enforce PEP-8 formatting rules.
You can format any file with
```shell
 poetry run black <target>
```
where `<target>` is the directory or file to run the tool on.

With `tox`, you can also check formatting any time with
```shell
 tox -e format
```
Note that since tox is intended to be invoked as part of a CI
pipeline, we will never rewrite files.

## Type Checking
This project (somewhat) enforces static typing through `mypy`.
