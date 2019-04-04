import random, sys, os, rabinMiller, Cryptomath

def generateKey(size):
    p = rabinMiller.generateLargePrime(size)
    q = rabinMiller.generateLargePrime(size)
    n = p*q

    while True:
        e = random.randrange(2**(size-1), 2** (size))
        if Cryptomath.gcd(e, (p-1)*(q-1)) == 1:
            break

    d = Cryptomath.findModInverse(e, (p-1) * (q-1))
    publickey = (n,e)
    privatekey = (n,d)

    print('Public Key:',publickey)
    print('Private Key', privatekey)

    return (publickey,privatekey)

def makeKeyToFile(name, size):
    if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
        sys.exit(
            'WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete these files and re-run this program.' % (
            name, name))

    publickey, privatekey = generateKey(size)
    print()
    print('The public key is a %s and a %s digit number.' % (len(str(publickey[0])), len(str(publickey[1]))))
    print('Writing public key to file %s_pubkey.txt...' % (name))
    fo = open('%s_pubkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (size, publickey[0], publickey[1]))
    fo.close()
    print()
    print('The private key is a %s and a %s digit number.' % (len(str(privatekey[0])), len(str(privatekey[1]))))
    print('Writing private key to file %s_privkey.txt...' % (name))
    fo = open('%s_privkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (size, privatekey[0], privatekey[1]))
    fo.close()

def main():
    print('Keyfile is being created')
    makeKeyToFile(sys.argv[1], 1024)
    print ('Keys pair file was made')

if __name__ == '__main__':
    main()