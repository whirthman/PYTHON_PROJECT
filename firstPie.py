# Encode Method
# Encodes strings of characters 

txt = "Whirthingham Wilson"
x = txt.encode(encoding="ascii")
print(txt.encode(encoding="UTF-8", errors="strict"))
print(txt.encode(encoding="ISO-8859-1", errors="strict"))
print(txt.encode(encoding="UTF-16",errors="xmlcharrefreplace"))
print(txt.encode(encoding="UTF-32",errors="replace"))
print(txt.encode(encoding="ascii",errors="backslashreplace"))

store_encode = txt.encode(encoding="UTF-16",errors="xmlcharrefreplace")

print(store_encode.decode("UTF-16"), " : This is a decoded string")
