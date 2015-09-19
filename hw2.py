
### Import ###

import binascii

### Value ###

ctext = '0328ff3119ac552ea021cb3262cd'
ptext = 'Finally, the list type allows you to quickly reverse the order of the list.'

###

binctext = binascii.unhexlify(ctext)
print binctext
