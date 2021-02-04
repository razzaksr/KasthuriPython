# check whether memory are same or not: is, is not>> True/False


data=int(input("Tell us data: "))
leftdigit=int(input("Tell us swift within nibble: "))
print("actual data sender given",data)
sent=data<<leftdigit
print("encrypted data of the sender",sent)
print("-----------sender sending data to the receiver------------------")

print("-----------receiver getting data from sender--------------------")
received=sent
print("Received data is",received)
print("Whether wrong data obtained",(received is not data))
print("Performing Decryption")
rightdigit=int(input("Tell us swift within nibble: "))
received>>=rightdigit
print("Whether data obtained as it is",(received is data))
print("Whether wrong data obtained",(received is not data))




