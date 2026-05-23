
#1
def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())
    
format_name("guillaume", "briez")

#2
def format_name1(f_name1, l_name1):
    formated_f_name = f_name1.title()
    formated_l_name = l_name1.title()
    print(f"{formated_f_name}, {formated_l_name}")

format_name1("gUIllaume", "bRIEz")

#3
def format_name3(f_name2, l_name2):
    formated_f_name2 = f_name2.title()
    formated_l_name2 = l_name2.title()
    return f"{formated_f_name2}, {formated_l_name2}"

formated_string = format_name3("guILLAUme", "bRIEZ")
print(formated_string)

#or

print(format_name3("guILLAUme", "bRIEZ"))


#Other usage

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)