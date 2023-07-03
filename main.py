import os
import openai
openai.organization = "org-2IJ8iShyCp0Qn6PFM7pI3shY"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()