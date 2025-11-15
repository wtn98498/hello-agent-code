
with open('../firstagent/prompt.txt', 'r', encoding='utf-8') as file:
    AGENT_SYSTEM_PROMPT = file.read()

print(AGENT_SYSTEM_PROMPT)