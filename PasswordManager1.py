# REFER THE FILE HACKINGPASSWORD.PY TO CHECK THE REQUIRED DOCS : (OR GOOGLING THINGS : )

# GOOGLE : https://docs.python.org/3/library/hashlib.html?highlight=hexdigest
import requests #( it is to have a fake browser , without the actual browser)
import hashlib # built in as in uses for HASHING ALGORITHMS , EX  for SHA1 GENERATOR , SHA256 , MD5 ETC ... 

def request_api_data(query_char) : # query_char is the hashed version of the password 
    url='https://api.pwnedpasswords.com/range/' + query_char # cuz the api WORKS WITH HASH FUNCTION CONCEPT (SHA1 Hash Generator)

    res=requests.get(url)
    # we want status of the o/p too be safe : <Response [200]>
    if res.status_code !=200 :
        raise RuntimeError(f"Error Fetching : {res.status_code} , check the API and try again ")
        # o/p is error : RuntimeError: Error Fetching : 400 , check the API and try again 
    
    return res
    ...
    
def pwned_api_data(password): # password is actually password123 here  
    # check if password exists in API RESPONSE NOW ? From above function 
    #print(password.encode("utf-8")) # it prints ,  b'123'
    
    # CHECK THE CODE WITHOUT ENCODE("UTF-8") : TypeError: Strings must be encoded before hashing
    
    #print(hashlib.sha1(password.encode("utf-8")).hexdigest().upper()) # it prints , <sha1 _hashlib.HASH object @ 0x00000279A99866F0> ,
    
    # after hexdigest() , 40bd001563085fc35165329ea1ff5c5ecbdbbeef , after upper(): 40BD001563085FC35165329EA1FF5C5ECBDBBEEF
    
    sha1password=hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    return sha1password
    
    
    ...    
    
#request_api_data('123') call the function , cuz 123 is a string (it can be letters also : OTHERWISE TYPEERROR : )
pwned_api_data("123") # call the function to check what is encoding-utf8 above 