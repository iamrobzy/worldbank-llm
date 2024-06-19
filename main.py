from llm4data.prompts.indicators import wdi

# Create a WDI API prompt object
wdi_api = wdi.WDIAPIPrompt()

# Send a prompt to the LLM to get a WDI API URL relevant to the prompt
response = wdi_api.send_prompt(
    "What is the gdp and the co2 emissions of the philippines and its neighbors in the last decade?"
)

# Parse the response to get the WDI API URL
wdi_api_url = wdi_api.parse_response(response)
print(wdi_api_url)