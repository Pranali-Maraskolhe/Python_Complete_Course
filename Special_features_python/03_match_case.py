def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Sever Error"
        case _:
            return "Unknown status"
        

print(http_status(501))