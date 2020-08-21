import os
from win32com.client import GetObject

WMI = GetObject('winmgmts:')
processes = WMI.InstancesOf('Win32_Process')

for p in WMI.ExecQuery('select * from Win32_Process where Name="cmd.exe"'):
    print("Killing PID:", p.Properties_('ProcessId').Value)
    os.system("taskkill /pid "+str(p.Properties_('ProcessId').Value))