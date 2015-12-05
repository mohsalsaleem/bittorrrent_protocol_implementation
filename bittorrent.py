import bencode

# value = bencode.debencodedict("d8:announce35:udp://tracker.openbittorrent.com:8013:creation datei1327049827e6:lengthi20e4:name10:sample.txt12:piece lengthi65536e6:pieces20:asdfghjklpoiuytrewqae")
value = bencode.debencodedict("d4:spamd4:spamd4:spami+23eeee")
print value