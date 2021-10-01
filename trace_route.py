import os, time

to_ping = input("To whom you want to Ping? ")
i=0
while True:
    i = i + 1
    os.system(f'date >> /home/trace_route.txt')
    exit_status = os.system(f'ping -c1 {to_ping} >> /home/trace_route.txt')
    os.system(f'traceroute {to_ping} >> /home/trace_route.txt')
    os.system(f"echo '' >> /home/trace_route.txt")
    os.system(f"echo '' >> /home/trace_route.txt")
    print('Test Case: #' + str(i))
    if exit_status!=0:
        print('Connection Lost!')
        break
    time.sleep(1)

i = 0
while i<6:
    i = i + 1
    os.system(f'date >> /home/trace_route.txt')
    exit_status = os.system(f'ping -c1 {to_ping} >> /home/trace_route.txt')
    os.system(f'traceroute {to_ping} >> /home/trace_route.txt')
    os.system(f"echo '' >> /home/trace_route.txt")
    os.system(f"echo '' >> /home/trace_route.txt")
    print('Extra Test Case: #' + str(i))
    time.sleep(1)
