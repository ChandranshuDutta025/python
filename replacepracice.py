letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
name = (input("enter your name "))
print(letter.replace("<|Name|>",name).replace("<|Date|>","23/2/24"))