import struct

f = open("train-images.idx3-ubyte", "rb")
h = open("train-labels.idx1-ubyte", "rb")
g = open("bernoulli_train", "w")

f.seek(0)
magic_number = f.read(4)
magic_number = struct.unpack('>i', magic_number)
magic_number = h.read(4)
magic_number = struct.unpack('>i', magic_number)
#print 'Magic Number:' + str(magic_number[0])
data_type = f.read(4)
data_type = struct.unpack('>i', data_type)
data_type = h.read(4)
data_type = struct.unpack('>i', data_type)
#print 'Number of Images:' + str(data_type[0])
dim = f.read(8)
dimr = struct.unpack('>i', dim[0:4])
dimr = dimr[0]
#print 'Number of Rows:' + str(dimr)
dimc = struct.unpack('>i', dim[4:])
dimc = dimc[0]
#print 'Number of Columns: ' + str(dimc)

for i in range(int(data_type[0])):
    feature_array = []
    for j in range(dimr * dimc):
        feature = f.read(1)
        feature = struct.unpack('>B', feature)
        if feature[0] < 10:
            feature = 0
        else:
            feature = 1
        feature_array.append(str(feature))
    label = h.read(1)
    label = struct.unpack('>B', label)
    g.write(str(label[0]) + '\t' + ' '.join(feature_array) + '\n')

f.close()
h.close()
g.close()

f = open("t10k-images.idx3-ubyte", "rb")
h = open("t10k-labels.idx1-ubyte", "rb")
g = open("bernoulli_test", "w")

f.seek(0)
magic_number = f.read(4)
magic_number = struct.unpack('>i', magic_number)
magic_number = h.read(4)
magic_number = struct.unpack('>i', magic_number)
#print 'Magic Number:' + str(magic_number[0])
data_type = f.read(4)
data_type = struct.unpack('>i', data_type)
data_type = h.read(4)
data_type = struct.unpack('>i', data_type)
#print 'Number of Images:' + str(data_type[0])
dim = f.read(8)
dimr = struct.unpack('>i', dim[0:4])
dimr = dimr[0]
#print 'Number of Rows:' + str(dimr)
dimc = struct.unpack('>i', dim[4:])
dimc = dimc[0]
#print 'Number of Columns: ' + str(dimc)

for i in range(int(data_type[0])):
    feature_array = []
    for j in range(dimr * dimc):
        feature = f.read(1)
        feature = struct.unpack('>B', feature)
        if feature[0] < 10:
            feature = 0
        else:
            feature = 1
        feature_array.append(str(feature))
    label = h.read(1)
    label = struct.unpack('>B', label)
    g.write(str(label[0]) + '\t' + ' '.join(feature_array) + '\n')

f.close()
h.close()
g.close()
