import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the SHL product catalog
url = "https://www.shl.com/solutions/products/product-catalog/"

# Send a request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Example: Adjust the selector based on the actual HTML structure
solutions = soup.find_all('tr')  # Assuming each solution is in a table row

# Extract data
data = []
for solution in solutions:
    name_tag = solution.find('a')  # Assuming the name is in an anchor tag
    remote_testing = solution.find('td', class_='remote-testing')  # Adjust class name
    adaptive_irt = solution.find('td', class_='adaptive-irt')  # Adjust class name
    test_type = solution.find('td', class_='test-type')  # Adjust class name

    name = name_tag.text.strip() if name_tag else 'N/A'
    link = name_tag['href'] if name_tag else 'N/A'
    remote = 'Yes' if remote_testing and 'green' in remote_testing['class'] else 'No'
    adaptive = 'Yes' if adaptive_irt and 'green' in adaptive_irt['class'] else 'No'
    test_type_text = test_type.text.strip() if test_type else 'N/A'

    data.append({
        'name': name,
        'link': link,
        'remote_testing': remote,
        'adaptive_irt': adaptive,
        'test_type': test_type_text
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('assessments.csv', index=False)