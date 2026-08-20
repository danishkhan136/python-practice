def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "Tnternal Server Error"
        case _:
            return "Unknown status"

print(http_status(200));