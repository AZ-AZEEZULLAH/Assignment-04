# Import the requests library to make HTTP requests
import requests

# Define a function to get a random joke
def get_joke():
    # This is the API endpoint that returns a random joke
    url = "https://official-joke-api.appspot.com/random_joke"

    try:
        # Send a GET request to the joke API
        response = requests.get(url)
        
        # Raise an error if the response status is not OK (e.g., 404 or 500)
        response.raise_for_status()

        # Parse the JSON response and convert it into a Python dictionary
        data = response.json()

        # Format and return the joke using setup and punchline from the API
        return f"😂 {data['setup']} - {data['punchline']}"
    
    # Catch any exceptions that occur during the request
    except requests.exceptions.RequestException as e:
        # Return an error message with the exception details
        return f"🔕 Error Fetching Joke: {e}"

# This condition ensures the code runs only when executed directly,
# not when imported as a module in another script
if __name__ == "__main__":
    # Print the joke returned by the get_joke function
    print(get_joke())
