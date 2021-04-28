import zlib, base64

def compress(inputfile, outputfile):
    data = open(inputfile, 'r').read()
    data_byte = bytes(data, 'utf-8')
    data_compress = base64.b64encode(zlib.compress(data_byte))
    decode_file = data_compress.decode('utf-8')
    open(outputfile, 'w').write(decode_file)




def decompress(inputfile, outputfile):
    data = open(inputfile, 'r').read()
    data_encode = data.encode('utf-8')
    data_decompress = zlib.decompress(base64.b64decode(data_encode))
    data_decode = data_decompress.decode('utf-8')
    file = open(outputfile, 'w')
    file.write(data_decode)
    file.close()