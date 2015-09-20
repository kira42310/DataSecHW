
### Import ###

import binascii

### Value ###

ctext = ['03','28','ff','31','19','ac','55','2e','a0','21','cb','32','62','cd','69','40','65','3e','44','d4','8d','22','84','21','a5','b2','d5','0a','b9','a7','41','5b','d8','fe','a9','dd','6a','57','08','d4','d8','29','61','d8','68','36','41','bc','0d','3d','91','4e','3f','11','87','71','b9','a8','77','ae','bb','28','38','f8','74','76','0b','8a','8f','bd','4d','ca','a3','4c','39']
nctext = ['11','29','f4','70','14','b0','5c','67','ee','31','83','3a','27','d5','68','5c','75','3e','51','c9','99','34','84','21','e9','ad','d3','13','ad','eb','5d','14','c4','aa','b8','df','6a','52','12','9d','cf','2a','68','81','2d','2a','40','ea','07','29','c2','5f','77','00','cf','78','f0','b4','71','e4']
ptext = 'Finally, the list type allows you to quickly reverse the order of the list.'

### start ###

nkey = []
for i in range(0,len(ctext)):
        nkey.append("{:02x}".format(int("{:02x}".format(ord(ptext[i])),16) ^ int(ctext[i],16)))

pptext = ''
for i in range(0,len(nctext)):
        pptext += "{:02x}".format(int(nctext[i],16) ^ int(nkey[i],16))

print(binascii.unhexlify(pptext))
