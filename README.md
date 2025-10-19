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

key = Key()

t = Key.encrypt('test123')

# Get Original String
t.decrypt()

# Get Raw Token String
t.token

```