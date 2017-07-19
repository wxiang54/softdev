from pprint import pprint

def is_valid_pass(p):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return bool([1 for c in p if c in alphabet] and [1 for c in p if c in alphabet.upper()] and [1 for c in p if c.isdigit()])

def rate_pass(p):
    if p == "password":
        raise ValueError("CHANGE YOUR PASSWORD !!!")
    
    # Using guidelines set forth by passwordmeter.com
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    numbers = "01234567890"
    symbols = ")!@#$%^&*()" + ".?,;:-_<>|~"
    minPassLength = 8
    criteria = {}
    
    # Addition 1: num_chars * 4
    n = len(p)
    criteria["addition1"] = n*4
    
    # Addition 2: (len - num_uppercase) * 2
    # * unless entire string is uppercase
    n = len( [1 for c in p if c in alphabet.upper()] )
    criteria["addition2"] = (len(p)-n)*2 \
                            if n > 0 and n < len(p) \
                            else 0

    # Addition 3: (len - lowercase) * 2
    # * unless entire string is lowercase
    n = len( [1 for c in p if c in alphabet] )
    criteria["addition3"] = (len(p)-n)*2 \
                            if n>0 and n < len(p) \
                            else 0

    # Addition 4: num_digits * 4
    # * unless entire string is digits
    n = len( [1 for c in p if c in numbers] )
    criteria["addition4"] = n*4 if n < len(p) else 0
    
    # Addition 5: num_symbols * 4
    n = len( [1 for c in p if c in symbols] )
    criteria["addition5"] = n*6
    
    # Addition 6: num_middle_digitsOrSymbols * 2
    # * e.g. would award +6 for "a$5$3"
    # * for 2 symbols and 1 digit in middle
    n = len( [1 for c in p[1:-1]
              if c in numbers
              or c in symbols] )
    criteria["addition6"] = n*2
    
    # Addition 7: num_requirements
    # * unless < 4 requirements met
    n = len( [1 for i in criteria if criteria[i]] ) \
        - int( len(p) > minPassLength )
    criteria["addition7"] = n*2 if n>=4 else 0

    
    # Deduction 1: -n if letters only
    n = len( [1 for c in p \
              if c in alphabet \
              or c in alphabet.upper()] )
    criteria["deduction1"] = -n if n == len(p) else 0
    
    # Deduction 2: -n if numbers only
    n = len( [1 for c in p if c in numbers] )
    criteria["deduction2"] = -n if n == len(p) else 0

    # Deduction 3: repeat characters
    repeats = [ float(c1-c2) / len(p) \
                for c1 in xrange(len(p)) \
                for c2 in xrange(len(p)) \
                if p[c1] == p[c2] and c2 > c1 ]
    criteria["deduction3"] = sum(repeats) * 10
    
    # Deduction 4: -n*2 for consec. uppercase letters
    n = len( [1 for i in xrange(len(p)-1) \
              if p[i] in alphabet.upper() \
              and p[i+1] in alphabet.upper()] )
    criteria["deduction4"] = -n*2
    
    # Deduction 5: -n*2 consec. lowercase letters
    n = len( [1 for i in xrange(len(p)-1)
              if p[i] in alphabet
              and p[i+1] in alphabet] )
    criteria["deduction5"] = -n*2
    
    # Deduction 6: -n*2 consec. numbers
    n = len( [1 for i in xrange(len(p)-1) \
              if p[i] in numbers \
              and p[i+1] in numbers] )
    criteria["deduction6"] = -n*2
    
    # Deduction 7: -n*3 sequential letters (3+)
    n = len( [1 for i in xrange(len(p)-2) \
              if p[i:i+3].lower() in alphabet] )
    criteria["deduction7"] = -n*3
    
    # Deduction 8: -n*3 sequential numbers (3+)
    n = len( [1 for i in xrange(len(p)-2) \
              if p[i:i+3] in numbers] )
    criteria["deduction8"] = -n*3
    
    # Deduction 9: -n*3 sequential symbols (3+)
    n = len( [1 for i in xrange(len(p)-2) \
              if p[i:i+3] in symbols[:11]] )
    criteria["deduction9"] = -n*3
    

    # total the score
    score = sum( [criteria[i] for i in criteria if criteria[i]] ) / float(10)
    
    #pprint(criteria)
    return 10.0 if score > 10 else 0.0 if score < 0 else score

if __name__ == "__main__":
    while (1):
        p = raw_input("Enter a password: ")
        print rate_pass(p)
