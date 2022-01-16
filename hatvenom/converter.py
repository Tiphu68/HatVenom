#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020-2022 EntySec
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import struct
import socket
import binascii


class Converter:
    @staticmethod
    def host_to_bytes(host, endian='little'):
        inet_aton = socket.inet_aton(host)
        inet_aton = struct.unpack('>L', inet_aton)[0]

        if endian == 'little':
            return struct.pack('<L', inet_aton)
        elif endian == 'big':
            return struct.pack('>L', inet_aton)
        else:
            return b''

    @staticmethod
    def port_to_bytes(port, endian='little'):
        htons = socket.htons(port)

        if endian == 'little':
            return struct.pack('<H', htons)
        elif endian == 'big':
            return struct.pack('>H', htons)
        else:
            return b''

    @staticmethod
    def string_to_bytes(string):
        return (b'0x' + binascii.hexlify(string.encode())).decode()