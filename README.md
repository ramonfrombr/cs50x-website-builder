# CS50x Website Builder

This project uses ChatGPT to translate the content from Harvard University's CS50 course, and then uses Flask to build the content into a set of static files that can be hosted on Github Pages.

This program has been used to build the websites for the Portuguese, French, and Spanish versions of the course:

- [CS50x em Português](https://cs50xemportugues.github.io/)
- [CS50x en Français](https://cs50xenfrancais.github.io/)
- [CS50x en Español](https://cs50xenespanol.github.io/)

But it can be used to translate the course to any language!

## Dependencies & Extensions

- Flask
- pytest
- marko
- Better Jinja (VSCode Extension): It prevents Jinja templates from formatting incorrectly.

# Development Setup

Run the following commands to setup development environment.

First, define the course language:

```
export COURSE_LANGUAGE=spanish
```

Define the application as `app`. That's the name of the package.

```
export FLASK_APP=app
```

Define the Flask environment as development mode, for hot reloading.

```
export FLASK_ENV=development
```

Define Flask debug tool as true, to display helpful debug messages.

```
export FLASK_DEBUG=1
```
