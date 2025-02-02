# Sleep Command

Suppose you want to pause the execution of a command for a specific period of time. In that case, you can use the **sleep** command. The syntax of the command is as follows:

```bash
sleep [NUMBER[SUFFIX]]
```

Here, **NUMBER** is the amount of time you want to pause the execution, and **SUFFIX** is the unit of time. You can use **s** for seconds, **m** for minutes, **h** for hours, and **d** for days.

For example, if you want to pause the execution for 5 seconds, you can use the following command:

```bash
sleep 5s
```

To complete this lab, you need to have a basic understanding of Bash commands and how to create and run Bash scripts. You also need to have access to a Linux or Unix operating system.

To use the **sleep** command, you can create a Bash script and add the following code:

```bash
#!/bin/bash

echo "Wait for 5 seconds"
sleep 5
echo "Completed"
```

This script will display the message "Wait for 5 seconds," pause the execution for 5 seconds, and then display the message "Completed."

To run the script, save it with the name **sleep_example.sh** and run the following command:

```bash
bash sleep_example.sh
```
