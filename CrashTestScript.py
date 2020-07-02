import os.path
import re

i = 1
design = (r'C:\Users\alexey\Desktop\issue18\PCB\Route_Sketch.pcb') # designs' path directly to pcb file
crash_dump = re.compile(r'\bExpeditionPCB[.]\bexe[.]\d{4}[.]\bdmp$') # pattern to search
crash_dump_dir=(r'D:\FULLDUMPS') # crash dump directory

'''
for roots, dirs, files in os.walk(crash_dump_dir):
    for file in files:
        #print(file)
        matches = crash_dump.search(file)
        if matches:
            print(matches)
'''
while 1 == 1:
    print("Run Number: {0}.".format(i))
    os.system(design)
    for roots, dirs, files in os.walk(crash_dump_dir):
        for file in files:
            matches = crash_dump.search(file)
            if matches:
                print("Crash On Run: {0}".format(i))
                # end = timeit.default_timer()
                # print("Duration Of Testrun (in seconds):", end - start)
                break
            else:
                print("Successfully Finished Run: {0}".format(i))
                i += 1