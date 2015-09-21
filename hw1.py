
import base64

### variable ###

ba64 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', \
	'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', \
	'0','1','2','3','4','5','6','7','8','9','+','/']

### Start ###

sword = "I am a student at Kasetsart University in Bangkok. I enjoy this course very much."
seed = '01101000010'
n = len(sword)
bits = n*8
print "source word long: %d char" % n
print "source bit long: %d bits" % bits

bichar = ''
for i in sword:
	bichar += '{0:08b}'.format(ord(i))

tmp = seed
pad = ''
for i in xrange(0,bits):
	bit = str(int(tmp[0]) ^ int(tmp[2]))
	tmp = tmp[1:] + bit
	pad += bit

bencryp = ''
for i in xrange(0,bits):
	bit = str(int(bichar[i]) ^ int(pad[i]))
	bencryp += bit

b64encryp = ''
tmpenc = bencryp
for i in xrange(0,len(tmpenc)/6):
	b64encryp += ba64[int(tmpenc[:6],2)]
	tmpenc = tmpenc[6:]

print 'encryp base64: %s' % b64encryp
print 'encryp base64 length: %d' % len(b64encryp)
