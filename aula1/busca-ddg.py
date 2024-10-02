from langchain_community.tools import DuckDuckGoSearchRun
ddg_search = DuckDuckGoSearchRun()
result = ddg_search.run("Medalhas de ouro do Brasil nas olimpiadas 2024")
print(result)