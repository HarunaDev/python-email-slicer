def app():
    # show app title
    print("Welcome to my awesome email slicer app \n")

    # get email from user
    email_input = input("Type in your email here: ")
    
    # func to check if input is valid
    def check_input(input_data):
        if "@" and "." not in input_data:
            while "@" and "." not in input_data:
                input_data = input("Type your email here: ")
    
    check_input(email_input)

    # split input data if username, domain and extension is in email
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    
    # print out split data for user to see
    output = {"username": username, "domain": domain, "extension": extension} 
    print(output)
            

app()