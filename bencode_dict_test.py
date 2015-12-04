import bencode

value = bencode.debencodedict("de")
print value

value = bencode.debencodedict("d9:publisher3:bob17:publisher-webpage15:www.example.come")
print value