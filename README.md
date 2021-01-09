![project cover](.static/cover.jpg)

# Chatroomies

[![Coverage](https://codecov.io/gh/claudinoac/chatrommies/branch/master/graph/badge.svg)](https://codecov.io/gh/claudinoac/chatroomies)
![Deploy](https://github.com/claudinoac/chatroomies/workflows/Deploy/badge.svg)
![Tests](https://github.com/claudinoac/chatroomies/workflows/Tests/badge.svg?branch=dev)
![Security Checks](https://github.com/claudinoac/chatroomies/workflows/Security/badge.svg?branch=dev)
![Lint](https://github.com/claudinoac/chatroomies/workflows/Lint/badge.svg?branch=dev)
[![PyPI version](https://badge.fury.io/py/chatroomies.svg)](https://badge.fury.io/py/chatroomies)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A web-based chat system

Featuring:

- ...


## Table of Contents:


- [Installation](#installation)
- [Project Architecture](#architecture)
- [Contributing](#contributing)
- [Team](#team)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)

---

## Installation:

### Requisites:
- Install [docker](https://www.docker.com/products/docker-desktop) and [docker-compose](https://docs.docker.com/compose/install/)


### Clone:

- Clone this repository:
	- ` git clone git@github.com:claudinoac/chatroomies`

### Setup:

- Build and run container:
	+ ```$ docker-compose up -d```


- Access [http://localhost:...](http://localhost:...')

- Log-in into the platform
- Use the chat

---

## Architecture Overview (C4 Model):

The architecture model was created using [Structurizr DSL](https://github.com/structurizr/dsl) and [PlantUML](https://plantuml.com)

![system-perspective](architecture-models/SystemPerspective.png)
![application-perspective](architecture-models/ApplicationPerspective.png)


## Testing:


### Unit tests:

- The unit tests are based on [Django test suite](https://docs.djangoproject.com/en/3.0/topics/testing/) and [PyTest]()
	
- All the unit tests will be in the `tests/unit` path, inside each application. 
- To run the unit tests, run 
	- ```$ make test unit```

### Integration tests
- The integration tests are based on [Behave BDD Testing](https://behave.readthedocs.io/en/latest/)

- All the integration tests should be located in `tests/integration` path, inside each application

- Every integration test has two parts: the .feature and the .py (steps) file
	- For details, check the [behave's documentation](https://behave.readthedocs.io/en/latest/)

- To run the integration tests, run 
	- ```$ make test integration```
	
---

## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/claudinoac/chatroomies.git`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/claudinoac/chatroomies/compare/" target="_blank">`https://github.com/claudinoac/chatrommies/compare/`</a>.

---

## Team

### Maintainers:
| <a href="http://github.com/claudinoac" target="_blank">**Alisson Claudino**</a>|
| :---: |
| [![Alisson Claudino](https://avatars3.githubusercontent.com/u/23270841?s=200&v=4)](http://fvcproductions.com)  |
| <a href="http://github.com/fvcproductions" target="_blank">`github.com/claudinoac`</a> |

### Contributors:
---

## FAQ

- **How can I can do ...?**
    - Response will be here

---

## Support

Reach out to me at one of the following places!

- Twitter at <a href="http://twitter.com/_claudinoac" target="_blank">`@_claudinoac`</a>

---

## License

- **[GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)**

