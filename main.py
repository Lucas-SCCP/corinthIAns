import config
import openai

openai.organization = "org-2IJ8iShyCp0Qn6PFM7pI3shY"
openai.api_key = config.OPENAI_API_KEY
response = openai.Model.list()

print(response)