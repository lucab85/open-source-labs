# Using if statement with AND logic

Create a Bash script named **if_with_AND.sh** that prompts the user to enter a username and password. The script will then compare the entered values with the strings "admin" and "secret" respectively. If both values match, the output will be "valid user". Otherwise, the output will be "invalid user".

- The Bash script must be named **if_with_AND.sh**
- The script must prompt the user to enter a username and password
- The script must use the AND operator (&&) to compare the entered values with "admin" and "secret" respectively
- If both values match, the output must be "valid user"
- Otherwise, the output must be "invalid user"

```bash
#!/bin/bash

echo "Enter username"
read username
echo "Enter password"
read password

if [[ ($username == "admin" && $password == "secret") ]]; then
  echo "valid user"
else
  echo "invalid user"
fi
```
