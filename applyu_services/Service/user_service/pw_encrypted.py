# passwrod corresponding
crrespongding_changes= [
    
    # Number changes 
    ['0','dss'],
    ['1','eed'],
    ['2','yuw'],
    ['3','udx'],
    ['4','ius'],
    ['5','ncj'],
    ['6','ui3'],
    ['7','ol5'],
    ['8','e3d'],
    ['9','nh6'],

    # Letter changes
    ['a','j2d'],
    ['b','s5i'],
    ['c','e4w'],
    ['d','c3d'],
    ['e','d3e'],
    ['f','wq5'],
    ['g','x4v'],
    ['h','er7'],
    ['i','z8s'],
    ['g','m9k'],
    ['k','y4e'],
    ['l','t6e'],
    ['n','o7x'],
    ['m','q9g'],
    ['o','b3v'],
    ['p','u3t'],
    ['q','l7k'],
    ['r','z9f'],
    ['s','g7t'],
    ['t','t0r'],
    ['u','o5p'],
    ['v','s4x'],
    ['w','u3j'],
    ['x','leo'],
    ['y','x4t'],
    ['z','e7r'],

    # Special characters changes
    ['!','ppg'],
    ['@','yfu'],
    ['#','y4ul'],
    ['$','y7u'],
    ['%','u5l'],
    ['^','u4y'],
    ['&','l1u'],
    ['~','y6y']
]

# Password encrpt 
def encryption(password):

    encrpted = None;

    for each_character in password:
        for match_charachter in crrespongding_changes:
            if each_character == match_charachter[0]:
                if each_character.isalpha() and each_character.isupper():
                    encrpted = encrpted + match_charachter[1].upper()
                else: 
                    encrpted = encrpted + match_charachter[1]
                break     

    return encrpted
                
