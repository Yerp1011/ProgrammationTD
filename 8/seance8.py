### TD 8

import struct








def extract(file_name):
    file = open(file_name, "rb")           # "rb" = read bytes

    data = file.read()

    header = {}

    #RIFF
    header['RIFF'] = data[:3]
    #print("".join(struct.unpack_from("cccc", data, 0))
    # File size
    header['file_size'] = struct.unpack_from("I", data, 4)[0]
    # WAVE
    header['WAVE'] = data[8:11]
    #fmt
    header['fmt'] = data[12:15]
    # format_lenght
    header['format_length'] = struct.unpack_from("I", data, 16)[0]
    # format_type
    header['format_type'] = struct.unpack_from("I", data, 10)[0]
    #channel_number
    header['channel_number'] = struct.unpack_from("H", data, 22)[0]

    # sample_rate
    header['sample_rate'] = struct.unpack_from("I", data, 24)[0]

    # SBC
    header['SBC'] = struct.unpack_from("I", data, 28)[0]
    #bit_per_sample
    header['bit_per_sample'] = struct.unpack_from("H", data, 34)[0]
    # sample_data
    header['sample_data'] = data[36:40]
    #sample_size
    header['sample_size'] = struct.unpack_from("I", data, 40)[0]




    sample = struct.iter_unpack("h", data[44:])



    return header, sample




def construct(header, sample, file_name):
    with open(file_name, "wb") as f:
        #f.write('')
        packed_sample = []
        for i in sample:

            packed_sample.append(struct.pack("h", i[0]))

        f.write(b'RIFF')
        f.write(struct.pack('I', 44- 8 + len(packed_sample)*4))
        f.write(b'WAVEfmt ')
        f.write(struct.pack('IHHIIHH ', 16, 1, 2, 44100, 176400, 4, 16))
        f.write(b'data')
        f.write(struct.pack('I', len(packed_sample)*4))
        for i in range (len(packed_sample)):
            f.write(packed_sample[i])



def ex3(file_name):
    header, samples = extract(file_name)
    modified_samples = []

    criteria = 0
    for i in samples:
        criteria += 1
        if criteria % 2 == 0:
            modified_samples.append(i)
    construct(header, modified_samples, file_name[:-4] + '_ex3.wav')


if __name__ == '__main__':

    header, sample = extract("the_wall.wav")
    construct(header, sample, "the_wall_construct.wav")
    ex3("the_wall.wav")

