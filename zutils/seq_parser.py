import sys

def readFastaFile (filename, lengthOnly = False, listOutput = False):
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
        return seq_len

def writeFastaFile (fasta, file = '', lineWidth = -1, order = None) :
    """Write a list or dict of fasta sequences into stdout or a file
              writeFastaFile (fasta, file = '', lineWidth = -1, order = None)
    """
    if file == '':
        fout = sys.stdout
    else :
        fout = open(file, 'w')

    if isinstance(fasta, dict) :
        if order == None:
            order = fasta.keys()
        if lineWidth > 0:
            for n in order:
                fout.write('>' + n + '\n')
                for k in range(0, len(fasta[n]), lineWidth):
                    fout.write(fasta[n][k:(k+lineWidth)] + '\n')
        else :
            for n in order:
                fout.write('>' + n + '\n' + fasta[n] + '\n')
    elif isinstance(fasta, list) :
        if lineWidth > 0:
            for seq in fasta:
                fout.write('>' + seq[0] + '\n')
                for k in range(0, len(seq[1]), lineWidth):
                    fout.write(seq[1][k:(k+lineWidth)] + '\n')
        else :
            for seq in fasta:
                fout.write('>' + seq[0] + '\n' + seq[1] + '\n')

if __name__ == '__main__':
    filename = sys.argv[1]
    x = readFastaFile(filename, lengthOnly=True)
    writeFastaFile(fasta, file='', lineWidth=-1, order=None)
    writeFastaFile(x, '', lineWidth = 100)