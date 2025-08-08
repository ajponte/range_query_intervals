[![tsrange-intervals](https://github.com/ajponte/tsrange_intervals/actions/workflows/python-app.yml/badge.svg)](https://github.com/ajponte/tsrange_intervals/actions/workflows/python-app.yml)

# Range Query Intervals

This project is an example of how to use a [Range Tree](https://en.wikipedia.org/wiki/Range_tree)
to find overlapping intervals, where each interval represent a start and end epoch value.

In Postgres, this can be implemented in a fairly straightforward way using [tsrange](https://www.postgresql.org/docs/current/rangetypes.html).

## Range Interface
This project includes an interface, `TimeRangeInterval` to interact with different cumulative indices of ranges.

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
