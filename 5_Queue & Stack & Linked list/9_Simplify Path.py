""" 
Given an absolute Unix-style path, convert it to its canonical simplified form.

Rules for simplification:

. means current directory and should be ignored.
.. means go to parent directory (if possible).
Multiple consecutive slashes should be treated as a single slash.
Any other token is a valid directory name.
The result must:

start with exactly one slash /
have directory names separated by one slash
not end with a trailing slash (unless the path is just /)
Input
A single line containing string path.

Constraints:

1 <= |path| <= 2 * 10^5
path starts with /
path contains English letters, digits, _, ., and /
 """
from collections import deque
parts = input().split('/')
stack = deque()

for element in parts:
    if element == "" or element == ".":
        continue
    elif element == "..":
        if stack:
            stack.pop()
    else:
        stack.append(element)
print('/'+'/'.join(stack))
