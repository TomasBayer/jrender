import collections
import sys
from typing import Annotated

import jinja2
import typer
import yaml

app = typer.Typer()


@app.command()
def render(
        *,
        template_file: Annotated[typer.FileText, typer.Argument(
            help="Path to the jinja template file.",
        )],
        no_input: Annotated[bool, typer.Option(
            "--no-input", '-n',
            help="Render the template with an empty context.",
        )] = False,
):
    try:
        template = jinja2.Template(template_file.read())
    except jinja2.exceptions.TemplateSyntaxError as e:
        sys.exit(f'Template is invalid Jinja2: {e}')

    if no_input:
        data = {}
    else:
        try:
            data = yaml.safe_load(sys.stdin)
        except yaml.YAMLError:
            sys.exit('Input data is not valid YAML/JSON.')

        if not isinstance(data, collections.abc.Mapping):
            sys.exit('Input data is not a valid YAML/JSON dictionary')

    print(template.render(**data))  # noqa: T201
