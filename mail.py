import re
while True:
    g_mail = input("Enter your E-mail: ")
    if not g_mail:
        break
    def srch():
        pat = r"@(.)*\." # (.) mean any character, * Zero or more time of the expression,
        if re.search(pat, g_mail):
            print("Found")
        else:
            print("Incorrect gmail address")
    srch()
