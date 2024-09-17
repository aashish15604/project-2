import hashlib

# Dictionary to store URL mappings
url_mapping = {}

def generate_short_url(long_url):
    """Generate a short URL for the given long URL."""
    # Create a unique hash for the URL
    url_hash = hashlib.md5(long_url.encode()).hexdigest()[:6]  # Use the first 6 characters of the MD5 hash
    short_url = f"http://short.url/{url_hash}"
    
    # Store the mapping in the dictionary
    url_mapping[short_url] = long_url
    return short_url

def get_long_url(short_url):
    """Retrieve the long URL from the short URL."""
    return url_mapping.get(short_url, "URL not found")

def main():
    print("URL Shortener")
    print("1. Shorten a URL")
    print("2. Retrieve a long URL")
    print("3. Exit")
    
    while True:
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            long_url = input("Enter the long URL to shorten: ")
            short_url = generate_short_url(long_url)
            print(f"Shortened URL: {short_url}")
        
        elif choice == '2':
            short_url = input("Enter the short URL to retrieve: ")
            long_url = get_long_url(short_url)
            print(f"Long URL: {long_url}")
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
