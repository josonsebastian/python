


traceroute = '''
Type escape sequence to abort.
Tracing the route to 192.168.1.1
  1 10.10.10.1 1 msec 0 msec 0 msec
  2 192.168.10.2 1 msec 1 msec 0 msec
  3 8.8.8.8 2 msec 1 msec 1 msec
  4 17.15.15.1 4 msec * msec * msec
'''


import json
import textfsm
with open('template') as temp:
	fsm = textfsm.TextFSM(temp)
	output = fsm.ParseText(traceroute)


print(json.dumps(fsm.header, indent=4))
print(json.dumps(output, indent=2))


