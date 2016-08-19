import myos

print(myos.listdir('./'))

print('Process (%s) start...' % myos.getpid())
# Only works on Unix/Linux/Mac:
pid = myos.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (myos.getpid(), myos.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (myos.getpid(), pid))
