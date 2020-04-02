# Airbnb clone project

## Definition

It's a simple system to preserve, read and modify models that represents entities for the airbnb services.

This behavior is achieved by the console program, this program is capable of reading a .json file , deserialize it and create instaces for python objects, also it's capable of modify existimg objects create new ones and store them again in tje .json file.

This module is just a little piece for the airbnb clone full implementation, will change it's scope in the future.

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name>`
Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

### Authors :black_nib:
* **Sebastián López Herrera** <[sebas119](https://github.com/sebas119)>
* **Daniel Rodriguez** <[danrocus1994](https://github.com/danrocus1994)>