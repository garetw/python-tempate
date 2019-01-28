# Tested Functional Python

# Goal:
    - to provide an easy entry into functional python testing
    - to create an easy-to-follow testing template for python
    - to provide repeatable steps to help produce quality code
    - to establish some basic directory structure strategies

# Foreward:
This project is just a template including some basic tools, and a basic example of constructing a functional python project.

# RTFM(S)
| concept | fucking manual |
| ------ | ------ |
| pipenv | [https://pipenv.readthedocs.io/en/latest/][PlDb] |
| pytest | [https://pythontesting.net/framework/pytest/pytest-introduction/][PlGh] |
| pylint | [https://pylint.readthedocs.io/en/latest/][PlGd] |
| autopep8 | [https://pypi.org/project/autopep8/][PlOd] |
| map_filter_reduce | [http://book.pythontips.com/en/latest/map_filter.html][PlMe] |
| logging | [https://docs.python.org/3/library/logging.html][PlGa] |

# Installation:
### local host
Project can be installed on any pipenv-equipped machine (rtfm)
`pipenv install --three --dev`
`pipenv run test`

### Docker
Project can be built in any docker-equipped machine
`docker build -t=ubuntu:test_sample .`
`docker run -it ubuntu:test_sample /bin/bash`
`cd to /opt`

# TESTING.
### personal ethos:
I want the work I produce to be of the highest quality that I can release.
I want to reduce both the human entropy (input), and effort into any given system
### evangelization:
Code changes. Consistently. That's a fact. Testing strategies help us compartmentalize
discreet functionality into modules that can be easily modified later. Many times we
get stuck in a rut of not being able to solve one particular piece of our code, when in fact, there are many other problems to be solved in the codebase. What if you could skip the function causing you frustration, and work on another one that you know you'll need later? Many times programs evolve entirely different from your expectation.
### benefits:
It's hard to really explain how beneficial testing is until you start try it. But as programmers, or people who engage in the art of writing code, why don't we write a 
program to help us write our program?
    
- testing begets testing, that is to say, the more you test, the more you want to test.
- saves you immense time in troubleshooting. Like... Immense.
- allows you a framework to start constructing your script from the inside-out
- will point out syntax errors, and provide helpful metadata
- breaks dependence on the print() function
- allows long-term maintenance of the codebase
- gives you functioning examples and built-in "documentation" of how the code works
- when you're done with your tests, you're almost done with the main script, because you've already written the functions. Now all you have to do is coordinate them

### limitations:
- 30-40% code overhead. Moar Lines. :(
- in 20% of cases a clear testing scenario i.e. a "clear way" to test is not obvious
- it can put you into a false sense of security if your tests are ill-conceived
- sometimes requires "mocks" or fake-data (i.e. a function that prints a new log-line into a text file to emulate a running server log), which introduces entropy
- you end up writing support functions for your tests that are only used in that context

# ------------------------------------------
# Shall we begin?
# ------------------------------------------

# PIPENV
### Ok.
Pipenv is basically a wrapper of both the popular `virtualenv` and `pip` projects.
It has a lot of power, it does a lot of things. I suggest you go read up on it here:



It has a very convenient interface, and centers around a file in your project directory called your Pipfile:
_(pipfile is written in TOML)_
```
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[scripts]
test = "py.test -rs ./src/"
autopep8 = "python -m autopep8 --in-place --aggressive --aggressive ./src/*.py"
lint = "pylint ./src/*.py"

[dev-packages]
pytest = "*"
autopep8 = "*"
pylint = "*"

[packages]
requests = "*"

[requires]
python_version = "3.7"

```
It's split out into subsections:

### Requires:
assoc_commands: `pipenv install`
Declares teh version of python you would like pipenv to execute this environment in.
Note: The declared version must be installed on the system.

### Packages:
assoc_commands: `pipenv install`
This helps you manage modules more effectively as the functionality of your dependencies changes over time. It de-complexifies the previous problem wheren you had to `pip install` a package, and manually add it to a `requirements.txt` file.

```
[packages]
requests = "*" # will install latest
requests = "1.4.0" # Equal or later than 1.4.0
requests = "2.13" # Equal or earler than 2.13.0
requests = ">2.10" # will install 2.19.1 but not 2.19.0
```

The following commands can be executed within context to the same effect:
```
$ pipenv install "requests>=1.4"
$ pipenv install "requests<=2.13"
$ pipenv install "requests>2.19"
```

### Dev-Packages:
assoc_commands: `pipenv install --dev`
This does the same as packages, but for development libraries, like our tests and linters.
```
[dev-packages]
pytest = "*"
pylint = "*"
autopep8 = "*"
```
Same as above will tag them as `dev` on install
```
$ pipenv install --dev pytest
$ pipenv install --dev pylint
$ pipenv install --dev autopep8
```

### Scripts:
# Hot damn, my favorite.
assoc_commands: `pipenv run <command>`
The Scripts section allows you to write scripts for pipenv to execute _contextually_
This allows you to invoke whole python commands, _or other arbitrary commands_ from outside of your provided environment by simply executing something like:

`pipenv run test` as defined in the following Pipenv file section

```
[scripts]
test = "py.test -rs ./src/"
```

This will run `py.test -rs ./src/` inside of the `pipenv` context that was previously-installed.

^^ This command will ultimately run your final script:
`pipenv run app.py`

### _okay, but how the fuck do I use it?_
# check out this dir structure.
    .
    ├── Dockerfile
    ├── src
    |   ├── sample_lib.py
    |   └── test_sample_lib.py
    ├── app.py
    ├── Pipfile

### Directory structure
- Dockerfile: allows you to build this project and run it as a docker container. (_see Docker_)
- src: folder where you store all your custom libraries alongside their tests
- app.py: main execution function
- Pipfile: dependencies i.e. `requests`, as well as custom environment scripts

### _sample app directory structure_
    .
    ├── Dockerfile
    ├── src
    |   ├── aws.py
    |   └── test_aws.py
    |   ├── custom_redis.py
    |   └── test_custom_redis.py
    |   ├── elasticsearch_tools
    |   └── test_elasticsearch_tools.py
    ├── app.py
    ├── Pipfile

Cool! This lets us put all of our libraries neatly with their tests under the folder `/src`
This also allows us to call into those libraries from a "higher-order" function called `app.py`
This will make it possible to coordinate across many libraries from one `app.py` file, and thus your `Application`
Finally, this allows us to call our entire app via the following command

`pipenv run app`
this should call
```
[scrpits]
app = "python app.py"
```
Your project folder structure may look like this:

    .
    ├── Dockerfile
    ├── src
    |   ├── aws.py
    |   └── test_aws.py
    |   ├── custom_redis.py
    |   └── test_custom_redis.py
    |   ├── elasticsearch_tools
    |   └── test_elasticsearch_tools.py
    ├── app.py
    ├── Pipfile

Given the structure, the following _could_ be an example
`app.py`
```
import src.aws as aws #import our aws module from the local /src dir
import src.custom_redis as custom_redis #import the custom_redis module/lib from the local /src dir
import src.elasticsearch_tools  as elasticsearch_tools #import the custom elasticsearch_module from the /src/dir

if __name__ == "__main__":
    aws_operation = aws.get_some_filtered_instances_or_something()
    load_redis = custom_redis.put(aws_operation)
    load_elasticsearch = elasticsearch_tools.put(aws_operation)
    query_elasticsearch = elasticsearch_tools.query(some_instance_exists?)
```
# APP.PY DO THE THINGS!!!
^^ The `app.py` file rolls up all of your subdirectories into immediately referencable, hierarchical units.

[//]: #

[PlDb]: <https://pipenv.readthedocs.io/en/latest/>
[PlGh]: <https://pythontesting.net/framework/pytest/pytest-introduction/>
[PlGd]: <https://pylint.readthedocs.io/en/latest/>
[PlOd]: <https://pypi.org/project/autopep8/>
[PlMe]: <http://book.pythontips.com/en/latest/map_filter.html>
[PlGa]: <https://docs.python.org/3/library/logging.html>