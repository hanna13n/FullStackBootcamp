import struct
import sys


def amplify(ipfile, opfile, amplification):
    i = open(ipfile, "rb")
    o = open(opfile, "wb")

    header = i.read(44)
    o.write(header)

    sample = i.read(2)

    while sample:
        if sample:
            ip_data = struct.unpack('h', sample)
            val = ip_data[0]
            val *= amplification
            val = int(val)
            op_data = struct.pack('h', val)
            o.write(op_data)

        sample = i.read(2)

    i.close
    o.close


def main():
    source = sys.argv[1]
    target = sys.argv[2]
    amplification = float(sys.argv[3])

    amplify(source, target, amplification)


main()
