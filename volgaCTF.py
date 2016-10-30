#!/usr/bin/python3
import os
fname = "flag.enc"
f_contents = ''

def main():
	with open(fname, "rb") as fd:
		f_contents = fd.read()
	print(f_contents)
	iv = os.urandom(64)
	print( "iv is :{0}".format(iv) )


if __name__ == '__main__':
	main()