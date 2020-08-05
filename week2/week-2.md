- Python
  - Challenge 1
  - Documentation & Resources
  - Loops
  - Lists
  - Dicts
  - If/Else
- Weekly Homework:
  - Complete challenge 1 of Code Club Crew
  - Commit it to their Github Repo

### Week 2
#### Overview
This week's focus is building a script in Python that will function as our application for the rest of the Bootcamp. DevOps Engineers regularly need to write small scripts to manage applications at scale or to shore up blind spots in their tooling. The most popular languages in the DevOps space for writing scripts are Python and Shell/Bash, and to a lesser extent Go.

We're going to focus on Python because the readability of Shell scripts quickly approaches zero when working with JSON or YAML.

---

#### Additional Reading:
> Take the time to familiarize yourself with the documentation. A great deal of early-stage programming involves reading documentation and learning the syntax of commands. Remember to ask questions in the C3 Slack. Much of the documentation is written by programmers and for programmers; Making it obtuse to read without practice.

- [Python Variables](https://www.learnpython.org/en/Variables_and_Types)
- [Python Dictionaries](https://realpython.com/python-dicts/)
- [Python Lists](https://www.openbookproject.net/books/bpp4awd/ch03.html)
- [Python Loops](https://www.learnpython.org/en/Loops)
- [Python Conditionals](https://www.learnpython.org/en/Conditions)

---

#### Using Python
> Writing _good_ Python is beyond the scope of this bootcamp. We'll suffice with working Python.

- [Download Python](https://www.python.org/downloads/) and install it.
- Create the files inside of your repo from Week 1:
  - `main.py`
  - `requirements.txt`
- Open `main.py` with Atom
  - Add the 'shebang' to the top
    - `#! python`
  - Add an `import` statement when adding libraries. (Make sure to add these libraries to `requirements.txt` as well.)
    - `import swapi-python`
- [Draw the rest of the owl](https://i.kym-cdn.com/photos/images/original/000/572/078/d6d.jpg)

---

#### Dictionaries
Dictionaries are Key/Value pairs, easily identified in Python because they're contained in curly braces `{}`. Dictionaries are extremely versatile; Their values can be almost any other data type, including other dictionaries.
- A dictionary's `key` must be unique.
  ```
  {
    key: value
  }
  ```
- Here's a dict with nested dicts:
  ```
  {
    key1: {
      key2: {
        key3: value1
      }
    }
  }
  ```
> If we wanted to know the value of `value1` we would do `print(key1["key2"]["key3"])`

- Use the `in` conditional to to check if a key exists in a dict
  ```
  if "key" in the_dictionary:
    print("I found key!")
  else:
    print("I didn't find key...")
  ```

---

#### Lists
Lists can be easily identified by their brackets `[]`. Lists differ from dicts in a few ways; For instance, rather than a dict's `key` a list uses an `index` which is a numerical value assigned to each slice of the list.

- Example Lists:
  ```
  numbers = [1,2,3,4]
  food = ["apple","banana","pear","potato"]
  ```
> Similar to working with a dict we can get a value out of a list by referencing its index: `print(food[1])`

---

#### Loops
Loops are what we use to iterate through a list or dict and work with them en masse. We'll be covering the `for` loop.
