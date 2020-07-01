
https://stackoverflow.com/questions/48577398/how-to-make-http-post-request-with-pywin32-pypiwin32
#  pypiwin32 - nazov balicka 
# automaticke HTTP GET vo Windows cez proxy v domene
# https://github.com/mhammond/pywin32/
# pywin32 pypiwin32 moduly ....

# ale ci aj funguje ???
 
import pythoncom
import win32com.client

pythoncom.CoInitialize()

url = "https://google.com"

h = win32com.client.Dispatch('WinHTTP.WinHTTPRequest.5.1')
h.SetAutoLogonPolicy(0) # log in automatically
h.Open('GET', url, True)
h.Send()

# este otestovat
# --- end ---

