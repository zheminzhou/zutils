ascii_numbers = [chr(num) for num in range(48,58)]

def map_parser (item6, filter = None) :
	mlen = 0
	fragments = []
	for c in item6:
		if c in ascii_numbers:
			mlen = mlen*10 + ord(c)-48
		else :
			if filter == None or c in filter:
				fragments.append([mlen, c])
	return fragments
def ref_map_parser (item6) :
	return map_fragment(item6, ('M', 'D'))

def qry_map_parser (item6) :
	return map_fragment(item6, ('M', 'I'))

def map_len (item6, filter = None) :
	mlen = 0
	length = 0
	for c in item6:
		if c in ascii_numbers:
			mlen = mlen*10 + ord(c)-48
		else :
			if filter == None or c in filter:
				length += mlen
			mlen = 0
	return length

def ref_map_len (item6) :
	return map_len(item6, ('M', 'D'))

def qry_map_len (item6) :
	return map_len(item6, ('M', 'I'))

def read_orientation (item2, returnValue = None) :
	if returnValue == None:
		return -1 if (int(item2) & 0x10) > 0 else 1
	else :
		return returnValue[1] if (int(item2) & 0x10) > 0 else returnValue[1]

def tag_parser (read, filter = None) :
	if isinstance(read, str) :
		items = read.strip().split('\t')
	else :
		items = read
	tags = {}
	if filter == None:
		for i in range(11, len(items)):
			tags[items[i][:2]] = items[i][5:]
	else :
		for i in range(11, len(items)):
			if items[i][:2] in filter:
				tags[items[i][:2]] = items[i][5:]
	return tags

def iterPairReader (file, split = True) :
	reads = {}
	with open(file,'r') as fileHandler:
		if split == False:
			for line in fileHandler:
				if line[0] == '@' : continue
				item = line.strip().split('\t')
				if item[0] in reads:
					yield [reads.pop(item[0]), line]
				else :
					reads[item[0]] = line
		else :
			for line in fileHandler:
				if line[0] == '@' : continue
				item = line.strip().split('\t')
				if item[0] in reads:
					yield [reads.pop(item[0]), item]
				else :
					reads[item[0]] = item		

if __name__ == '__main__':
	import sys
	for t in iterPairReader(sys.argv[1]):
		x = map_len(t[0][5])
		print x