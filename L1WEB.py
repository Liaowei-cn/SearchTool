##  OS(ALL)
##  VS(Python3 & PyQt5)
##  NAME(Search WEB)
##  INFO(version:1.0 date:2017.05.20)

#   >>>>>(函数库调用)
import webbrowser
import os
#   >>>>>(动态库调用)
os.rename('动态库配置.txt','set.py')
from set import*
os.rename('set.py','动态库配置.txt')
#   >>>>>(搜索函数定义)
def SearchOnline(i,keyword):
	if i == 1:
		webbrowser.open(http1+code1+keyword, new=0, autoraise=True)
	elif i == 2:
		webbrowser.open(http2+code2+keyword, new=0, autoraise=True)
	elif i == 3:
		webbrowser.open(http3+code3+keyword, new=0, autoraise=True)
	elif i == 4:
		webbrowser.open(http4+code4+keyword, new=0, autoraise=True)
	elif i == 5:
		webbrowser.open(http5+code5+keyword, new=0, autoraise=True)
	else:
		webbrowser.open(http6+code6+keyword, new=0, autoraise=True)
if __name__ == "__main__":
	i=2
	keyword="你好"
	SearchOnline(i,keyword)