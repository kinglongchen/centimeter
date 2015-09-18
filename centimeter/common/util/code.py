__author__ = 'chenjinlong'
def decode2unicode(str):
    return str.decode('utf-8') if not isinstance(str,unicode) else str
def encode2utf8(str):
    return str.encode('utf-8') if isinstance(str,unicode) else str