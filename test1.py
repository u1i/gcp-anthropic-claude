# Import required libraries
from anthropic import AnthropicVertex

# Set your Google Cloud Project ID
PROJECT_ID = "myproject-123"

# Initialize the AnthropicVertex client
client = AnthropicVertex(project_id=PROJECT_ID, region="us-east5")

# Initialize an empty list to store the results
result = []

# Define the user message and the parameters for streaming
with client.messages.stream(
    model="claude-3-5-sonnet@20240620",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Send me a recipe for banana bread.",
        }
    ],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
        result.append(text)

# Print the resulting text
final_result = ''.join(result)
print("\nFinal Result:")
print(final_result)

