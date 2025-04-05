# Match
browser_name = input("Enter your browser name\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("Code to be executed - Firefox")
    case "chrome":
        print("Code to be executed - Chrome")
    case "edge":
        print("Code to be executed - Edge")
    case "safari":
        print("Code to be executed - Safari")
    case _:
        print("Browser Not Found!")

user_type = input("Enter the type of user - admin, manager, guest\n")
user_type = user_type.lower()
match user_type:
    case "admin" | "manager":
        print("Hello Officer")
    case "guest":
        print("Hello Guest")
    case _:
        print("Hello There!")
