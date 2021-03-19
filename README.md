# Azure IOTHUB medical device simulator
### Note that this project is still in active development.

Run 'run.py' to start the simulation.\
Health parameters are listed in the params.py file.

Connection strings are read from a file called devices.txt
```
Example: main.py hightemp "<connectionstring>"
```

Possible values are
```
normal
hightemp
lowoxygen
highheartrate
```
Example output:
```
Sending hightemp message: {"temperature": 41.542316364605306,"heartbeat": 77.93984891333814,"oxygen": 90.51814520644962}
Sending normal message: {"temperature": 37.07529152404957,"heartbeat": 76.54132747139667,"oxygen": 92.66473098393087}
```