# RUN THE PROGRAM USING THE COMMAND :
# PS D:\PYTHON\UdemyPythonDeveloperCourse\PASSWORDMANAGER>    python .\PasswordManager4.py hello bye ouboibuguuig9698y0y8ighili 

# WHERE HELLO , BYE , OUBOIBUGUUIG9698Y0Y8IGHILI ARE 3 PASSWORDS 
  
# REFER THE FILE PASSWORDMANAGER3.PY TO CHECK THE REQUIRED DOCS : (OR GOOGLING THINGS : )

# GOOGLE : https://docs.python.org/3/library/hashlib.html?highlight=hexdigest
import requests #( it is to have a fake browser , without the actual browser)
import hashlib # built in as in uses for HASHING ALGORITHMS , EX  for SHA1 GENERATOR , SHA256 , MD5 ETC ... 

import sys # CUZ WE WANT TO RECIEVE THE PARAMETER FROM THE COMMMAND LINE 
def request_api_data(query_char) : # query_char is the hashed version of the password 
    url='https://api.pwnedpasswords.com/range/' + query_char # cuz the api WORKS WITH HASH FUNCTION CONCEPT (SHA1 Hash Generator)

    res=requests.get(url)
    # we want status of the o/p too be safe : <Response [200]>
    if res.status_code !=200 :
        raise RuntimeError(f"Error Fetching : {res.status_code} , check the API and try again ")
        # o/p is error : RuntimeError: Error Fetching : 400 , check the API and try again 
    
    return res
    ...


# INSTEAD OF READ PASSWORD I WANT TO WRITE THE PASSWORD NOW : WE SUE DIFFERENT FUNCTION():
# GET_PASSWORD_LEAKS_COUNT() : to count THE NOR OF TIMES , HACKED     

def get_password_leaks_count(hashes , hash_to_check): # has =1st 5 character , then hash_to_check = next last characters 
    # we can use tuple comprehension 
    '''
    hashes=(line.split(':') for line in hashes.text) # use print(hashes) to o/p :
    #<generator object get_password_leaks_count.<locals>.<genexpr> at 0x00000192E6DA4E40>
    #print(hashes)
    
    
    # it will create a list of each item separately 
    for h in hashes : # remove count and check to remove the error :
        #print(h , count ) # ValueError: not enough values to unpack (expected 2, got 1)
        print(h)
    
    '''
    
    # so use splitLines()  : to use both h and count 
    hashes=(line.split(':') for line in hashes.text.splitlines()) # use print(hashes) to o/p :
    #<generator object get_password_leaks_count.<locals>.<genexpr> at 0x00000192E6DA4E40>
    #print(hashes)
     # it will create a list of each item separately 
    
    for h ,count in hashes : # remove count and check to remove the error : (h=hash)
        #print(h , count ) # ValueError: not enough values to unpack (expected 2, got 1)
        
        if h==hash_to_check:
            return count # HOW MANY TIMES THE PASSWORD , HAS BEEN LEAKED

    return 0 # this return should be ouside for loop , cuz or else if loop fails , then we always return 0 (PROPER PASSWORD)
 
    
def pwned_api_data(password): # password is actually password123 here  
    # check if password exists in API RESPONSE NOW ? From above function 
    #print(password.encode("utf-8")) # it prints ,  b'123'
    
    # CHECK THE CODE WITHOUT ENCODE("UTF-8") : TypeError: Strings must be encoded before hashing
    
    #print(hashlib.sha1(password.encode("utf-8")).hexdigest().upper()) # it prints , <sha1 _hashlib.HASH object @ 0x00000279A99866F0> ,
    
    # after hexdigest() , 40bd001563085fc35165329ea1ff5c5ecbdbbeef , after upper(): 40BD001563085FC35165329EA1FF5C5ECBDBBEEF
    
    sha1password=hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    
    # remember we need only 1st 5 characters of the password (first5_char): cuz we need to store the remaining one in 2nd varibale tail
    
    first5_char , tail = sha1password[:5] , sha1password[5:] # to divide in to 5 characters 
    
    response=request_api_data(first5_char)
    
    print(first5_char , tail) # to check what is going on , 40BD0   01563085FC35165329EA1FF5C5ECBDBBEEF
    print(response) # it is PROPER : <Response [200]>
    return get_password_leaks_count(response , tail ) # check waht that response is 
    #return sha1password to check what is doing 
    
        
    
#request_api_data('123') call the function , cuz 123 is a string (it can be letters also : OTHERWISE TYPEERROR : )
pwned_api_data("123") # call the function to check what is encoding-utf8 above 

def main(args): # THIS FUNCTION ACCEPTS INPUT FROM THE COMMAND LINE
    for password in args : #cuz we give multiple passwords from command prompt
        # we will recieve the COUNT from GET_PASSWORD_LEAKS_COUNT()
        count=pwned_api_data(password)
        
        if count : # IF YOUR PASSWORD IS ALSO PRESENT (OLD PASSWORD , ALREADY EXISTED AND HACKED )
            print(f"{password} was found {count} times... you should probably change your password!")
        
        else : # if your password is unique 
            print(f" {password} was not Found , Carry on ! ")
            
    return 'done!'
    ...
    
main(sys.argv[1:]) # TO ACCEPT ANY NUMBER OF ARGUEMENTS FORM TERMINAL (ALL THE PASSWORDS )     