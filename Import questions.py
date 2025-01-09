import psycopg2

# PostgreSQL database connection details
DB_HOST = "127.0.0.1"
DB_NAME = "questions_db"
DB_USER = "postgres"
DB_PASSWORD = "1010"

# List of questions to insert into the database
questions = [
    {
        "question": "What is true about Python packages? (Choose two.)",
        "code": None,
        "options": "a code designed to initialize a package’s state should be placed inside a file named init.py;;-;a package’s contents can be stored and distributed as an mp3 file;;-;__pycache__ is a folder that stores semi-compiled Python modules;;-;the sys.path variable is a list of strings",
        "answer": "__pycache__ is a folder that stores semi-compiled Python modules;;-;the sys.path variable is a list of strings",
        "multiplea": "1",
        "category": "5",
        "exam": "1"
    },
    {
        "question": "What is the expected output of the following code?",
        "code": "import sys\nimport math\nb1 = type(dir(math)) is list\nb2 = type(sys.path) is list\nprint(b1 and b2)",
        "options": "None;;-;True;;-;0;;-;False",
        "answer": "True",
        "multiplea": "0",
        "category": "1",
        "exam": "1"
    },
    {
        "question": "A Python package named pypack includes a module named pymod.py which contains a function named pyfun(). Which of the following snippets will let you invoke the function? (Choose two.)",
        "code": None,
        "options": "from pypack.pymod import pyfun\npyfun();;-;import pypack\npymod.pyfun();;-;from pypack import *\npyfun();;-;import pypack\nimport pypack.pymod\npypack.pymod.pyfun()",
        "answer": "from pypack.pymod import pyfun\npyfun();;-;import pypack\nimport pypack.pymod\npypack.pymod.pyfun()",
        "multiplea": "1",
        "category": "5",
        "exam": "1"
    },
    {
        "question": "Assuming that the code below has been executed successfully, which of the following expressions will always evaluate to True?",
        "code": "import random\nv1 = random.random()\nv2 = random.random()",
        "options": "len(random.sample([1,2,3],1)) > 2;;-;v1 == v2;;-;random.choice([1,2,3]) > 0;;-;v1>1",
        "answer": "random.choice([1,2,3]) > 0",
        "multiplea": "0",
        "category": "4",
        "exam": "1"
    },
    {
    "question": "With regards to the directory structure below, select the proper forms of the directives in order to import module_c. (Choose two.)",
    "code": "pypack (dir)\n│\n├── upper (dir)\n│   └── lower (dir)\n│       └── module_c.py (file)\n├── module_b.py (file)\n└── module_a.py (file)",
    "options": "from pypack.upper.lower import module_c;;-;import pypack.upper.lower.module_c;;-;upper.lower.module_c;;-;import upper.lower.module_c",
    "answer": "from pypack.upper.lower import module_c;;-;import pypack.upper.lower.module_c",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "Which one of the platform module functions should be used to determine the underlying platform name?",
    "code": None,
    "options": "platform.processor();;-;platform.uname();;-;platform.python_version();;-;platform.platform()",
    "answer": "platform.platform()",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is the expected behavior of the following code?",
    "code": "s = '2A'\ntry:\n    n = int(s)\nexcept ValueError:\n    n = 2\nexcept ArithmeticError:\n    n = 1\nexcept:\n    n = 0\n\nprint(n)",
    "options": "The code is erroneous and it will not execute;;-;It outputs 1;;-;It outputs 2;;-;It outputs 0",
    "answer": "It outputs 2",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "Which of the following snippets will execute without raising any unhandled exceptions? (Choose two.)",
    "code": None,
    "options": "Option A:\n\n```python\ntry:\n    print(-1/1)\nexcept:\n    print(0/1)\nelse:\n    print(1/1)\n```\n\nOption B:\n\n```python\ntry:\n    x = 1\nexcept:\n    x = x + 1\nelse:\n    x = x + 2\n```\n\nOption C:\n\n```python\ntry:\n    x = y + 1\nexcept (NameError, SystemError):\n    x = y + 1\nelse:\n    y = x\n```\n\nOption D:\n\n```python\ntry:\n    x = 1 / 0\nexcept NameError:\n    x = 1 / 1\nelse:\n    x = x + 1\n```",
    "answer": "Option A;;-;Option B",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is the expected behavior of the following code?",
    "code": "string = str(1/3)\ndummy = ''\nfor character in string:\n    dummy = dummy + character\n    print(dummy[-1])",
    "options": "It outputs each character of '0.3333333333333333' one by one;;-;It raises an exception;;-;It outputs '3' once;;-;It outputs nothing",
    "answer": "It outputs each character of '0.3333333333333333' one by one",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is true about the following snippet? (Choose two.)",
    "code": "class E(Exception):\n    def __init__(self, message):\n        self._message = message\n    def __str__(self):\n        return \"it's nice to see you\"\n\ntry:\n    print(\"I feel fine\")\n    raise E(\"what a pity\")\nexcept E as e:\n    print(e)\nelse:\n    print(\"the show must go on\")",
    "options": "The string what a pity will be seen;;-;The string it's nice to see you will be seen;;-;The code will raise an unhandled exception;;-;The string I feel fine will be seen",
    "answer": "The string it's nice to see you will be seen;;-;The string I feel fine will be seen",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is the expected behavior of the following code?",
    "code": "my_list = [1, 2, 3]\n\ntry:\n    my_list[3] = my_list[2]\nexcept BaseException as error:\n    print(error)",
    "options": "It outputs error;;-;It outputs;;-;The code is erroneous and it will not execute;;-;It outputs list assignment index out of range",
    "answer": "It outputs list assignment index out of range",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "Which of the following expressions evaluate to True? (Choose two.)",
    "code": None,
    "options": "ord('0') - ord('9') == 10;;-;len('') == 2;;-;chr(ord('z') - 1) == 'y';;-;len('1234') == 4",
    "answer": "chr(ord('z') - 1) == 'y';;-;len('1234') == 4",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "Which of the following expressions evaluate to True? (Choose two.)",
    "code": None,
    "options": " 'XY'.lower() > 'xy';;-; '9'*2 != '2'*9;;-; float(3.14) == str(3*1.14);;-; 1+1 == int('1'+'2'*2)",
    "answer": "'9'*2 != '2'*9;;-;1+1 == int('1'+'2'*2)",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is the expected behavior of the following code?",
    "code": "string = str(1/3)\ndummy = ''\nfor character in string:\n    dummy = dummy + character\n    print(dummy[-1])",
    "options": "It outputs 3;;-;It outputs 'None';;-;It outputs 0;;-;It raises an exception",
    "answer": "It raises an exception",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is the expected behavior of the following code?",
    "code": "the_list = 'alphabetagamma'.split('a')\nthe_string = ''.join(the_list)\nprint(the_string.isalpha())",
    "options": "It outputs True;;-;It outputs False;;-;It outputs nothing;;-;It raises an exception",
    "answer": "It outputs False",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "Which of the following invocations are valid? (Choose two.)",
    "code": None,
    "options": "sort('python');;-;'python'.find('');;-;'python'.sort();;-;sorted('python')",
    "answer": "'python'.find('');;-;sorted('python')",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "Which of the following expressions evaluate to True? (Choose two.)",
    "code": None,
    "options": "'in' in 'in';;-;'ha' in 'Thames';;-;'in' not in 'not';;-;'r.upper()' in 'Thames'",
    "answer": "'in' in 'in';;-;'ha' in 'Thames'",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "Assuming that the snippet below has been executed successfully, which of the following expressions will evaluate to True? (Choose two.)",
    "code": "string = 'python'[-2:]\nstring = string[-1] + string[-2]",
    "options": "len(string) == 3;;-;string[0] == 'o';;-;string[0] == string[-1];;-;string is None",
    "answer": "string[0] == 'o';;-;string[0] == string[-1]",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "Which of the following statements are true? (Choose two.)",
    "code": None,
    "options": "An escape sequence can be recognized by the / sign put in front of it;;-;ASCII is a subset of UNICODE;;-;In ASCII stands for Internal Information;;-;A code point is a number assigned to a given character",
    "answer": "ASCII is a subset of UNICODE;;-;A code point is a number assigned to a given character",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "A property that stores information about a given class's super-classes is named:",
    "code": None,
    "options": "__bases__;;-;__super__;;-;__classes__;;-;__ancestors__",
    "answer": "__bases__",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "Which of the following expressions evaluate to True? (Select two answers.)",
    "code": None,
    "options": "len('c') == 1;;-;len('') == 0;;-;chr(ord('B') + 1) == 'C';;-;chr(ord('Z') - 1) == 'Y'",
    "answer": "len('c') == 1;;-;chr(ord('Z') - 1) == 'Y'",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "With regards to the directory structure below, select the proper forms of the directives in order to import module_a. (Select two answers.)",
    "code": "pypack (dir)\n│\n├── upper (dir)\n│   └── lower (dir)\n│       └── module_c.py (file)\n├── module_b.py (file)\n└── module_a.py (file)",
    "options": "import pypack.module_a;;-;import module_a from pypack;;-;import module_a;;-;from pypack import module_a",
    "answer": "import pypack.module_a;;-;from pypack import module_a",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "You are going to read 16 bytes from a binary file into a bytearray called data. Which lines would you use? (Choose two.)",
    "code": None,
    "options": "data = bytearray(16)\nbf.readinto(data);;-;data = binfile.read(bytearray(16));;-;bf.readinto(bytearray(16));;-;data = bytearray(binfile.read(16))",
    "answer": "data = bytearray(16)\nbf.readinto(data);;-;data = bytearray(binfile.read(16))",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "Which of the following statements are true? (Select two answers.)",
    "code": None,
    "options": "Closing an open file is performed by the closefile() function;;-;The second open() argument describes the open mode and defaults to 'w';;-;If open()'s second argument is 'r' the file must exist or open will fail;;-;If open()'s second argument is 'w' and the invocation succeeds, the previous file's content is lost",
    "answer": "If open()'s second argument is 'r' the file must exist or open will fail;;-;If open()'s second argument is 'w' and the invocation succeeds, the previous file's content is lost",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "The __bases__ property contains:",
    "code": None,
    "options": "Base class locations (addr);;-;Base class objects (class);;-;Base class names (str);;-;Base class ids (int)",
    "answer": "Base class objects (class)",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "The following class hierarchy is given. What is the expected output of the code?",
    "code": "class A:\n    def a(self):\n        print('A', end='')\n    def b(self):\n        self.a()\n\nclass B(A):\n    def a(self):\n        print('B', end='')\n    def do(self):\n        self.b()\n\nclass C(A):\n    def a(self):\n        print('C', end='')\n    def do(self):\n        self.b()\n\nB().do()\nC().do()",
    "options": "BB;;-;CC;;-;AA;;-;BC",
    "answer": "BC",
    "multiplea": "0",
    "category": "8",
    "exam": "1"
},
{
    "question": "A method for passing the arguments used by the following snippet is called:",
    "code": "def fun(a, b):\n    return a + b\n\nres = fun(1, 2)",
    "options": "sequential;;-;named;;-;positional;;-;keyword",
    "answer": "positional",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "If you want to access an exception object's components and store them in an object called e, you have to use the following form of exception statement:",
    "code": None,
    "options": "except Exception(e):;;-;except e=Exception:;;-;except Exception as e:;;-;such an action is not possible in Python",
    "answer": "except Exception as e:",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is true about Object-Oriented Programming in Python? (Select two answers.)",
    "code": None,
    "options": "encapsulation allows you to protect some data from uncontrolled access;;-;the arrows on a class diagram are always directed from a superclass towards its subclass;;-;inheritance is the relation between a superclass and a subclass;;-;an object is a recipe for a class",
    "answer": "encapsulation allows you to protect some data from uncontrolled access;;-;inheritance is the relation between a superclass and a subclass",
    "multiplea": "1",
    "category": "8",
    "exam": "1"
},
{
    "question": "What is the expected behavior of the following code?",
    "code": "the_string = ','.join(('alpha', 'omega'))\nthe_list = the_string.split(',')\nprint(',' in the_list)",
    "options": "It outputs False;;-;It outputs nothing;;-;It outputs True;;-;It raises an exception",
    "answer": "It outputs False",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "If you need to serve two different exceptions called Ex1 and Ex2 in one except branch, you can write:",
    "code": None,
    "options": "except Ex1 Ex2:;;-;except (Ex1, Ex2):;;-;except Ex1, Ex2:;;-;except Ex1+Ex2:",
    "answer": "except (Ex1, Ex2):",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is the expected behavior of the following code?",
    "code": "def unclear(x):\n    if x % 2 == -1:\n        return 0\n\nprint(unclear(1) + unclear(2))",
    "options": "print 0;;-;cause a runtime exception;;-;prints 3;;-;print an empty line",
    "answer": "print 0",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "Which of the following expressions evaluate to True? (Select two answers.)",
    "code": None,
    "options": "ord('0') - ord('9') == 10;;-;len('''12 34''') == 4;;-;len('***') == 2;;-;chr(ord('Z') - 1) == 'Y'",
    "answer": "len('''12 34''') == 4;;-;chr(ord('Z') - 1) == 'Y'",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "What can you deduce from the following statement? (Select two answers)",
    "code": "str = open('file.txt', 'rt')",
    "options": "str is a string read in from the file named file.txt;;-;a newline character translation will be performed during the reads;;-;if file.txt does not exist, it will be created;;-;the opened file cannot be written with the use of the str variable",
    "answer": "a newline character translation will be performed during the reads;;-;the opened file cannot be written with the use of the str variable",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is the expected behavior of the following code?",
    "code": "the_list = 'alpha;beta;gamma'.split(';')\nthe_string = ''.join(the_list)\nprint(the_string.isalpha())",
    "options": "it raises an exception;;-;it outputs True;;-;it outputs False;;-;it outputs nothing",
    "answer": "it outputs False",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is the expected behavior of the following code?",
    "code": "string = str(1/3)\ndummy = ''\nfor character in string:\n    dummy = dummy + character\nprint(dummy[-1])",
    "options": "it outputs 'None';;-;it outputs 3;;-;it raises an exception;;-;it outputs 0",
    "answer": "it raises an exception",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is the expected behavior of the following code?",
    "code": "my_list = [i for i in range(5)]\nm = [my_list[i] for i in range(4, 0, -1) if my_list[i] % 2 != 0]\nprint(m)",
    "options": "it outputs [1, 3];;-;the code is erroneous and it will not execute;;-;it outputs [3, 1];;-;it outputs [4, 2, 0]",
    "answer": "it outputs [3, 1]",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is the expected behavior of the following code?",
    "code": "m = 0\n\ndef foo(n):\n    global m\n    assert m != 0\n    try:\n        return 1/n\n    except ArithmeticError:\n        raise ValueError\n\ntry:\n    foo(0)\nexcept AssertionError:\n    m += 1\nexcept ArithmeticError:\n    m += 2\nexcept:\n    m += 3\n\nprint(m)",
    "options": "It outputs 1;;-;It outputs 2;;-;It outputs 3;;-;It raises an AssertionError",
    "answer": "It raises an AssertionError",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is the expected output of the following snippet?",
    "code": "a = 2\nif a > 0:\n    a += 1\nelse:\n    a -= 1\n\nprint(a)",
    "options": "3;;-;1;;-;2;;-;the code is erroneous",
    "answer": "3",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "Assuming that the following code has been executed successfully, select the expression which evaluates to True (Select two answers).",
    "code": "def f(x, y):\n    nom, denom = x, y\n    def g():\n        return nom / denom\n    return g\n\na = f(1, 2)\nb = f(3, 4)",
    "options": "a() == 4;;-;a is not None;;-;b() == 4;;-;a != b",
    "answer": "a is not None;;-;a != b",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "Which of the following statements are true? (Select two answers).",
    "code": None,
    "options": "open() is a function which returns an int that represents a physical file handle;;-;the second open() argument is optional;;-;instid, outstd, errstd are the names of pre-opened streams;;-;if invoking open() fails, the value None is returned",
    "answer": "the second open() argument is optional;;-;if invoking open() fails, the value None is returned",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is the expected output of the following snippet?",
    "code": "lst = [1, 2, 3, 4]\nlst = lst[-3:-2]\nlst = lst[-1]\nprint(lst)",
    "options": "2;;-;3;;-;1;;-;4",
    "answer": "2",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "A variable stored separately in every object is called:",
    "code": None,
    "options": "there are no such variables, all variables are shared among objects;;-;a class variable;;-;an object variable;;-;an instance variable",
    "answer": "an instance variable",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "Assuming that the following code has been executed successfully, select the expressions which evaluate to True (Select two answers).",
    "code": "def f(x, y):\n    nom, denom = x, y\n    def g():\n        return nom / denom\n    return g\n\na = f(1, 2)\nb = f(3, 4)",
    "options": "a is not None;;-;a != b;;-;b() == 0.75;;-;a() == 4",
    "answer": "a is not None;;-;a != b",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is the expected behavior of the following code?",
    "code": "my_list = [1, 2, 3]\n\ntry:\n    my_list[3] = my_list[2]\nexcept BaseException as error:\n    print(error)",
    "options": "it outputs list assignment index out of range;;-;the code is erroneous and it will not execute;;-;it outputs <class 'IndexError'>;;-;it outputs error",
    "answer": "it outputs list assignment index out of range",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "Assuming that the following inheritance set is in force, which of the following classes are declared properly? (Select two answers).",
    "code": "class A:\n    pass\n\nclass B(A):\n    pass\n\nclass C(A):\n    pass\n\nclass D(B):\n    pass",
    "options": "class Class_4(D, A): pass;;-;class Class_1(C, D): pass;;-;class Class_3(A, C): pass;;-;class Class_2(B, D): pass",
    "answer": "class Class_1(C, D): pass;;-;class Class_2(B, D): pass",
    "multiplea": "1",
    "category": "8",
    "exam": "1"
},
{
    "question": "What is the expected behavior of the following code?",
    "code": "s = '2A'\n\ntry:\n    n = int(s)\nexcept TypeError:\n    n = 3\nexcept LookupError:\n    n = 2\nexcept:\n    n = 1\n\nprint(n)",
    "options": "it outputs 2;;-;the code is erroneous and it will not execute;;-;it outputs 3;;-;it outputs 1",
    "answer": "it outputs 1",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is true about Python packages? (Select two answers).",
    "code": None,
    "options": "the __name__ variable content determines the way in which the module was run;;-;a package can be stored as a tree of sub-directories/sub-folders;;-;__pycache__ is the name of a built-in variable;;-;hashbang is the name of a built-in Python function",
    "answer": "the __name__ variable content determines the way in which the module was run;;-;a package can be stored as a tree of sub-directories/sub-folders",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is the expected output of the following code?",
    "code": "str = 'abcdef'\n\ndef fun(s):\n    del s[2]\n    return s\n\nprint(fun(str))",
    "options": "abcef;;-;the program will cause a runtime exception error;;-;acdef;;-;abdef",
    "answer": "the program will cause a runtime exception error",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "A Python module named pymod, py contains a function named pyfun(). Which of the following snippets will let you invoke the function? (Select two answers).",
    "code": None,
    "options": "from pymod import * Pymod.pyfun();;-;import pymod Pymod.Pyfun();;-;import pyfun from pymod Pyfun();;-;from pymod import pyfun Pyfun()",
    "answer": "import pymod Pymod.Pyfun();;-;from pymod import pyfun Pyfun()",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "You need data which can act as a simple telephone directory. You can obtain it with the following clauses (choose two relevant variants; assume that no other items have been created before).",
    "code": None,
    "options": "dir={'Mom':5551234567, 'Dad':5557654321};;-;dir={'Mom':'5551234567', 'Dad':'5557654321'};;-;dir={'Mom:5551234567, Dad:5557654321'};;-;dir={'Mom:5551234567', Dad:'5557654321'}",
    "answer": "dir={'Mom':5551234567, 'Dad':5557654321};;-;dir={'Mom':'5551234567', 'Dad':'5557654321'}",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "Which of the following invocations are valid? (Select two answers).",
    "code": None,
    "options": "sorted('python');;-;'python'.sort();;-;sort('python');;-;'python'.find('')",
    "answer": "sorted('python');;-;'python'.find('')",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is the expected behavior of the following code?",
    "code": "class Class:\n    Variable = 0\n    def __init__(self):\n        self.value = 0\n\nobject_1 = Class()\nobject_1.Variable += 1\nobject_2 = Class()\nobject_2.value += 1\nprint(object_2.Variable + object_1.value)",
    "options": "It outputs 1;;-;It outputs 0;;-;It raises an exception;;-;It outputs 2",
    "answer": "It outputs 1",
    "multiplea": "0",
    "category": "8",
    "exam": "1"
},
{
    "question": "What is the expected output of the following code if there is no file named non_existing_file inside the working directory?",
    "code": "try:\n    f = open('non_existing_file', 'r')\n    print(1, end=' ')\nexcept IOError as error:\n    print(error.errno, error, end=' ')\n    print(2, end=' ')\nelse:\n    f.close()\n    print(3, end=' ')",
    "options": "22;;-;13;;-;1 23;;-;2 23",
    "answer": "22",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "What will the value of the i variable be when the following loop finishes its execution?",
    "code": "for i in range(10):\n    pass",
    "options": "10;;-;the variable becomes unavailable;;-;11;;-;9",
    "answer": "9",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "Assuming that the math module has been successfully imported, which of the following expressions evaluate to True? (Select two answers).",
    "code": None,
    "options": "math.hypot(3, 4) == math.sqrt(25);;-;math.hypot(2, 5) == math.trunc(2.5);;-;math.hypot(2, 5) == math.floor(2.5);;-;math.ceil(2.5) == math.floor(2.5)",
    "answer": "math.hypot(3, 4) == math.sqrt(25);;-;math.hypot(2, 5) == math.trunc(2.5)",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is true about Python class constructors? (Select two answers).",
    "code": None,
    "options": "the constructor must have at least one parameter;;-;the constructor must return a value other than None;;-;the constructor is a method named __init__;;-;there can be more than one constructor in a Python class",
    "answer": "the constructor is a method named __init__;;-;there can be more than one constructor in a Python class",
    "multiplea": "1",
    "category": "8",
    "exam": "1"
},
{
    "question": "Assuming that the code below has been executed successfully, which of the following expressions evaluate to True? (Select two answers.)",
    "code": "class Class:\n    var = 1\n    def __init__(self, value):\n        self.prop = value\n\nObject = Class(2)",
    "options": "'var' in Class.__dict__;;-;'prop' in Object.__dict__;;-;len(Object.__dict__) == 1;;-;'var' in Object.__dict__",
    "answer": "'var' in Class.__dict__;;-;len(Object.__dict__) == 1",
    "multiplea": "1",
    "category": "8",
    "exam": "1"
},
{
    "question": "Which of the following expressions evaluate to True? (Select two answers).",
    "code": None,
    "options": "str(-1-1) in '0123456739'[2];;-;'phd' in 'alpha';;-;'deb' not in 'abcde'[::-1];;-;'True' not in 'False'",
    "answer": "str(-1-1) in '0123456739'[2];;-;'True' not in 'False'",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "What will be the value of the i variable when the while loop finishes its execution?",
    "code": "i = 0\nwhile i != 0:\n    i = i - 1\nelse:\n    i = i + 1",
    "options": "1;;-;0;;-;2;;-;the variable becomes unavailable",
    "answer": "1",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is the expected behavior of the following code?",
    "code": "s = '2A'\n\ntry:\n    n = int(s)\nexcept ValueError:\n    n = 2\nexcept ArithmeticError:\n    n = 1\nexcept:\n    n = 0\n\nprint(n)",
    "options": "It outputs 2;;-;It outputs 1;;-;It outputs 0;;-;It raises a ValueError",
    "answer": "It outputs 2",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "Assuming that the V variable holds an integer value of 2, which of the following operators should be used instead of OPER to make the expression equal to 1?",
    "code": "V OPER 1",
    "options": "<<;;-;>>;;-;~;;-;^",
    "answer": ">>",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "What can you do if you don't like a long package path like this one?\n`import alpha.beta.gamma.delta.epsilon.zeta`",
    "code": None,
    "options": "You can make an alias for the name using the `as` keyword;;-;Nothing, you need to use the full path;;-;You can shorten it to `import alpha.zeta`;;-;You can use the `alias` keyword to rename it",
    "answer": "You can make an alias for the name using the `as` keyword",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "An operator able to perform bitwise shifts is coded as (select two answers).",
    "code": None,
    "options": "- -;;-;++;;-;<<;;-;>>",
    "answer": "<<;;-;>>",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is the expected output of the following snippet?",
    "code": "s = 'abc'\nfor i in range(len(s)):\n    s = s[:i] + s[i].upper() + s[i+1:]\nprint(s)",
    "options": "abc;;-;ABC;;-;Abc;;-;The code will cause a runtime exception",
    "answer": "ABC",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "The following expression\n1+-2\nis:",
    "code": None,
    "options": "equal to 1;;-;invalid;;-;equal to 2;;-;equal to -1",
    "answer": "equal to -1",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "Which of the following lines of code will work flawlessly when put inside the `dup()` method to make the snippet's output equal to `[0, 1, 1]`? (Select two answers.)",
    "code": "class MyClass:\n    def __init__(self, initial):\n        self.store = [initial]\n\n    def put(self, new):\n        self.store.append(new)\n\n    def get(self):\n        return self.store\n\n    def dup(self):\n        # Insert the line of code here\n\nObject = MyClass(0)\nObject.put(1)\nObject.dup()\nprint(Object.get())",
    "options": "self.put(self.store[1]);;-;self.put(self.get()[-1]);;-;put self.store[1];;-;self.put(store[1])",
    "answer": "self.put(self.store[1]);;-;self.put(self.get()[-1])",
    "multiplea": "1",
    "category": "8",
    "exam": "1"
},
{
    "question": "What is the expected output of the following code?",
    "code": "def foo(x, y, z):\n    return x(y) - x(z)\n\nprint(foo(lambda x: x % 2, 2, 1))",
    "options": "1;;-;0;;-;-1;;-;An exception is raised",
    "answer": "-1",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is true about Python packages? (Select two answers.)",
    "code": None,
    "options": "The `sys.path` variable is a list of strings;;-;`__pycache__` is a folder that stores compiled Python modules;;-;A package's contents can be stored and distributed as an mp3 file;;-;Code designed to initialize a package's state should be placed inside a file named `init.py`",
    "answer": "The `sys.path` variable is a list of strings;;-;`__pycache__` is a folder that stores compiled Python modules",
    "multiplea": "1",
    "category": "1",
    "exam": "1"
},
{
    "question": "What is the expected output of the following code?",
    "code": "def foo(x, y):\n    return y(x) + (x + 1)\n\nprint(foo(1, lambda x: x * x))",
    "options": "3;;-;5;;-;4;;-;an exception is raised",
    "answer": "5",
    "multiplea": "0",
    "category": "1",
    "exam": "1"
}
]

# Connect to the PostgreSQL database
conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
cursor = conn.cursor()

# Drop the questions table if it exists
cursor.execute("DROP TABLE IF EXISTS questions")

# Create the questions table with the new 'exam' column
cursor.execute("""
CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    question TEXT,
    code TEXT,
    options TEXT,
    answer TEXT,
    multiplea BOOLEAN,
    category INTEGER,
    exam INTEGER
)
""")

# Insert questions into the database
for q in questions:
    cursor.execute("""
    INSERT INTO questions (question, code, options, answer, multiplea, category, exam)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (q['question'], q.get('code'), q['options'], q['answer'], q['multiplea'], q['category'], q['exam']))

# Commit the transaction
conn.commit()

# Close the database connection
cursor.close()
conn.close()
