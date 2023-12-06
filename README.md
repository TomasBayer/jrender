# jinjarender

`jinjarender` is a command-line tool that renders [Jinja template files](https://jinja.palletsprojects.com/) using a
context built from YAML files and mappings supplied on the command line. It is primarily designed for quickly testing
template files.

## Installation

Requires Python version 3.9 or higher and pip.

```bash
pip install jinjarender
```

## Example

```bash
# Create a template file
> echo "Hello {{name}}" > hello.jinja

# Render the template by supplying values
> jinjarender hello.jinja name=World

# Values provided through the command line are always interpreted as strings. For other data types or more complex data
# structures, provide the context in a YAML file.
> jinjarender hello.jinja -f vars.yaml
```
