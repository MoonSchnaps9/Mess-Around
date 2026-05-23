def format_name3(f_name2, l_name2):
    #Here:
    """Take a first and last name and format it to 
    return the title case version of the name."""
    #-----
    if f_name2 == "" or l_name2 == "":
        return "You did not provide any valid inputs"
    formated_f_name2 = f_name2.title()
    formated_l_name2 = l_name2.title()
    return f"{formated_f_name2}, {formated_l_name2}"

print(format_name3(input("What is your first name?"),input("What is your last name?")))