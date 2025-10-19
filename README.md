QuickFernet
-

A simple wrapper for cryptography.fernet to easily encrypt and decrypt strings.

---

`pip install QuickFernet`

---

Example Usage:
-
```
from quickfernet import Key

# Declare String
string = 'hello world'

# Create New Key Object
key = Key()

# Create New Token Object for String
t = key.encrypt(string)

# Get Original String
t.decrypt()

# Get Raw Token String
t.token

```