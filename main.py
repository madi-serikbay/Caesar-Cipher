from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar(start_text, shift_amount, cipher_direction):
  index_list = []
  for letter in start_text:
    for n in range(0, len(alphabet)):
      if letter == alphabet[n]:
        index_list.append(n)
        break
      else:
        continue
  shift_remainder = shift_amount % 26
  if cipher_direction == "encode":
    for n in range(0, len(index_list)):
      if index_list[n] + shift_remainder < 26:
        index_list[n] += shift_remainder
      elif index_list[n] + shift_remainder > 26:
        index_list[n] = index_list[n] + shift_remainder - 26

  elif cipher_direction == "decode":
    for n in range(0, len(index_list)):
      if index_list[n] - shift_remainder >= 0:
        index_list[n] -= shift_remainder
      elif index_list[n] - shift_remainder < 0:
        index_list[n] = index_list[n] + 26 - shift_remainder

  end_text = ""
  for n in index_list:
    end_text += alphabet[n]
  print(f"The {cipher_direction}d word is '{end_text}'")

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

answer = True
while answer:
  while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode' or direction == 'decode':
      break
    else:
      print(f"'{direction}' is invalid, please enter either 'encode' or 'decode'")
      continue
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)
  ans = input("If you want to restart and do it all over, please enter 'yes'. If you want to stop, enter 'no'.").lower()
  if ans == "no":
    answer = False
  