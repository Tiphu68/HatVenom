#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020-2021 EntySec
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

import os
import sys
import codecs
import argparse
import codecs


class PayloadGenerator:
    pe_headers = {
        'x86': (
            b'\x4d\x5a\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xff\xff\x00\x00\xb8\x00\x00\x00\x00\x00\x00\x00'
            b'\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x0e\x1f\xba\x0e\x00\xb4\x09\xcd'
            b'\x21\xb8\x01\x4c\xcd\x21\x54\x68\x69\x73\x20\x70\x72\x6f\x67\x72\x61\x6d\x20\x63\x61\x6e\x6e\x6f'
            b'\x74\x20\x62\x65\x20\x72\x75\x6e\x20\x69\x6e\x20\x44\x4f\x53\x20\x6d\x6f\x64\x65\x2e\x0d\x0d\x0a'
            b'\x24\x00\x00\x00\x00\x00\x00\x00\x50\x45\x00\x00\x4c\x01\x02\x00\xd3\x7c\xb5\x58\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\xe0\x00\x0f\x03\x0b\x01\x02\x1b\x00\x02\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00'
            b'\x00\x10\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x40\x00\x00\x10\x00\x00\x00\x02\x00\x00'
            b'\x04\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x30\x00\x00\x00\x02\x00\x00'
            b'\x1a\x89\x00\x00\x03\x00\x00\x00\x00\x00\x20\x00\x00\x10\x00\x00\x00\x00\x10\x00\x00\x10\x00\x00'
            b'\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x00\x00\x14\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x2e\x74\x65\x78\x74\x00\x00\x00'
            b'\x63\x01\x00\x00\x00\x10\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x20\x00\x50\x60\x2e\x69\x64\x61\x74\x61\x00\x00\x14\x00\x00\x00\x00\x20\x00\x00'
            b'\x00\x02\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x00\x30\xc0'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00'
        ),
        'x64': (
            b'\x4d\x5a\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xff\xff\x00\x00\xb8\x00\x00\x00\x00\x00\x00\x00'
            b'\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x0e\x1f\xba\x0e\x00\xb4\x09\xcd'
            b'\x21\xb8\x01\x4c\xcd\x21\x54\x68\x69\x73\x20\x70\x72\x6f\x67\x72\x61\x6d\x20\x63\x61\x6e\x6e\x6f'
            b'\x74\x20\x62\x65\x20\x72\x75\x6e\x20\x69\x6e\x20\x44\x4f\x53\x20\x6d\x6f\x64\x65\x2e\x0d\x0d\x0a'
            b'\x24\x00\x00\x00\x00\x00\x00\x00\x50\x45\x00\x00\x64\x86\x02\x00\xe8\x5d\xb6\x58\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\xf0\x00\x2f\x02\x0b\x02\x02\x1b\x00\x04\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00'
            b'\x00\x10\x00\x00\x00\x10\x00\x00\x00\x00\x40\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x02\x00\x00'
            b'\x04\x00\x00\x00\x00\x00\x00\x00\x05\x00\x02\x00\x00\x00\x00\x00\x00\x30\x00\x00\x00\x02\x00\x00'
            b'\x9a\x9e\x00\x00\x03\x00\x00\x00\x00\x00\x20\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x10\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x2e\x74\x65\x78\x74\x00\x00\x00\x20\x02\x00\x00\x00\x10\x00\x00'
            b'\x00\x04\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x00\x50\x60'
            b'\x2e\x69\x64\x61\x74\x61\x00\x00\x14\x00\x00\x00\x00\x20\x00\x00\x00\x02\x00\x00\x00\x06\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x00\x30\xc0\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00'
        )
    }

    macho_templates = {
        'x64': os.path.expanduser("~/.hatvenom/templates/macho_x64.bin"),
        'aarch64': os.path.expanduser("~/.hatvenom/templates/macho_aarch64.bin")
    }

    elf_headers = {
        'armle': (
            b"\x7f\x45\x4c\x46\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            b"\x02\x00\x28\x00\x01\x00\x00\x00\x54\x80\x00\x00\x34\x00\x00\x00"
            b"\x00\x00\x00\x00\x00\x00\x00\x00\x34\x00\x20\x00\x01\x00\x00\x00"
            b"\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00"
            b"\x00\x80\x00\x00\xef\xbe\xad\xde\xef\xbe\xad\xde\x07\x00\x00\x00"
            b"\x00\x10\x00\x00"
        ),
        'mipsbe': (
            b"\x7f\x45\x4c\x46\x01\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            b"\x00\x02\x00\x08\x00\x00\x00\x01\x00\x40\x00\x54\x00\x00\x00\x34"
            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x34\x00\x20\x00\x01\x00\x00"
            b"\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x40\x00\x00"
            b"\x00\x40\x00\x00\xde\xad\xbe\xef\xde\xad\xbe\xef\x00\x00\x00\x07"
            b"\x00\x00\x10\x00"
        ),
        'mipsle': (
            b"\x7f\x45\x4c\x46\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            b"\x02\x00\x08\x00\x01\x00\x00\x00\x54\x00\x40\x00\x34\x00\x00\x00"
            b"\x00\x00\x00\x00\x00\x00\x00\x00\x34\x00\x20\x00\x01\x00\x00\x00"
            b"\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x00"
            b"\x00\x00\x40\x00\xef\xbe\xad\xde\xef\xbe\xad\xde\x07\x00\x00\x00"
            b"\x00\x10\x00\x00"
        ),
        'x86': (
            b"\x7f\x45\x4c\x46\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            b"\x02\x00\x03\x00\x01\x00\x00\x00\x54\x80\x04\x08\x34\x00\x00\x00"
            b"\x00\x00\x00\x00\x00\x00\x00\x00\x34\x00\x20\x00\x01\x00\x00\x00"
            b"\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x80\x04\x08"
            b"\x00\x80\x04\x08\xef\xbe\xad\xde\xef\xbe\xad\xde\x07\x00\x00\x00"
            b"\x00\x10\x00\x00"
        ),
        'aarch64': (
            b"\x7f\x45\x4c\x46\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            b"\x02\x00\xb7\x00\x00\x00\x00\x00\x78\x00\x00\x00\x00\x00\x00\x00"
            b"\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            b"\x00\x00\x00\x00\x40\x00\x38\x00\x01\x00\x00\x00\x00\x00\x00\x00"
            b"\x01\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            b"\xef\xbe\xad\xde\x00\x00\x00\x00\xef\xbe\xad\xde\x00\x00\x00\x00"
            b"\x00\x10\x00\x00\x00\x00\x00\x00"
        ),
        'x64': (
            b"\x7f\x45\x4c\x46\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            b"\x02\x00\x3e\x00\x01\x00\x00\x00\x78\x00\x40\x00\x00\x00\x00\x00"
            b"\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            b"\x00\x00\x00\x00\x40\x00\x38\x00\x01\x00\x00\x00\x00\x00\x00\x00"
            b"\x01\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            b"\x00\x00\x40\x00\x00\x00\x00\x00\x00\x00\x40\x00\x00\x00\x00\x00"
            b"\x41\x41\x41\x41\x41\x41\x41\x41\x42\x42\x42\x42\x42\x42\x42\x42"
            b"\x00\x10\x00\x00\x00\x00\x00\x00"
        )
    }

    @staticmethod
    def ip_to_bytes(host):
        result = b""
        for i in host.split("."):
            result += bytes([int(i)])
        return result

    @staticmethod
    def port_to_bytes(port):
        result = "%.4x" % int(port)
        return bytes.fromhex(result)

    @staticmethod
    def string_to_bytes(string):
        string = string.encode().hex()
        string = '\\x' + '\\x'.join(a + b for a, b in zip(string[::2], string[1::2]))
        return codecs.escape_decode(string, 'hex')[0]

    def generate_payload(self, file_format, arch, data, offsets={}):
        if file_format in self.formats.keys():
            for offset in offsets.keys():
                if (':' + offset + ':ip:').encode() in data:
                    data = data.replace((':' + offset + ':ip:').encode(), self.ip_to_bytes(offsets[offset]))
                elif (':' + offset + ':port:').encode() in data:
                    data = data.replace((':' + offset + ':port:').encode(), self.port_to_bytes(offsets[offset]))
                elif (':' + offset + ':string:').encode() in data:
                    data = data.replace((':' + offset + ':string:').encode(), self.string_to_bytes(offsets[offset]))
                elif (':' + offset + ':').encode() in data:
                    sub = offsets[offset] if isinstance(offsets[offset], bytes) else codecs.escape_decode(offsets[offset], 'hex')[0]
                    data = data.replace((':' + offset + ':').encode(), sub)
                else:
                    return None
            return self.formats[file_format](self, arch, data)
        return None

    def generate_pe(self, arch, data):
        if arch in self.pe_headers.keys():
            pe = self.pe_headers[arch] + data
            if arch in ['x86']:
                pe += b'\xFF' * 4 + b'\x00' * 4 + b'\xFF' * 4
                content = pe.ljust(1536, b'\x00')
            elif arch in ['x64']:
                pe += b'\x00' * 7 + b'\xFF' * 8 + b'\x00' * 8 + b'\xFF' * 8
                content = pe.ljust(2048, b'\x00')
            else:
                content = None
            return content
        return None

    def generate_elf(self, arch, data):
        if arch in self.elf_headers.keys():
            elf = self.elf_headers[arch] + data
            if elf[4] == 1:
                if arch.endswith("be"):
                    p_filesz = struct.pack(">L", len(elf))
                    p_memsz = struct.pack(">L", len(elf) + len(data))
                else:
                    p_filesz = struct.pack("<L", len(elf))
                    p_memsz = struct.pack("<L", len(elf) + len(data))
                content = elf[:0x44] + p_filesz + p_memsz + elf[0x4c:]
            elif elf[4] == 2:
                if arch.endswith("be"):
                    p_filesz = struct.pack(">Q", len(elf))
                    p_memsz = struct.pack(">Q", len(elf) + len(data))
                else:
                    p_filesz = struct.pack("<Q", len(elf))
                    p_memsz = struct.pack("<Q", len(elf) + len(data))

                content = elf[:0x60] + p_filesz + p_memsz + elf[0x70:]
            else:
                content = None
            return content
        return None

    def generate_macho(self, arch, data):
        if arch in self.macho_templates.keys():
            if os.path.exists(self.macho_templates[arch]):
                if len(data) >= len('PAYLOAD:'):
                    macho_file = open(self.macho_templates[arch], 'rb')
                    macho = macho_file.read()
                    macho_file.close()

                    payload_index = macho.index(b'PAYLOAD:')
                    content = macho[:payload_index] + data + macho[payload_index + len(data):]
                    return content
        return None

    formats = {
        'pe': generate_pe,
        'elf': generate_elf,
        'macho': generate_macho
    }


class HatVenom(PayloadGenerator):
    def ip_bytes(self, ip):
        return self.ip_to_bytes(ip)

    def port_bytes(self, port):
        return self.port_to_bytes(port)

    def string_bytes(self, string):
        return self.string_to_bytes(string)

    def generate(self, file_format, arch, shellcode, offsets={}):
        return self.generate_payload(file_format, arch, shellcode, offsets)

    def generate_to(self, file_format, arch, shellcode, offsets={}, filename='a.out'):
        with open(filename, 'wb') as f:
            f.write(self.generate_payload(file_format, arch, shellcode, offsets))


class StoreDictKeyPair(argparse.Action):
     def __call__(self, parser, namespace, values, option_string=None):
         my_dict = {}
         for kv in values.split(","):
             k,v = kv.split("=")
             my_dict[k] = v
         setattr(namespace, self.dest, my_dict)


class HatVenomCLI(PayloadGenerator):
    description = "Powerful payload generation and shellcode injection tool that provides support for common platforms and architectures."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--format', dest='format', help='Platform to generate for.')
    parser.add_argument('--arch', dest='arch', help='Architecture to generate for.')
    parser.add_argument('--shellcode', dest='shellcode', help='Shellcode to inject.')
    parser.add_argument('--offsets', dest='offsets', help='Shellcode offsets.', action=StoreDictKeyPair)
    parser.add_argument('-o', '--output', dest='output', help='File to output generated payload.')
    parser.add_argument('-l', '--list', action="store_true", help='List all formats and platforms.')
    args = parser.parse_args()

    def start(self):
        if self.args.list:
            formats = ""
            print(formats)
            sys.exit(0)

        if self.args.format and self.args.arch and self.args.shellcode:
            offsets = dict() if not self.args.offsets else self.args.offsets

            filename = self.args.output if self.args.output else 'a.out'
            shellcode = codecs.escape_decode(self.args.shellcode, 'hex')[0]

            print(f"[i] Target format: {self.args.format}")
            print(f"[i] Target architecture: {self.args.arch}")

            print("[*] Generating payload...")
            payload = self.generate_payload(self.args.format, self.args.arch, shellcode, offsets)

            if payload is None:
                print(f"[-] Invalid format or architecture specified!")
                sys.exit(1)

            print(f"[i] Final payload size: {str(len(payload))}")
            print(f"[*] Saving payload to {filename}...")
            with open(filename, 'wb') as f:
                f.write(payload)
            print(f"[+] Payload saved to {filename}!")
            sys.exit(0)
        else:
            print("[-] No format, architecture and shellcode specified!")

        print("[-] Failed to generate payload!")
        sys.exit(1)