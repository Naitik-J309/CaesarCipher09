# ASCII Art Banner
print(''' 
  .oooooo.                                                  
 d8P'  `Y8b                                                 
888           .oooo.    .ooooo.   .oooo.o  .oooo.   oooo d8b
888          `P  )88b  d88' `88b d88(  "8 `P  )88b  `888""8P
888           .oP"888  888ooo888 `"Y88b.   .oP"888   888    
`88b    ooo  d8(  888  888    .o o.  )88b d8(  888   888    
 `Y8bood8P'  `Y888""8o `Y8bod8P' 8""888P' `Y888""8o d888b   

  .oooooo.    o8o             oooo                          
 d8P'  `Y8b   `"'             `888                          
888          oooo  oo.ooooo.   888 .oo.    .ooooo.  oooo d8b
888          `888   888' `88b  888P"Y88b  d88' `88b `888""8P
888           888   888   888  888   888  888ooo888  888    
`88b    ooo   888   888   888  888   888  888    .o  888    
 `Y8bood8P'  o888o  888bod8P' o888o o888o `Y8bod8P' d888b   
                    888                                     
                   o888o                                   
''')

# Main loop to repeatedly prompt user until they type "quit"
function = ""
while function != "quit":
    # Get user intent: encode, decode, or quit
    function = input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'quit' to stop the application: ").lower()
    
    # Exit if user chooses to quit
    if function == "quit":
        exit()
    
    # Validate function input
    while function not in ['encode', 'decode']:
        function = input("Please type 'encode' to encrypt, type 'decode' to decrypt, please be precise: ").lower()
    
    # Ask whether to include numbers/special characters or not
    type = input("Do you want to change the numbers, y for yes and n for no: ").lower()
    
    # Get the message and shift amount from the user
    message = input("Type your message: ")
    shift = int(input("Type the shift number: "))

    # Cipher for only alphabetic characters (leave digits/punctuation unchanged)
    def cipherno(message, shift):
        new_mesg = ""
        # Normalize shift within ASCII printable range (95 characters from 32 to 126)
        if shift < 0:
            shift = -((-shift) % 95)
        else:
            shift = shift % 95

        for i in message:
            if i.isalpha():
                ascii_val = ord(i)
                new_val = ascii_val + shift
                # Wrap around if character exceeds printable ASCII
                if new_val > 126:
                    new_val = (new_val - 127) + 32
                elif new_val < 32:
                    new_val = 127 - (32 - new_val)
                new_mesg += chr(new_val)
            else:
                # Non-alphabet characters stay the same
                new_mesg += i
        return new_mesg

    # Cipher for all characters in ASCII printable range (including digits/symbols)
    def cipher(message, shift):
        new_mesg = ""
        if shift < 0:
            shift = -((-shift) % 95)
        else:
            shift = shift % 95

        for i in message:
            ascii_val = ord(i)
            new_val = ascii_val + shift
            if new_val > 126:
                new_val = (new_val - 127) + 32
            elif new_val < 32:
                new_val = 127 - (32 - new_val)
            new_mesg += chr(new_val)
        return new_mesg

    # Execute encoding or decoding based on user input
    if type == "y":
        # Numbers and symbols included
        if function == "encode":
            msg = cipher(message, shift)
            print("The encoded message is:", msg)
        elif function == "decode":
            shift = -shift
            msg = cipher(message, shift)
            print("The decoded message is:", msg)
    elif type == "n":
        # Numbers and symbols untouched
        if function == "encode":
            msg = cipherno(message, shift)
            print("The encoded message is:", msg)
        elif function == "decode":
            shift = -shift
            msg = cipherno(message, shift)
            print("The decoded message is:", msg)