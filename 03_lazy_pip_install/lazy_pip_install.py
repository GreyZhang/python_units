
#!/usr/bin/python
 
import os
 
def LazyPipInstall(lib_name):
    installed_flg = False
    num = int(1)
    while installed_flg == False:
        print("the %dth time try to install %s" % (num, lib_name))
        num = int(num + 1)
        try:
            exec('import ' + lib_name)
            installed_flg = True
        except:
            os.system("pip3 install %s" % lib_name)
 
# LazyPipInstall('xlrd')
# LazyPipInstall('xlwt')
# LazyPipInstall('pandas')
# LazyPipInstall('numpy')
# LazyPipInstall('matplotlib')
LazyPipInstall('openpyxl')
