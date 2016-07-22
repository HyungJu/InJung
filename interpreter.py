import sys
import os
from subprocess import call
#possible commands : ㅇ ㅈ ㅊ
def interpret(filename):
	hostlang="Python" #interpreter's language
	mode="strict" #strick / unstrict (allow ENGLISH or not)
	dzdw = open(filename, 'r+')
	dzdww = open("output.py", 'w') 
	source=dzdw.read()
	if hostlang=="Python":
		source=source.replace("(","(\"")
		source=source.replace(")","\")")
		source=source.replace("ㅇ","print(\"안녕 세계 \")\n")
	if hostlang=="C":
		source=source.replace("(","(\"")
		source=source.replace(")","\")")
		source=source.replace("ㅇ","printf(\"안녕 세계 \")\n")


	source=source.replace("ㅈ","exit(0)\n")
	if mode=="unstrict":
		source=source.replace("ㅊ","print")
		#abcdefghijklmnopqrstuvwxyz
		#ㄱㄴㄷㄹㅁ01ㅊㅋㅌㅍ23456789ㄲㄸㅏㅑㅓㅕㅗ
		#see this table
		source=source.replace("ㄱ","a")
		source=source.replace("ㄴ","b")
		source=source.replace("ㄷ","c")
		source=source.replace("ㄹ","d")
		source=source.replace("ㅁ","e")
		source=source.replace("0","f")
		source=source.replace("1","g")
		source=source.replace("ㅊ","h")
		source=source.replace("ㅋ","i")
		source=source.replace("ㅌ","j")
		source=source.replace("ㅠ","k")
		source=source.replace("2","l")
		source=source.replace("3","m")
		source=source.replace("4","n")
		source=source.replace("5","o")
		source=source.replace("6","p")
		source=source.replace("7","q")
		source=source.replace("8","r")
		source=source.replace("9","s")
		source=source.replace("ㄲ","t")
		source=source.replace("ㄸ","u")
		source=source.replace("ㅏ","v")
		source=source.replace("ㅑ","w")
		source=source.replace("ㅓ","x")
		source=source.replace("ㅕ","y")
		source=source.replace("ㅗ","z")

	if mode=="strict":
		source=source.replace("ㄱ","") #removing Hanguls except ㅇㅈㅊ
		source=source.replace("ㄴ","")
		source=source.replace("ㄷ","")
		source=source.replace("ㄹ","")
		source=source.replace("ㅁ","")
		source=source.replace("ㅂ","")
		source=source.replace("ㅅ","")
		source=source.replace("ㅋ","")
		source=source.replace("ㅌ","")
		source=source.replace("ㅍ","")
		source=source.replace("ㅎ","")
	dzdww.write(source)


if len(sys.argv) == 1:          
  print ("파일이름을 입력하시오.ㅇㅈ\n세계에서 가장 간단한 한글 프로그래밍 언어, ㅇㅈ.\nㅇ는 안녕 세상 출력, ㅈ는 프로그램 중지.")
  exit(1)
interpret(sys.argv[1])

