import datetime


def print_log(page_name, search, author):
    print(f"""Function {page_name} called:  
        Search: {search} 
        By: {author}
        Timestamp: {datetime.datetime.utcnow()} """)

