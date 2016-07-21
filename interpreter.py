import sys
import os


def interpret(filename):
	dzdw = open(filename, 'r+')
	dzdww = open("output.py", 'w')
	source=dzdw.read()
	source=source.replace("ㅇ","print(\"안녕 세계 \")\n")
	source=source.replace("ㅈ","exit(0)\n")
	dzdww.write(source)


if len(sys.argv) == 1:          
  print ("파일이름을 입력하시오.ㅇㅈ\n세계에서 가장 간단한 한글 프로그래밍 언어, ㅇㅈ.\nㅇ는 안녕 세상 출력, ㅈ는 프로그램 중지.")
  exit(1)
interpret(sys.argv[1])

