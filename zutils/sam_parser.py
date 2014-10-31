ascii_numbers = [chr(num) for num in range(48,58)]

def ref_map_len (item6) :
	length = 0
	mlen = 0
	for c in item6:
		if c in ascii_numbers:
			mlen = mlen*10 + ord(c)-48
		else :
			if c in ('M', 'D'):
				length += mlen
			mlen = 0
	return length

def qry_map_len (item6) :
	length = 0
	mlen = 0
	for c in item6:
		if c in ascii_numbers:
			mlen = mlen*10 + ord(c)-48
		else :
			if c in ('M', 'I'):
				length += mlen
			mlen = 0
	return length

def read_orientation (item2, returnValue = None) :
	if returnValue == None:
		return -1 if (int(item2) & 0x10) > 0 else 1
	else :
		return returnValue[0] if (int(item2) & 0x10) > 0 else returnValue[1]


if __name__ == '__main__':
	import sys
	test = readFasta(sys.argv[1], listOutput=True)
	print test