import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      
    
      position = alphabet.index(char)
      new_position = position + shift_amount
      char=alphabet[new_position]
    else:
      char
    end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")
  
not_stop=True
while not_stop:
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 26:
    shift=shift%26
  else:
    shift
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  ask = input("Do you want restart chiper program? enter 'yes' or 'no'\n")  
  if ask=='no':
    not_stop=False
    print("Goodbye")