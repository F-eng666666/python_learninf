import multiprocessing

global_var1 = "Global"
global_var2 = "default"

def child_process(global_var1, local_var):
    print("Child process: global_var=", global_var1,
          "local_var=", local_var,
          "global_var2=", global_var2)

if __name__ == '__main__':
    local_var = "Local"
    local_var = 'local main'
    global_var1 = 'global main'
    global_var2 = "global main 2"
    print("Parent process: global_var=", global_var1, "local_var=", local_var)

    p = multiprocessing.Process(target=child_process, args=(global_var1, local_var))
    p.start()