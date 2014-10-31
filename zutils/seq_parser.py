def readFasta (filename, lengthOnly = False, listOutput = False):
	if listOutput == False and lengthOnly == False:
		seq_len = {}
		with open(filename, 'r') as fasfile:
			for line in fasfile:
				if line[0] == '>':
					name = line[1:].strip().split('\t')[0].split(' ')[0]
					seq_len[name] = []
				else :
					seq_len[name].append(line.strip())
		return {n:''.join(s) for n,s in seq_len.iteritems()}
	elif listOutput == False and lengthOnly == True:
		seq_len = {}
		with open(filename, 'r') as fasfile:
			for line in fasfile:
				if line[0] == '>':
					name = line[1:].strip().split('\t')[0].split(' ')[0]
					seq_len[name] = 0
				else :
					seq_len[name] += len(line.strip())
		return seq_len
	if listOutput == True and lengthOnly == False:
		seq_len = []
		with open(filename, 'r') as fasfile:
			for line in fasfile:
				if line[0] == '>':
					name = line[1:].strip().split('\t')[0].split(' ')[0]
					seq_len.append([name, []])
				else :
					seq_len[-1][1].append(line.strip())
		return [[s[0], ''.join(s[1])] for s in seq_len]
	elif listOutput == True and lengthOnly == True:
		seq_len = []
		with open(filename, 'r') as fasfile:
			for line in fasfile:
				if line[0] == '>':
					name = line[1:].strip().split('\t')[0].split(' ')[0]
					seq_len.append([name, 0])
				else :
					seq_len[-1][1] += len(line.strip())