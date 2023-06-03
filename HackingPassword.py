# YOU CAN USE SOMETHNG TO CHECK WHETHER YOUR EMAIL AND PASSWORD IS BEEN HACKED , OR NOT (# DONT ENTER YOUR PASSWORD EVERYWHERE)
# GOOGLE : https://haveibeenpwned.com/Passwords
# GOOGLE : hackers use dictionary attacks , means
# GOOGLE : brute force attack (HACKING METHOD )

# GOOGLE : https://passwordsgenerator.net/sha1-hash-generator/ (AND ENTER THE PASSWORD , CHECK THAT BELOW HASHING FUNCTION)
# WE HAVE MANY HASHING ALGORITHMS : MD5 SHA256 , SHA512 ,( BUT WE USE SHA1 ) , U CAN CLICK ANYONE - TO GENERATE THINGS 
# cUZ OVER THE WIRE , WE DONT WANT TO SEND THE ORIGINAL PASSWORD , INSTEAD W SEND THAT HASHED PASSWORD(TO API)
# BUT STILL ANYONE CAN COME AND TRY..TRY AGAIN . AND COME TILL PASSWORD_123(ORIGINAL PASSWORD ???? ) , HENCE HASH IT (AND GET HASHED PASSWORD FOR HACKING)
# SO EVERY BIG COMPANIES LIKE NETFKIX , MICROSOFT , GOOGLE  AMAZON , USES ,  K ANONYMITY TECHNIQUE (A MODERN TECHNIQUE )
# SO THAT COMPANIES CAN TRACK U , STILL DONT KNOW , WHO YOU ARE 
# SO WE CAN USE STARTING 4 OR 5 LETTERS TO CHECK THE PATTERN OF HASHED PASSWORDS 
#(EX : 4DFD0................... , HAS MANY -N- PASSWORDS)  ==> SO API CAN NEVER FIND OUR PASSWORD  


# FROM MD5 HASH GENERATOR : U CAN GENERATE MORE COMPLEX NOW :
# EX : HELLO , HASHES : EB61EEAD90E3B899C6BCBE27AC581660 , 
# (BUT IF U GIVE HELLO , ALWAYS SAME HASH FUNCTIONS ARE GENERATED NOW ,ALWAYS SAME O/P FOR HELLO ) , 
# (IF I GIVE EB61EEAD90E3B899C6BCBE27AC581660 , WE MAY OR MAYNOT GET HELLO , O/P IS NOT ABLE TO CONVERT IN TO I/P , VICE VERSA IS POSSIBLE )

# SHA-256 IS USED IN CRYPTOGRAPHY (VERY COMPLEX ==> VERY SLOW (VERY LONG)), BUT WE WANT TO O(1)  ===> VERY FAST (USE -- MD5 HASH GENERATOR ) 

# GOOGLE : MD5 hash generator is used where
# GOOGLE : SHA256 hash generator is used where
# GOOGLE : SHA512 hash generator is used where

import requests #( it is to have a fake browser , without the actual browser)

# chek this 4DFD0 , FROM THE API BELOW , (CUZ IT CHANGES EVERYTIME )
url='https://api.pwnedpasswords.com/range/' + '4DFD0' # cuz the api WORKS WITH HASH FUNCTION CONCEPT (SHA1 Hash Generator)

res=requests.get(url)
print(res) # we created a object of Response <Response [400]> (UNAUTHORISED) , SO USE 4DFD0 , NOW SAFE : <Response [200]>
'''
What is response with code 400?
The HyperText Transfer Protocol (HTTP) 400 Bad Request response status code indicates that the server cannot or will not process the request
due to something that is perceived to be a client error (for example, malformed request syntax, invalid request message framing,
or deceptive request routing).02-Mar-2023
'''