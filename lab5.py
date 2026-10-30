"""
Lab 5 - Strings and Tuples

Objective:
1. Learn how to write a good python docstring for documenting functions'
purpose, parameters, return values. A good docstring helps other developers
understand how to use the function and serves as documentation that can be
displayed in tools like IDEs. A sample docstring has been written for exercise 1 and 2,
students need to write good docstrings for all the other exercises.
2. Review how to code simple Python functions and write unit tests using assert
3. Practice how to operate on strings and tuples (similar to lists, but strings and tuples are immutable)
4. Review iterations using loop
5. Review the boolean expression and conditionals
6. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, etc.;
   Loop (for or while) to update the variable based on requirements;
   Return the variable or a value related to this variable.
"""

"""
Exercise 1

Complete the function below to reverse a string.
Please use the accumulator algorithm instead of return s[::-1].

For example,
reverse_str("Abd") should return "dbA".
reverse_str("COMP115") should return "511PMOC".

Hint: the string concatenation using the operator '+'
"""
def reverse_str(s):
    """
    This function reverses string s.

    E.g.,
    >>> reverse_str('app')
    'ppa'
    """
    result = ""
    for ch in s:
        result = ch + result
    return result


# Write your unit tests below
assert reverse_str("Abd") == "dbA"
assert reverse_str("COMP115") == "511PMOC"
assert reverse_str("app") == "ppa"
assert reverse_str("") == ""
assert reverse_str("x") == "x"


"""
Exercise 2

Complete the function below to count how many vowels ('a', 'e', 'i', 'o', 'u') in a string.
Note that uppercase vowels are also considered vowels.

For example,
count_vowels("Apple") should return 2, since 'A' and 'e' are vowels.
count_vowels("Hmmm") should return 0, since there are no vowels.

Hint: you may want to convert the input string to its lowercase version using s.lower() first.
"""
def count_vowels(s):
    """
    This function counts the number of vowels in the string s.

    E.g.,
    >>> count_vowels("Apple")
    2
    """
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count


# Write your unit tests below
assert count_vowels("Apple") == 2
assert count_vowels("Hmmm") == 0
assert count_vowels("AEIOUaeiou") == 10
assert count_vowels("") == 0


"""
Exercise 3

Complete the following function to remove the duplicate characters in a string.

E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"

Hint: in
"""
def remove_duplicates(s):
    """
    Remove repeated characters from a string, keeping only the first
    occurrence of each character. Comparison is case-sensitive.

    Parameters:
        s (str): The input string.

    Returns:
        str: A new string with each character of s appearing once,
             in the order of first appearance.

    E.g.,
    >>> remove_duplicates("apple")
    'aple'
    >>> remove_duplicates("Popsipple")
    'Popsile'
    """
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    return result


# Write your unit tests below
assert remove_duplicates("apple") == "aple"
assert remove_duplicates("Popsipple") == "Popsile"
assert remove_duplicates("pear") == "pear"
assert remove_duplicates("") == ""
assert remove_duplicates("aaaa") == "a"


"""
Exercise 4

Complete the following function to return the lowerest index of a charactor t found in a string s,
to return -1 if the character is not in the string.

E.g.,
find_index("Abd", 'b') == 1
find_index("Abdccc", 'c') == 3
find_index("Abd", 'w') == -1

Note: we should implement our own algorithm, not using the built-in function find().
"""
def find_index(s, t):
    """
    Find the lowest index at which character t appears in string s.

    Parameters:
        s (str): The string to search in.
        t (str): The single character to search for.

    Returns:
        int: The index of the first occurrence of t in s,
             or -1 if t does not occur in s.

    E.g.,
    >>> find_index("Abdccc", 'c')
    3
    >>> find_index("Abd", 'w')
    -1
    """
    for i in range(len(s)):
        if s[i] == t:
            return i
    return -1


# Write your unit tests below
assert find_index("Abd", 'b') == 1
assert find_index("Abdccc", 'c') == 3
assert find_index("Abd", 'w') == -1
assert find_index("Abd", 'A') == 0
assert find_index("", 'a') == -1


"""
Exercise 5

Complete the following function to return the project completion day,
given the current day in a week and estimated time of days to completion.

E.g.,
project_completion_day('Monday', 4) returns 'Friday'.
project_completion_day('Monday', 7) returns 'Monday'.
project_completion_day('Saturday', 2) returns 'Monday'.
project_completion_day('Saturday', 1) returns 'Sunday'.

Hint:
days_week.index(day) will return the index of the day in the tuple days_week.

"""

days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday')
# Notice that days_week is a tuple, and it works the same if it's a list,
# since the index operation is the same for tuple and list.


def project_completion_day(day, days_to_completion):
    """
    Work out which day of the week a project will be completed on.

    Parameters:
        day (str): The current day of the week, e.g. 'Monday'.
                   Must be one of the names in days_week.
        days_to_completion (int): Number of days from today until the
                                  project is completed (>= 0).

    Returns:
        str: The name of the day of the week the project will be completed.

    E.g.,
    >>> project_completion_day('Monday', 4)
    'Friday'
    >>> project_completion_day('Saturday', 2)
    'Monday'
    """
    index = (days_week.index(day) + days_to_completion) % len(days_week)
    return days_week[index]


# Write your unit tests below
assert project_completion_day('Monday', 4) == 'Friday'
assert project_completion_day('Monday', 7) == 'Monday'
assert project_completion_day('Saturday', 2) == 'Monday'
assert project_completion_day('Saturday', 1) == 'Sunday'
assert project_completion_day('Sunday', 0) == 'Sunday'
assert project_completion_day('Wednesday', 15) == 'Thursday'


"""
Exercise 6

Write a function count_days_starting_with(c) that takes a character c
and returns the number of days in days_week whose names start with c.

Note: we've declared a tuple of days_week in line 136, which is
days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday')

E.g.,

count_days_starting_with('T') returns 2, because of 'Tuesday' and 'Thursday'.
count_days_starting_with('M') returns 1, because of 'Monday'.
count_days_starting_with('S') returns 2, because of 'Saturday' and 'Sunday'.
count_days_starting_with('X') returns 0, because of no element in days_week starts with 'X'.

"""

def count_days_starting_with(c):
    """
    Count how many days in days_week have names starting with character c.

    Parameters:
        c (str): The starting character to match (case-sensitive).

    Returns:
        int: The number of day names in days_week that start with c.

    E.g.,
    >>> count_days_starting_with('T')
    2
    >>> count_days_starting_with('X')
    0
    """
    count = 0
    for d in days_week:
        if d[0] == c:
            count += 1
    return count


# Write your unit tests below
assert count_days_starting_with('T') == 2
assert count_days_starting_with('M') == 1
assert count_days_starting_with('S') == 2
assert count_days_starting_with('X') == 0
assert count_days_starting_with('W') == 1


"""
Exercise 7

Write a function highest_score(students) that takes a list of student records and
returns the name of the student with the highest score.
Each student record contains a student's name and score, in the format (name, score).

Hints:
1. Use a loop to examine each student's record.
   You can use
   for s in students:
   to iterate through the students list. Then use s[0] to get the current element's name,
   and s[1] to get its score.

   Or, you can use
   for name, score in students:
   to iterate through the students list. Python automatically unpacks each student record
   into the two variables name and score. This works because each record contains
   exactly two values, whether the record is a tuple or a list.
2. Track the highest score and the corresponding student's name.
3. If multiple students have the same highest score, return the name of the first student with that score.

E.g., highest_score([("Alice", 85), ("Bob", 92), ("Carol", 78)]) will return "Bob"
      highest_score([("Tom", 90), ("Amy", 95), ("Sam", 88)]) will return "Amy"
      highest_score([("David", 75)]) will return "David"
"""

def highest_score(students):
    """
    Find the student with the highest score.

    Parameters:
        students (list): A non-empty list of (name, score) records,
                         where name is a str and score is a number.

    Returns:
        str: The name of the student with the highest score. If several
             students share the highest score, the first one is returned.

    E.g.,
    >>> highest_score([("Alice", 85), ("Bob", 92), ("Carol", 78)])
    'Bob'
    """
    best_name = students[0][0]
    best_score = students[0][1]
    for name, score in students:
        if score > best_score:
            best_name = name
            best_score = score
    return best_name


# Write your unit tests below
assert highest_score([("Alice", 85), ("Bob", 92), ("Carol", 78)]) == "Bob"
assert highest_score([("Tom", 90), ("Amy", 95), ("Sam", 88)]) == "Amy"
assert highest_score([("David", 75)]) == "David"
assert highest_score([("Ann", 90), ("Ben", 90), ("Cal", 80)]) == "Ann"
assert highest_score([["Zed", 10], ["Yan", 20]]) == "Yan"


"""Log Parsing Exercise (Optional Challenge)

You are given a log string containing application logs
in a standardized format. Each log entry contains
a timestamp, severity level, module name, and message.
Your task is to parse and analyze these logs.

As in log_string below, the log format - each log line follows this pattern:
YYYY-MM-DD HH:MM:SS [LEVEL] module.py Message
"""


log_string = """2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s
2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)
2024-03-05 14:32:22 [INFO] server.py Server started on port 8000
2024-03-05 14:32:45 [ERROR] database.py Connection lost to primary
2024-03-05 14:33:02 [WARNING] cache.py Redis connection unstable
2024-03-05 14:33:15 [ERROR] api.py Request handler crashed
2024-03-05 14:33:22 [INFO] database.py Attempting reconnect
"""


"""
Implement a function parse_log_line(line) to parse a single log line into its components.

Your function returns:
A tuple of 4 elements: (timestamp, level, module, message)

timestamp (str): Date and time in format "YYYY-MM-DD HH:MM:SS"
level (str): Log severity level ("ERROR", "WARNING", or "INFO")
module (str): The Python module/file name (e.g., "database.py")
message (str): The log message text

E.g.,
line = '2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s'
parse_log_line(line) == ('2024-03-05 14:32:15', 'ERROR', 'database.py', 'Connection timeout after 30s')

Hints:
1. str.split() returns a list of strings, split by default (whitespace).
"hello world python".split()
# Returns: ['hello', 'world', 'python']

2. string concatenation
'I like ' + 'you'
# Returns 'I like you'

3. str.join()
list = ['Hello,', 'world!']
' '.join(list)
# Returns 'Hello, world!'
"""

def parse_log_line(line):
    """
    Parse a single log line into its components.

    The line must follow the format:
        YYYY-MM-DD HH:MM:SS [LEVEL] module.py Message

    Parameters:
        line (str): One log line.

    Returns:
        tuple: (timestamp, level, module, message), all strings, where
               timestamp is "YYYY-MM-DD HH:MM:SS", level has its square
               brackets removed, and message is the remaining text.

    E.g.,
    >>> parse_log_line('2024-03-05 14:33:22 [INFO] database.py Attempting reconnect')
    ('2024-03-05 14:33:22', 'INFO', 'database.py', 'Attempting reconnect')
    """
    parts = line.split()
    timestamp = parts[0] + ' ' + parts[1]
    level = parts[2][1:-1]          # strip the '[' and ']'
    module = parts[3]
    message = ' '.join(parts[4:])
    return (timestamp, level, module, message)


# Write your unit tests below
line = '2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s'
assert parse_log_line(line) == ('2024-03-05 14:32:15', 'ERROR', 'database.py',
                                'Connection timeout after 30s')
assert parse_log_line('2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)') == \
    ('2024-03-05 14:32:18', 'WARNING', 'api.py', 'Slow query detected (2.3s)')
assert parse_log_line('2024-03-05 14:33:22 [INFO] database.py Attempting reconnect') == \
    ('2024-03-05 14:33:22', 'INFO', 'database.py', 'Attempting reconnect')


"""Now use your parse_log_line() to parse all the lines in the sample data log_string,
and store each tuple item in a list.
Hint: log_string.splitlines() will return a list of lines with a skip for empty lines."""

logs = []
for log_line in log_string.splitlines():
    if log_line.strip() != "":
        logs.append(parse_log_line(log_line))

assert len(logs) == 7
assert logs[2] == ('2024-03-05 14:32:22', 'INFO', 'server.py', 'Server started on port 8000')


"""Now you can use what you've learnt about accumulator algorithm to do more data analyzing.
For example, to count how many ERROR logs there."""

def count_level(logs, level):
    """
    Count how many parsed log entries have the given severity level.

    Parameters:
        logs (list): A list of (timestamp, level, module, message) tuples.
        level (str): The severity level to count, e.g. "ERROR".

    Returns:
        int: The number of entries in logs whose level equals level.

    E.g.,
    >>> count_level([('t', 'ERROR', 'a.py', 'm'), ('t', 'INFO', 'b.py', 'm')], 'ERROR')
    1
    """
    count = 0
    for timestamp, lvl, module, message in logs:
        if lvl == level:
            count += 1
    return count


def messages_from_module(logs, module):
    """
    Collect the messages logged by a particular module.

    Parameters:
        logs (list): A list of (timestamp, level, module, message) tuples.
        module (str): The module name to filter by, e.g. "database.py".

    Returns:
        list: The messages (str) from that module, in log order.
    """
    result = []
    for timestamp, level, mod, message in logs:
        if mod == module:
            result.append(message)
    return result


assert count_level(logs, 'ERROR') == 3
assert count_level(logs, 'WARNING') == 2
assert count_level(logs, 'INFO') == 2
assert count_level(logs, 'DEBUG') == 0
assert messages_from_module(logs, 'database.py') == [
    'Connection timeout after 30s',
    'Connection lost to primary',
    'Attempting reconnect',
]

print("Number of ERROR logs:", count_level(logs, 'ERROR'))
print("All tests passed!")


"""
Remember to complete the lab quiz on e-learn. That's all for this lab!
"""
