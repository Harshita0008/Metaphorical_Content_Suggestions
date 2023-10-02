import os
import openai
from metaphor_python import Metaphor

# OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Metaphor API key
metaphor = Metaphor(os.getenv("METAPHOR_API_KEY"))

# User's content recommendation query
USER_INPUT = "I'm interested in learning about space exploration."

# System message for GPT-3.5 Turbo
SYSTEM_MESSAGE = "You are a content recommendation assistant. Provide relevant content suggestions based on the user's query."

# Generating a content recommendation based on user input
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": USER_INPUT},
    ],
)

# Extract the recommendation from the response
recommendation = completion.choices[0].message.content

# Using Metaphor for enhancing the recommendation of Content
metaphor_query = f"Enhance content recommendation for '{USER_INPUT}'"
search_response = metaphor.search(
    metaphor_query, use_autoprompt=True, start_published_date="2023-06-01"
)

# Extract relevant URLs from Metaphor's search results
relevant_urls = [result.url for result in search_response.results]

# Present the enhanced recommendation to the user as Output
print(f"Enhanced Recommendation: {recommendation}")
print(f"Relevant URLs: {relevant_urls}\n")
