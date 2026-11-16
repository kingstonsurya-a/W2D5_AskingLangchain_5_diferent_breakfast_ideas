"""
Week 2 · Day 5 — Ask LangChain for 5 Breakfast Ideas

Run:
    export OPENAI_API_KEY="your-real-key"
    python breakfast.py          # prints just the 5 ideas
    python breakfast.py --raw    # also prints the whole message object once
"""

import os
import sys

from langchain_openai import ChatOpenAI

# API key comes from the environment only — never hard-coded.
if not os.getenv("OPENAI_API_KEY"):
    sys.exit("OPENAI_API_KEY is not set. Run: export OPENAI_API_KEY=\"your-key\"")

# Default temperature -> the five ideas usually change between runs.
# For the same five every run, use: ChatOpenAI(model="gpt-4o-mini", temperature=0)
llm = ChatOpenAI(model="gpt-4o-mini")

# "Healthy" is defined here instead of leaving it to the model,
# and the output format is pinned so the reply is predictable.
prompt = """Give me exactly 5 healthy breakfast ideas.

"Healthy" means: high in protein or fibre, low in added sugar,
made from whole foods, and quick to make at home (under 20 minutes).
Prefer Indian breakfast options.

Format rules:
- A numbered list from 1 to 5.
- One line per idea: the dish name, then a short note on why it is healthy.
- No introduction, no closing sentence, no extra text, just the 5 lines."""

reply = llm.invoke(prompt)

if "--raw" in sys.argv:
    # The lesson: invoke() returns an AIMessage object, not a string.
    print("----- Full message object -----")
    print(reply)
    print("-------------------------------\n")

# .content holds just the text of the reply.
print(reply.content)