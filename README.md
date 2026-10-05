# Kargar

A simple project generator written in Python where you can generate projects with ease.

## Installation

> ![NOTE]
>
> Kargar is not ready yet.

It's a piece of cake. Just make sure you have [uv](https://docs.astral.sh/uv) installed.

Then run:

```shell
uv tool install kargar
```

## The Name?

Kargar means _builder_ in Persian. Why I choose this name? Because this project generate projects.

## Developing Generators

Kargar generators are distributed as Git repositories rather than Python packages. This keeps Kargar's core on PyPI while allowing anyone to create and publish generators independently.

A generator is a **project blueprint**, not a framework that takes over the generation process. Generators primarily define the files, templates, and configuration needed to create a project, while Kargar handles the generation itself.

### Using a Generator

Generators are referenced using:

```text
OWNER/NAME
```

For example:

```bash
kargar new ManiProjs/react
```

By default, Kargar expands this to:

```text
ManiProjs/kargar-react
```

To use the repository name exactly as specified, use `--exact`:

```bash
kargar new ManiProjs/react --exact
```

which resolves to:

```text
ManiProjs/react
```

### Generator Repository

A generator repository might look like:

```text
kargar-react/
├── kargar.toml
├── templates/
│   ├── package.json
│   ├── tsconfig.json
│   └── src/
│       └── ...
└── README.md
```

The `kargar.toml` file describes the generator, while `templates/` contains the project files that Kargar will generate.

This is an example for a `kargar.toml`:

```toml
name = "react"
description = "A React + TypeScript project"
version = "1.0.0"

[generator]
language = "typescript"

[template]
directory = "templates"

[variables]
project_name = "my-app"
```

### Why Git Repositories?

Generators do not need to be published to PyPI.

This means Kargar can have an ecosystem of community generators without filling PyPI with packages such as:

```text
kargar-react
kargar-vue
kargar-rust
kargar-cli
...
```

Anyone can create a generator, put it in a Git repository, and make it available to Kargar users.

### Kargar vs. Traditional Generator Frameworks

Kargar is intentionally different from generator frameworks such as Yeoman.

A Kargar generator is primarily a **description of what a project should look like**. Kargar remains responsible for interpreting that description and generating the project.

In other words:

```text
Traditional generator
    Generator → executes generation logic → project

Kargar
    Generator → describes project → Kargar → project
```

This keeps generators simple, portable, and easy to share.
