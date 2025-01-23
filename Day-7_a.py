def remove_fullstops(input_string):
  return input_string.replace('.', '')

input_string = input("Enter a string with fullstops: ")
result = remove_fullstops(input_string)
print(result)