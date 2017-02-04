"""
3. If you could write an example of a GET and POST API test that validates a JSON response.
   The api call can be made up for this exercise.
"""
#GET
import urllib.request
import json
import requests

r = requests.get(url = "http://yummly.co")
print(r.json())

#POST
# modify "recipe name" and "Author name"
"""
{
      "@context": "http://schema.org/",
      "@type": "Recipe",
      "name": "Baked Garlic Sweet Potato Fries",
      "image": "https://lh6.ggpht.com/1UPZxQSvx86W1FY-7pGmrOtmYf1VzbYmlYkuQk1y4AM-9pKut_bnUEmH8oG78fDjiFE9zljdO20iU0hKHJWL2g",
      "description": "Baked Garlic Sweet Potato Fries With Sweet Potatoes, Olive Oil, Kosher Salt, Ground Black Pepper, Garlic, Grated Parmesan Cheese, Parsley Leaves",
      "author": {
        "@type": "Person",
        "name": "Damn Delicious"
      },
"""
url = "http://yummly.co"
payload = {'name': 'Roasted Chicken', 'author/name': 'Rumi Lutsch'}

r = requests.post(url, data=json.dumps(payload))
