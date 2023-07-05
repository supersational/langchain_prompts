# LangChain Prompts

Some examples of prompts from the [LangChain](https://github.com/hwchase17/langchain) codebase.
Note: Not comprehensive, and may contain truncated strings where the string concatenated with a `+`.
## [/retrievers/document_compressors/chain_filter_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//retrievers/document_compressors/chain_filter_prompt.py#L2)
```python
	prompt_template = """Given the following question and context, return YES if the context is relevant to the question and NO if it isn't.
	
	> Question: {question}
	> Context:
	>>>
	{context}
	>>>
	> Relevant (YES / NO):"""
	
```

## [/retrievers/document_compressors/chain_extract_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//retrievers/document_compressors/chain_extract_prompt.py#L2)
```python
	prompt_template = """Given the following question and context, extract any part of the context *AS IS* that is relevant to answer the question. If none of the context is relevant return {no_output_str}. 
	
	Remember, *DO NOT* edit the extracted parts of the context.
	
	> Question: {{question}}
	> Context:
	>>>
	{{context}}
	>>>
	Extracted relevant parts:"""
	
```

## [/tools/spark_sql/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//tools/spark_sql/prompt.py#L2)
```python
	QUERY_CHECKER = """
	{query}
	Double check the Spark SQL query above for common mistakes, including:
	- Using NOT IN with NULL values
	- Using UNION when UNION ALL should have been used
	- Using BETWEEN for exclusive ranges
	- Data type mismatch in predicates
	- Properly quoting identifiers
	- Using the correct number of arguments for functions
	- Casting to the correct data type
	- Using the proper columns for joins
	
	If there are any of the above mistakes, rewrite the query. If there are no mistakes, just reproduce the original query."""
	
```

## [/tools/sql_database/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//tools/sql_database/prompt.py#L2)
```python
	QUERY_CHECKER = """
	{query}
	Double check the {dialect} query above for common mistakes, including:
	- Using NOT IN with NULL values
	- Using UNION when UNION ALL should have been used
	- Using BETWEEN for exclusive ranges
	- Data type mismatch in predicates
	- Properly quoting identifiers
	- Using the correct number of arguments for functions
	- Casting to the correct data type
	- Using the proper columns for joins
	
	If there are any of the above mistakes, rewrite the query. If there are no mistakes, just reproduce the original query."""
	
```

## [/tools/jira/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//tools/jira/prompt.py#L2)
```python
	JIRA_ISSUE_CREATE_PROMPT = """
	    This tool is a wrapper around atlassian-python-api's Jira issue_create API, useful when you need to create a Jira issue. 
	    The input to this tool is a dictionary specifying the fields of the Jira issue, and will be passed into atlassian-python-api's Jira `issue_create` function.
	    For example, to create a low priority task called "test issue" with description "test description", you would pass in the following dictionary: 
	    {{"summary": "test issue", "description": "test description", "issuetype": {{"name": "Task"}}, "priority": {{"name": "Low"}}}}
	    """
	
```

## [/tools/jira/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//tools/jira/prompt.py#L24)
```python
	JIRA_CATCH_ALL_PROMPT = """
	    This tool is a wrapper around atlassian-python-api's Jira API.
	    There are other dedicated tools for fetching all projects, and creating and searching for issues, 
	    use this tool if you need to perform any other actions allowed by the atlassian-python-api Jira API.
	    The input to this tool is line of python code that calls a function from atlassian-python-api's Jira API
	    For example, to update the summary field of an issue, you would pass in the following string:
	    self.jira.update_issue_field(key, {{"summary": "New summary"}})
	    or to find out how many projects are in the Jira instance, you would pass in the following string:
	    self.jira.projects()
	    For more information on the Jira API, refer to https://atlassian-python-api.readthedocs.io/jira.html
	    """
	
```

## [/tools/jira/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//tools/jira/prompt.py#L36)
```python
	JIRA_CONFLUENCE_PAGE_CREATE_PROMPT = """This tool is a wrapper around atlassian-python-api's Confluence 
	atlassian-python-api API, useful when you need to create a Confluence page. The input to this tool is a dictionary 
	specifying the fields of the Confluence page, and will be passed into atlassian-python-api's Confluence `create_page` 
	function. For example, to create a page in the DEMO space titled "This is the title" with body "This is the body. You can use 
	<strong>HTML tags</strong>!", you would pass in the following dictionary: {{"space": "DEMO", "title":"This is the 
	title","body":"This is the body. You can use <strong>HTML tags</strong>!"}} """
	
```

## [/tools/powerbi/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//tools/powerbi/prompt.py#L2)
```python
	QUESTION_TO_QUERY = """
	Answer the question below with a DAX query that can be sent to Power BI. DAX queries have a simple syntax comprised of just one required keyword, EVALUATE, and several optional keywords: ORDER BY, START AT, DEFINE, MEASURE, VAR, TABLE, and COLUMN. Each keyword defines a statement used for the duration of the query. Any time < or > are used in the text below it means that those values need to be replaced by table, columns or other things. If the question is not something you can answer with a DAX query, reply with "I cannot answer this" and the question will be escalated to a human.
	
	Some DAX functions return a table instead of a scalar, and must be wrapped in a function that evaluates the table and returns a scalar; unless the table is a single column, single row table, then it is treated as a scalar value. Most DAX functions require one or more arguments, which can include tables, columns, expressions, and values. However, some functions, such as PI, do not require any arguments, but always require parentheses to indicate the null argument. For example, you must always type PI(), not PI. You can also nest functions within other functions. 
	
	Some commonly used functions are:
	EVALUATE <table> - At the most basic level, a DAX query is an EVALUATE statement containing a table expression. At least one EVALUATE statement is required, however, a query can contain any number of EVALUATE statements.
	EVALUATE <table> ORDER BY <expression> ASC or DESC - The optional ORDER BY keyword defines one or more expressions used to sort query results. Any expression that can be evaluated for each row of the result is valid.
	EVALUATE <table> ORDER BY <expression> ASC or DESC START AT <value> or <parameter> - The optional START AT keyword is used inside an ORDER BY clause. It defines the value at which the query results begin.
	DEFINE MEASURE | VAR; EVALUATE <table> - The optional DEFINE keyword introduces one or more calculated entity definitions that exist only for the duration of the query. Definitions precede the EVALUATE statement and are valid for all EVALUATE statements in the query. Definitions can be variables, measures, tables1, and columns1. Definitions can reference other definitions that appear before or after the current definition. At least one definition is required if the DEFINE keyword is included in a query.
	MEASURE <table name>[<measure name>] = <scalar expression> - Introduces a measure definition in a DEFINE statement of a DAX query.
	VAR <name> = <expression> - Stores the result of an expression as a named variable, which can then be passed as an argument to other measure expressions. Once resultant values have been calculated for a variable expression, those values do not change, even if the variable is referenced in another expression.
	
	FILTER(<table>,<filter>) - Returns a table that represents a subset of another table or expression, where <filter> is a Boolean expression that is to be evaluated for each row of the table. For example, [Amount] > 0 or [Region] = "France"
	ROW(<name>, <expression>) - Returns a table with a single row containing values that result from the expressions given to each column.
	DISTINCT(<column>) - Returns a one-column table that contains the distinct values from the specified column. In other words, duplicate values are removed and only unique values are returned. This function cannot be used to Return values into a cell or column on a worksheet; rather, you nest the DISTINCT function within a formula, to get a list of distinct values that can be passed to another function and then counted, summed, or used for other operations.
	DISTINCT(<table>) - Returns a table by removing duplicate rows from another table or expression.
	
	Aggregation functions, names with a A in it, handle booleans and empty strings in appropriate ways, while the same function without A only uses the numeric values in a column. Functions names with an X in it can include a expression as an argument, this will be evaluated for each row in the table and the result will be used in the regular function calculation, these are the functions:
	COUNT(<column>), COUNTA(<column>), COUNTX(<table>,<expression>), COUNTAX(<table>,<expression>), COUNTROWS([<table>]), COUNTBLANK(<column>), DISTINCTCOUNT(<column>), DISTINCTCOUNTNOBLANK (<column>) - these are all variantions of count functions.
	AVERAGE(<column>), AVERAGEA(<column>), AVERAGEX(<table>,<expression>) - these are all variantions of average functions.
	MAX(<column>), MAXA(<column>), MAXX(<table>,<expression>) - these are all variantions of max functions.
	MIN(<column>), MINA(<column>), MINX(<table>,<expression>) - these are all variantions of min functions.
	PRODUCT(<column>), PRODUCTX(<table>,<expression>) - these are all variantions of product functions.
	SUM(<column>), SUMX(<table>,<expression>) - these are all variantions of sum functions.
	
	Date and time functions:
	DATE(year, month, day) - Returns a date value that represents the specified year, month, and day.
	DATEDIFF(date1, date2, <interval>) - Returns the difference between two date values, in the specified interval, that can be SECOND, MINUTE, HOUR, DAY, WEEK, MONTH, QUARTER, YEAR.
	DATEVALUE(<date_text>) - Returns a date value that represents the specified date.
	YEAR(<date>), QUARTER(<date>), MONTH(<date>), DAY(<date>), HOUR(<date>), MINUTE(<date>), SECOND(<date>) - Returns the part of the date for the specified date.
	
	Finally, make sure to escape double quotes with a single backslash, and make sure that only table names have single quotes around them, while names of measures or the values of columns that you want to compare against are in escaped double quotes. Newlines are not necessary and can be skipped. The queries are serialized as json and so will have to fit be compliant with json syntax. Sometimes you will get a question, a DAX query and a error, in that case you need to rewrite the DAX query to get the correct answer.
	
	The following tables exist: {tables}
	
	and the schema's for some are given here:
	{schemas}
	
	Examples:
	{examples}
	
	Question: {tool_input}
	DAX: 
	"""
	
```

## [/tools/graphql/tool.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//tools/graphql/tool.py#L18)
```python
	    description = """\
	    Input to this tool is a detailed and correct GraphQL query, output is a result from the API.
	    If the query is not correct, an error message will be returned.
	    If an error is returned with 'Bad request' in it, rewrite the query and try again.
	    If an error is returned with 'Unauthorized' in it, do not try again, but tell the user to change their authentication.
	
	    Example Input: query {{ allUsers {{ id, name, email }} }}\
	    """  # noqa: E501
	
```

## [/memory/entity.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//memory/entity.py#L184)
```python
	        create_table_query = f"""
	            CREATE TABLE IF NOT EXISTS {self.full_table_name} (
	                key TEXT PRIMARY KEY,
	                value TEXT
	            )
	        """
	
```

## [/memory/entity.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//memory/entity.py#L194)
```python
	        query = f"""
	            SELECT value
	            FROM {self.full_table_name}
	            WHERE key = ?
	        """
	
```

## [/memory/entity.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//memory/entity.py#L209)
```python
	        query = f"""
	            INSERT OR REPLACE INTO {self.full_table_name} (key, value)
	            VALUES (?, ?)
	        """
	
```

## [/memory/entity.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//memory/entity.py#L225)
```python
	        query = f"""
	            SELECT 1
	            FROM {self.full_table_name}
	            WHERE key = ?
	            LIMIT 1
	        """
	
```

## [/memory/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//memory/prompt.py#L4)
```python
	_DEFAULT_ENTITY_MEMORY_CONVERSATION_TEMPLATE = """You are an assistant to a human, powered by a large language model trained by OpenAI.
	
	You are designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, you are able to generate human-like text based on the input you receive, allowing you to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.
	
	You are constantly learning and improving, and your capabilities are constantly evolving. You are able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. You have access to some personalized information provided by the human in the Context section below. Additionally, you are able to generate your own text based on the input you receive, allowing you to engage in discussions and provide explanations and descriptions on a wide range of topics.
	
	Overall, you are a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether the human needs help with a specific question or just wants to have a conversation about a particular topic, you are here to assist.
	
	Context:
	{entities}
	
	Current conversation:
	{history}
	Last line:
	Human: {input}
	You:"""
	
```

## [/memory/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//memory/prompt.py#L26)
```python
	_DEFAULT_SUMMARIZER_TEMPLATE = """Progressively summarize the lines of conversation provided, adding onto the previous summary returning a new summary.
	
	EXAMPLE
	Current summary:
	The human asks what the AI thinks of artificial intelligence. The AI thinks artificial intelligence is a force for good.
	
	New lines of conversation:
	Human: Why do you think artificial intelligence is a force for good?
	AI: Because artificial intelligence will help humans reach their full potential.
	
	New summary:
	The human asks what the AI thinks of artificial intelligence. The AI thinks artificial intelligence is a force for good because it will help humans reach their full potential.
	END OF EXAMPLE
	
	Current summary:
	{summary}
	
	New lines of conversation:
	{new_lines}
	
	New summary:"""
	
```

## [/memory/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//memory/prompt.py#L51)
```python
	_DEFAULT_ENTITY_EXTRACTION_TEMPLATE = """You are an AI assistant reading the transcript of a conversation between an AI and a human. Extract all of the proper nouns from the last line of conversation. As a guideline, a proper noun is generally capitalized. You should definitely extract all names and places.
	
	The conversation history is provided just in case of a coreference (e.g. "What do you know about him" where "him" is defined in a previous line) -- ignore items mentioned there that are not in the last line.
	
	Return the output as a single comma-separated list, or NONE if there is nothing of note to return (e.g. the user is just issuing a greeting or having a simple conversation).
	
	EXAMPLE
	Conversation history:
	Person #1: how's it going today?
	AI: "It's going great! How about you?"
	Person #1: good! busy working on Langchain. lots to do.
	AI: "That sounds like a lot of work! What kind of things are you doing to make Langchain better?"
	Last line:
	Person #1: i'm trying to improve Langchain's interfaces, the UX, its integrations with various products the user might want ... a lot of stuff.
	Output: Langchain
	END OF EXAMPLE
	
	EXAMPLE
	Conversation history:
	Person #1: how's it going today?
	AI: "It's going great! How about you?"
	Person #1: good! busy working on Langchain. lots to do.
	AI: "That sounds like a lot of work! What kind of things are you doing to make Langchain better?"
	Last line:
	Person #1: i'm trying to improve Langchain's interfaces, the UX, its integrations with various products the user might want ... a lot of stuff. I'm working with Person #2.
	Output: Langchain, Person #2
	END OF EXAMPLE
	
	Conversation history (for reference only):
	{history}
	Last line of conversation (for extraction):
	Human: {input}
	
	Output:"""
	
```

## [/memory/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//memory/prompt.py#L89)
```python
	_DEFAULT_ENTITY_SUMMARIZATION_TEMPLATE = """You are an AI assistant helping a human keep track of facts about relevant people, places, and concepts in their life. Update the summary of the provided entity in the "Entity" section based on the last line of your conversation with the human. If you are writing the summary for the first time, return a single sentence.
	The update should only include facts that are relayed in the last line of conversation about the provided entity, and should only contain facts about the provided entity.
	
	If there is no new information about the provided entity or the information is not worth noting (not an important or relevant fact to remember long-term), return the existing summary unchanged.
	
	Full conversation history (for context):
	{history}
	
	Entity to summarize:
	{entity}
	
	Existing summary of {entity}:
	{summary}
	
	Last line of conversation:
	Human: {input}
	Updated summary:"""
	
```

## [/memory/chat_message_histories/postgres.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//memory/chat_message_histories/postgres.py#L41)
```python
	        create_table_query = f"""CREATE TABLE IF NOT EXISTS {self.table_name} (
	            id SERIAL PRIMARY KEY,
	            session_id TEXT NOT NULL,
	            message JSONB NOT NULL
	        );"""
	
```

## [/callbacks/mlflow_callback.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//callbacks/mlflow_callback.py#L105)
```python
	    return f"""
	    <p style="color:black;">{formatted_prompt}:</p>
	    <blockquote>
	      <p style="color:green;">
	        {formatted_generation}
	      </p>
	    </blockquote>
	    """
	
```

## [/agents/self_ask_with_search/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/self_ask_with_search/prompt.py#L4)
```python
	_DEFAULT_TEMPLATE = """Question: Who lived longer, Muhammad Ali or Alan Turing?
	Are follow up questions needed here: Yes.
	Follow up: How old was Muhammad Ali when he died?
	Intermediate answer: Muhammad Ali was 74 years old when he died.
	Follow up: How old was Alan Turing when he died?
	Intermediate answer: Alan Turing was 41 years old when he died.
	So the final answer is: Muhammad Ali
	
	Question: When was the founder of craigslist born?
	Are follow up questions needed here: Yes.
	Follow up: Who was the founder of craigslist?
	Intermediate answer: Craigslist was founded by Craig Newmark.
	Follow up: When was Craig Newmark born?
	Intermediate answer: Craig Newmark was born on December 6, 1952.
	So the final answer is: December 6, 1952
	
	Question: Who was the maternal grandfather of George Washington?
	Are follow up questions needed here: Yes.
	Follow up: Who was the mother of George Washington?
	Intermediate answer: The mother of George Washington was Mary Ball Washington.
	Follow up: Who was the father of Mary Ball Washington?
	Intermediate answer: The father of Mary Ball Washington was Joseph Ball.
	So the final answer is: Joseph Ball
	
	Question: Are both the directors of Jaws and Casino Royale from the same country?
	Are follow up questions needed here: Yes.
	Follow up: Who is the director of Jaws?
	Intermediate answer: The director of Jaws is Steven Spielberg.
	Follow up: Where is Steven Spielberg from?
	Intermediate answer: The United States.
	Follow up: Who is the director of Casino Royale?
	Intermediate answer: The director of Casino Royale is Martin Campbell.
	Follow up: Where is Martin Campbell from?
	Intermediate answer: New Zealand.
	So the final answer is: No
	
	Question: {input}
	Are followup questions needed here:{agent_scratchpad}"""
	
```

## [/agents/chat/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/chat/prompt.py#L3)
```python
	FORMAT_INSTRUCTIONS = """The way you use the tools is by specifying a json blob.
	Specifically, this json should have a `action` key (with the name of the tool to use) and a `action_input` key (with the input to the tool going here).
	
	The only values that should be in the "action" field are: {tool_names}
	
	The $JSON_BLOB should only contain a SINGLE action, do NOT return a list of multiple actions. Here is an example of a valid $JSON_BLOB:
	
	```
	{{{{
	  "action": $TOOL_NAME,
	  "action_input": $INPUT
	}}}}
	```
	
	ALWAYS use the following format:
	
	Question: the input question you must answer
	Thought: you should always think about what to do
	Action:
	```
	$JSON_BLOB
	```
	Observation: the result of the action
	... (this Thought/Action/Observation can repeat N times)
	Thought: I now know the final answer
	Final Answer: the final answer to the original input question"""
	
```

## [/agents/mrkl/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/mrkl/prompt.py#L3)
```python
	FORMAT_INSTRUCTIONS = """Use the following format:
	
	Question: the input question you must answer
	Thought: you should always think about what to do
	Action: the action to take, should be one of [{tool_names}]
	Action Input: the input to the action
	Observation: the result of the action
	... (this Thought/Action/Action Input/Observation can repeat N times)
	Thought: I now know the final answer
	Final Answer: the final answer to the original input question"""
	
```

## [/agents/structured_chat/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/structured_chat/prompt.py#L3)
```python
	FORMAT_INSTRUCTIONS = """Use a json blob to specify a tool by providing an action key (tool name) and an action_input key (tool input).
	
	Valid "action" values: "Final Answer" or {tool_names}
	
	Provide only ONE action per $JSON_BLOB, as shown:
	
	```
	{{{{
	  "action": $TOOL_NAME,
	  "action_input": $INPUT
	}}}}
	```
	
	Follow this format:
	
	Question: input question to answer
	Thought: consider previous and subsequent steps
	Action:
	```
	$JSON_BLOB
	```
	Observation: action result
	... (repeat Thought/Action/Observation N times)
	Thought: I know what to respond
	Action:
	```
	{{{{
	  "action": "Final Answer",
	  "action_input": "Final response to human"
	}}}}
	```"""
	
```

## [/agents/conversational_chat/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/conversational_chat/prompt.py#L10)
```python
	FORMAT_INSTRUCTIONS = """RESPONSE FORMAT INSTRUCTIONS
	----------------------------
	
	When responding to me, please output a response in one of two formats:
	
	**Option 1:**
	Use this if you want the human to use a tool.
	Markdown code snippet formatted in the following schema:
	
	```json
	{{{{
	    "action": string, \\ The action to take. Must be one of {tool_names}
	    "action_input": string \\ The input to the action
	}}}}
	```
	
	**Option #2:**
	Use this if you want to respond directly to the human. Markdown code snippet formatted in the following schema:
	
	```json
	{{{{
	    "action": "Final Answer",
	    "action_input": string \\ You should put what you want to return to use here
	}}}}
	```"""
	
```

## [/agents/conversational_chat/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/conversational_chat/prompt.py#L36)
```python
	SUFFIX = """TOOLS
	------
	Assistant can ask the user to use tools to look up information that may be helpful in answering the users original question. The tools the human can use are:
	
	{{tools}}
	
	{format_instructions}
	
	USER'S INPUT
	--------------------
	Here is the user's input (remember to respond with a markdown code snippet of a json blob with a single action, and NOTHING else):
	
	{{{{input}}}}"""
	
```

## [/agents/conversational_chat/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/conversational_chat/prompt.py#L50)
```python
	TEMPLATE_TOOL_RESPONSE = """TOOL RESPONSE: 
	---------------------
	{observation}
	
	USER'S INPUT
	--------------------
	
	Okay, so what is the response to my last comment? If using information obtained from the tools you must mention it explicitly without mentioning the tool names - I have forgotten all TOOL RESPONSES! Remember to respond with a markdown code snippet of a json blob with a single action, and NOTHING else."""
	
```

## [/agents/agent_toolkits/spark_sql/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/spark_sql/prompt.py#L3)
```python
	SQL_PREFIX = """You are an agent designed to interact with Spark SQL.
	Given an input question, create a syntactically correct Spark SQL query to run, then look at the results of the query and return the answer.
	Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most {top_k} results.
	You can order the results by a relevant column to return the most interesting examples in the database.
	Never query for all the columns from a specific table, only ask for the relevant columns given the question.
	You have access to tools for interacting with the database.
	Only use the below tools. Only use the information returned by the below tools to construct your final answer.
	You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.
	
	DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
	
	If the question does not seem related to the database, just return "I don't know" as the answer.
	"""
	
```

## [/agents/agent_toolkits/spark_sql/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/spark_sql/prompt.py#L17)
```python
	SQL_SUFFIX = """Begin!
	
	Question: {input}
	Thought: I should look at the tables in the database to see what I can query.
	{agent_scratchpad}"""
	
```

## [/agents/agent_toolkits/openapi/planner_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/openapi/planner_prompt.py#L6)
```python
	API_PLANNER_PROMPT = """You are a planner that plans a sequence of API calls to assist with user queries against an API.
	
	You should:
	1) evaluate whether the user query can be solved by the API documentated below. If no, say why.
	2) if yes, generate a plan of API calls and say what they are doing step by step.
	3) If the plan includes a DELETE call, you should always return an ask from the User for authorization first unless the User has specifically asked to delete something.
	
	You should only use API endpoints documented below ("Endpoints you can use:").
	You can only use the DELETE tool if the User has specifically asked to delete something. Otherwise, you should return a request authorization from the User first.
	Some user queries can be resolved in a single API call, but some will require several API calls.
	The plan will be passed to an API controller that can format it into web requests and return the responses.
	
	----
	
	Here are some examples:
	
	Fake endpoints for examples:
	GET /user to get information about the current user
	GET /products/search search across products
	POST /users/{{id}}/cart to add products to a user's cart
	PATCH /users/{{id}}/cart to update a user's cart
	DELETE /users/{{id}}/cart to delete a user's cart
	
	User query: tell me a joke
	Plan: Sorry, this API's domain is shopping, not comedy.
	
	User query: I want to buy a couch
	Plan: 1. GET /products with a query param to search for couches
	2. GET /user to find the user's id
	3. POST /users/{{id}}/cart to add a couch to the user's cart
	
	User query: I want to add a lamp to my cart
	Plan: 1. GET /products with a query param to search for lamps
	2. GET /user to find the user's id
	3. PATCH /users/{{id}}/cart to add a lamp to the user's cart
	
	User query: I want to delete my cart
	Plan: 1. GET /user to find the user's id
	2. DELETE required. Did user specify DELETE or previously authorize? Yes, proceed.
	3. DELETE /users/{{id}}/cart to delete the user's cart
	
	User query: I want to start a new cart
	Plan: 1. GET /user to find the user's id
	2. DELETE required. Did user specify DELETE or previously authorize? No, ask for authorization.
	3. Are you sure you want to delete your cart? 
	----
	
	Here are endpoints you can use. Do not reference any of the endpoints above.
	
	{endpoints}
	
	----
	
	User query: {query}
	Plan:"""
	
```

## [/agents/agent_toolkits/openapi/planner_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/openapi/planner_prompt.py#L62)
```python
	API_PLANNER_TOOL_DESCRIPTION = f"Can be used to generate the right API calls to assist with a user query, like {API_PLANNER_TOOL_NAME}(query). Should always be called before trying to call the API controller."
	
```

## [/agents/agent_toolkits/openapi/planner_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/openapi/planner_prompt.py#L65)
```python
	API_CONTROLLER_PROMPT = """You are an agent that gets a sequence of API calls and given their documentation, should execute them and return the final response.
	If you cannot complete them and run into issues, you should explain the issue. If you're able to resolve an API call, you can retry the API call. When interacting with API objects, you should extract ids for inputs to other API calls but ids and names for outputs returned to the User.
	
	
	Here is documentation on the API:
	Base url: {api_url}
	Endpoints:
	{api_docs}
	
	
	Here are tools to execute requests against the API: {tool_descriptions}
	
	
	Starting below, you should follow this format:
	
	Plan: the plan of API calls to execute
	Thought: you should always think about what to do
	Action: the action to take, should be one of the tools [{tool_names}]
	Action Input: the input to the action
	Observation: the output of the action
	... (this Thought/Action/Action Input/Observation can repeat N times)
	Thought: I am finished executing the plan (or, I cannot finish executing the plan without knowing some other information.)
	Final Answer: the final output from executing the plan or missing information I'd need to re-plan correctly.
	
	
	Begin!
	
	Plan: {input}
	Thought:
	{agent_scratchpad}
	"""
	
```

## [/agents/agent_toolkits/openapi/planner_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/openapi/planner_prompt.py#L102)
```python
	API_ORCHESTRATOR_PROMPT = """You are an agent that assists with user queries against API, things like querying information or creating resources.
	Some user queries can be resolved in a single API call, particularly if you can find appropriate params from the OpenAPI spec; though some require several API calls.
	You should always plan your API calls first, and then execute the plan second.
	If the plan includes a DELETE call, be sure to ask the User for authorization first unless the User has specifically asked to delete something.
	You should never return information without executing the api_controller tool.
	
	
	Here are the tools to plan and execute API requests: {tool_descriptions}
	
	
	Starting below, you should follow this format:
	
	User query: the query a User wants help with related to the API
	Thought: you should always think about what to do
	Action: the action to take, should be one of the tools [{tool_names}]
	Action Input: the input to the action
	Observation: the result of the action
	... (this Thought/Action/Action Input/Observation can repeat N times)
	Thought: I am finished executing a plan and have the information the user asked for or the data the user asked to create
	Final Answer: the final output from executing the plan
	
	
	Example:
	User query: can you add some trendy stuff to my shopping cart.
	Thought: I should plan API calls first.
	Action: api_planner
	Action Input: I need to find the right API calls to add trendy items to the users shopping cart
	Observation: 1) GET /items with params 'trending' is 'True' to get trending item ids
	2) GET /user to get user
	3) POST /cart to post the trending items to the user's cart
	Thought: I'm ready to execute the API calls.
	Action: api_controller
	Action Input: 1) GET /items params 'trending' is 'True' to get trending item ids
	2) GET /user to get user
	3) POST /cart to post the trending items to the user's cart
	...
	
	Begin!
	
	User query: {input}
	Thought: I should generate a plan to help with this query and then copy that plan exactly to the controller.
	{agent_scratchpad}"""
	
```

## [/agents/agent_toolkits/openapi/planner_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/openapi/planner_prompt.py#L155)
```python
	    template="""Here is an API response:\n\n{response}\n\n====
	Your task is to extract some information according to these instructions: {instructions}
	When working with API objects, you should usually use ids over names.
	If the response indicates an error, you should instead output a summary of the error.
	
	Output:""",
	
```

## [/agents/agent_toolkits/openapi/planner_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/openapi/planner_prompt.py#L172)
```python
	    template="""Here is an API response:\n\n{response}\n\n====
	Your task is to extract some information according to these instructions: {instructions}
	When working with API objects, you should usually use ids over names. Do not return any ids or names that are not in the response.
	If the response indicates an error, you should instead output a summary of the error.
	
	Output:""",
	
```

## [/agents/agent_toolkits/openapi/planner_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/openapi/planner_prompt.py#L189)
```python
	    template="""Here is an API response:\n\n{response}\n\n====
	Your task is to extract some information according to these instructions: {instructions}
	When working with API objects, you should usually use ids over names. Do not return any ids or names that are not in the response.
	If the response indicates an error, you should instead output a summary of the error.
	
	Output:""",
	
```

## [/agents/agent_toolkits/openapi/planner_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/openapi/planner_prompt.py#L206)
```python
	    template="""Here is an API response:\n\n{response}\n\n====
	Your task is to extract some information according to these instructions: {instructions}
	When working with API objects, you should usually use ids over names. Do not return any ids or names that are not in the response.
	If the response indicates an error, you should instead output a summary of the error.
	
	Output:""",
	
```

## [/agents/agent_toolkits/openapi/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/openapi/prompt.py#L19)
```python
	OPENAPI_SUFFIX = """Begin!
	
	Question: {input}
	Thought: I should explore the spec to find the base url for the API.
	{agent_scratchpad}"""
	
```

## [/agents/agent_toolkits/json/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/json/prompt.py#L21)
```python
	JSON_SUFFIX = """Begin!"
	
	Question: {input}
	Thought: I should look at the keys that exist in data to see what I have access to
	{agent_scratchpad}"""
	
```

## [/agents/agent_toolkits/powerbi/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/powerbi/prompt.py#L5)
```python
	POWERBI_PREFIX = """You are an agent designed to help users interact with a PowerBI Dataset.
	
	Agent has access to a tool that can write a query based on the question and then run those against PowerBI, Microsofts business intelligence tool. The questions from the users should be interpreted as related to the dataset that is available and not general questions about the world. If the question does not seem related to the dataset, just return "This does not appear to be part of this dataset." as the answer.
	
	Given an input question, ask to run the questions against the dataset, then look at the results and return the answer, the answer should be a complete sentence that answers the question, if multiple rows are asked find a way to write that in a easily readable format for a human, also make sure to represent numbers in readable ways, like 1M instead of 1000000. Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most {top_k} results.
	"""
	
```

## [/agents/agent_toolkits/powerbi/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/powerbi/prompt.py#L12)
```python
	POWERBI_SUFFIX = """Begin!
	
	Question: {input}
	Thought: I can first ask which tables I have, then how each table is defined and then ask the query tool the question I need, and finally create a nice sentence that answers the question.
	{agent_scratchpad}"""
	
```

## [/agents/agent_toolkits/powerbi/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/powerbi/prompt.py#L18)
```python
	POWERBI_CHAT_PREFIX = """Assistant is a large language model built to help users interact with a PowerBI Dataset.
	
	Assistant has access to a tool that can write a query based on the question and then run those against PowerBI, Microsofts business intelligence tool. The questions from the users should be interpreted as related to the dataset that is available and not general questions about the world. If the question does not seem related to the dataset, just return "This does not appear to be part of this dataset." as the answer.
	
	Given an input question, ask to run the questions against the dataset, then look at the results and return the answer, the answer should be a complete sentence that answers the question, if multiple rows are asked find a way to write that in a easily readable format for a human, also make sure to represent numbers in readable ways, like 1M instead of 1000000. Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most {top_k} results.
	"""
	
```

## [/agents/agent_toolkits/powerbi/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/powerbi/prompt.py#L25)
```python
	POWERBI_CHAT_SUFFIX = """TOOLS
	------
	Assistant can ask the user to use tools to look up information that may be helpful in answering the users original question. The tools the human can use are:
	
	{{tools}}
	
	{format_instructions}
	
	USER'S INPUT
	--------------------
	Here is the user's input (remember to respond with a markdown code snippet of a json blob with a single action, and NOTHING else):
	
	{{{{input}}}}
	"""
	
```

## [/agents/agent_toolkits/pandas/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/pandas/prompt.py#L7)
```python
	MULTI_DF_PREFIX = """
	You are working with {num_dfs} pandas dataframes in Python named df1, df2, etc. You 
	should use the tools below to answer the question posed of you:"""
	
```

## [/agents/agent_toolkits/pandas/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/pandas/prompt.py#L16)
```python
	SUFFIX_WITH_DF = """
	This is the result of `print(df.head())`:
	{df_head}
	
	Begin!
	Question: {input}
	{agent_scratchpad}"""
	
```

## [/agents/agent_toolkits/pandas/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/pandas/prompt.py#L24)
```python
	SUFFIX_WITH_MULTI_DF = """
	This is the result of `print(df.head())` for each dataframe:
	{dfs_head}
	
	Begin!
	Question: {input}
	{agent_scratchpad}"""
	
```

## [/agents/agent_toolkits/sql/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/sql/prompt.py#L3)
```python
	SQL_PREFIX = """You are an agent designed to interact with a SQL database.
	Given an input question, create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
	Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most {top_k} results.
	You can order the results by a relevant column to return the most interesting examples in the database.
	Never query for all the columns from a specific table, only ask for the relevant columns given the question.
	You have access to tools for interacting with the database.
	Only use the below tools. Only use the information returned by the below tools to construct your final answer.
	You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.
	
	DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
	
	If the question does not seem related to the database, just return "I don't know" as the answer.
	"""
	
```

## [/agents/agent_toolkits/sql/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/agent_toolkits/sql/prompt.py#L17)
```python
	SQL_SUFFIX = """Begin!
	
	Question: {input}
	Thought: I should look at the tables in the database to see what I can query.  Then I should query the schema of the most relevant tables.
	{agent_scratchpad}"""
	
```

## [/agents/conversational/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//agents/conversational/prompt.py#L14)
```python
	FORMAT_INSTRUCTIONS = """To use a tool, please use the following format:
	
	```
	Thought: Do I need to use a tool? Yes
	Action: the action to take, should be one of [{tool_names}]
	Action Input: the input to the action
	Observation: the result of the action
	```
	
	When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:
	
	```
	Thought: Do I need to use a tool? No
	{ai_prefix}: [your response here]
	```"""
	
```

## [/vectorstores/clickhouse.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//vectorstores/clickhouse.py#L183)
```python
	        self.schema = f"""\
	CREATE TABLE IF NOT EXISTS {self.config.database}.{self.config.table}(
	    {self.config.column_map['id']} Nullable(String),
	    {self.config.column_map['document']} Nullable(String),
	    {self.config.column_map['embedding']} Array(Float32),
	    {self.config.column_map['metadata']} JSON,
	    {self.config.column_map['uuid']} UUID DEFAULT generateUUIDv4(),
	    CONSTRAINT cons_vec_len CHECK length({self.config.column_map['embedding']}) = {dim},
	    INDEX vec_idx {self.config.column_map['embedding']} TYPE \
	{self.config.index_type}({index_params}) GRANULARITY 1000
	) ENGINE = MergeTree ORDER BY uuid SETTINGS index_granularity = 8192\
	"""
	
```

## [/vectorstores/clickhouse.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//vectorstores/clickhouse.py#L224)
```python
	        i_str = f"""
	                INSERT INTO TABLE 
	                    {self.config.database}.{self.config.table}({ks})
	                VALUES
	                {','.join(_data)}
	                """
	
```

## [/vectorstores/clickhouse.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//vectorstores/clickhouse.py#L357)
```python
	        q_str = f"""
	            SELECT {self.config.column_map['document']}, 
	                {self.config.column_map['metadata']}, dist
	            FROM {self.config.database}.{self.config.table}
	            {where_str}
	            ORDER BY L2Distance({self.config.column_map['embedding']}, [{q_emb_str}]) 
	                AS dist {self.dist_order}
	            LIMIT {topk} {' '.join(settings_strs)}
	            """
	
```

## [/vectorstores/myscale.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//vectorstores/myscale.py#L162)
```python
	        schema_ = f"""
	            CREATE TABLE IF NOT EXISTS {self.config.database}.{self.config.table}(
	                {self.config.column_map['id']} String,
	                {self.config.column_map['text']} String,
	                {self.config.column_map['vector']} Array(Float32),
	                {self.config.column_map['metadata']} JSON,
	                CONSTRAINT cons_vec_len CHECK length(\
	                    {self.config.column_map['vector']}) = {dim},
	                VECTOR INDEX vidx {self.config.column_map['vector']} \
	                    TYPE {self.config.index_type}(\
	                        'metric_type={self.config.metric}'{index_params})
	            ) ENGINE = MergeTree ORDER BY {self.config.column_map['id']}
	        """
	
```

## [/vectorstores/myscale.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//vectorstores/myscale.py#L201)
```python
	        i_str = f"""
	                INSERT INTO TABLE 
	                    {self.config.database}.{self.config.table}({ks})
	                VALUES
	                {','.join(_data)}
	                """
	
```

## [/vectorstores/myscale.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//vectorstores/myscale.py#L329)
```python
	        q_str = f"""
	            SELECT {self.config.column_map['text']}, 
	                {self.config.column_map['metadata']}, dist
	            FROM {self.config.database}.{self.config.table}
	            {where_str}
	            ORDER BY distance({self.config.column_map['vector']}, [{q_emb_str}]) 
	                AS dist {self.dist_order}
	            LIMIT {topk}
	            """
	
```

## [/vectorstores/rocksetdb.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//vectorstores/rocksetdb.py#L263)
```python
	                    ), "page content stored in column `{}` must be of type `str`. \
	                        But found: `{}`".format(
	
```

## [/vectorstores/rocksetdb.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//vectorstores/rocksetdb.py#L300)
```python
	        return f"""\
	SELECT * EXCEPT({self._embedding_key}), {distance_str}
	FROM {self._collection_name}
	{where_str}\
	ORDER BY dist {distance_func.order_by()}
	LIMIT {str(k)}
	"""
	
```

## [/vectorstores/hologres.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//vectorstores/hologres.py#L47)
```python
	            + """, 'proxima_vectors', 
	'{"embedding":{"algorithm":"Graph",
	"distance_method":"SquaredEuclidean",
	"build_params":{"min_flush_proxima_row_count" : 1,
	"min_compaction_proxima_row_count" : 1, 
	"max_total_size_to_merge_mb" : 2000}}}');"""
	
```

## [/vectorstores/analyticdb.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//vectorstores/analyticdb.py#L271)
```python
	        sql_query = f"""
	            SELECT *, l2_distance(embedding, :embedding) as distance
	            FROM {self.collection_name}
	            {filter_condition}
	            ORDER BY embedding <-> :embedding
	            LIMIT :k
	        """
	
```

## [/vectorstores/starrocks.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//vectorstores/starrocks.py#L178)
```python
	        self.schema = f"""\
	CREATE TABLE IF NOT EXISTS {self.config.database}.{self.config.table}(    
	    {self.config.column_map['id']} string,
	    {self.config.column_map['document']} string,
	    {self.config.column_map['embedding']} array<float>,
	    {self.config.column_map['metadata']} string
	) ENGINE = OLAP PRIMARY KEY(id) DISTRIBUTED BY HASH(id) \
	  PROPERTIES ("replication_num" = "1")\
	"""
	
```

## [/vectorstores/starrocks.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//vectorstores/starrocks.py#L226)
```python
	        i_str = f"""
	                INSERT INTO
	                    {self.config.database}.{self.config.table}({ks})
	                VALUES
	                {','.join(_data)}
	                """
	
```

## [/vectorstores/starrocks.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//vectorstores/starrocks.py#L360)
```python
	        q_str = f"""
	            SELECT {self.config.column_map['document']}, 
	                {self.config.column_map['metadata']}, 
	                cosine_similarity_norm(array<float>[{q_emb_str}],
	                  {self.config.column_map['embedding']}) as dist
	            FROM {self.config.database}.{self.config.table}
	            {where_str}
	            ORDER BY dist {self.dist_order}
	            LIMIT {topk}
	            """
	
```

## [/output_parsers/prompts.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//output_parsers/prompts.py#L4)
```python
	NAIVE_FIX = """Instructions:
	--------------
	{instructions}
	--------------
	Completion:
	--------------
	{completion}
	--------------
	
	Above, the Completion did not satisfy the constraints given in the Instructions.
	Error:
	--------------
	{error}
	--------------
	
	Please try again. Please only respond with an answer that satisfies the constraints laid out in the Instructions:"""
	
```

## [/output_parsers/retry.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//output_parsers/retry.py#L15)
```python
	NAIVE_COMPLETION_RETRY = """Prompt:
	{prompt}
	Completion:
	{completion}
	
	Above, the Completion did not satisfy the constraints given in the Prompt.
	Please try again:"""
	
```

## [/output_parsers/retry.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//output_parsers/retry.py#L23)
```python
	NAIVE_COMPLETION_RETRY_WITH_ERROR = """Prompt:
	{prompt}
	Completion:
	{completion}
	
	Above, the Completion did not satisfy the constraints given in the Prompt.
	Details: {error}
	Please try again:"""
	
```

## [/output_parsers/format_instructions.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//output_parsers/format_instructions.py#L3)
```python
	STRUCTURED_FORMAT_INSTRUCTIONS = """The output should be a markdown code snippet formatted in the following schema, including the leading and trailing "```json" and "```":
	
	```json
	{{
	{format}
	}}
	```"""
	
```

## [/output_parsers/format_instructions.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//output_parsers/format_instructions.py#L11)
```python
	PYDANTIC_FORMAT_INSTRUCTIONS = """The output should be formatted as a JSON instance that conforms to the JSON schema below.
	
	As an example, for the schema {{"properties": {{"foo": {{"title": "Foo", "description": "a list of strings", "type": "array", "items": {{"type": "string"}}}}}}, "required": ["foo"]}}}}
	the object {{"foo": ["bar", "baz"]}} is a well-formatted instance of the schema. The object {{"properties": {{"foo": ["bar", "baz"]}}}} is not well-formatted.
	
	Here is the output schema:
	```
	{schema}
	```"""
	
```

## [/output_parsers/datetime.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//output_parsers/datetime.py#L37)
```python
	        return f"""Write a datetime string that matches the 
	            following pattern: "{self.format}". Examples: {examples}"""
	
```

## [/evaluation/agents/trajectory_eval_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//evaluation/agents/trajectory_eval_prompt.py#L13)
```python
	EVAL_TEMPLATE = """An AI language model has been given access to the following set of tools to help answer a user's question.
	
	The tools given to the AI model are:
	
	{tool_descriptions}
	
	The question the human asked the AI model was: {question}
	
	The AI language model decided to use the following set of tools to answer the question:
	
	{agent_trajectory}
	
	The AI language model's final answer to the question was: {answer}
	
	Let's to do a detailed evaluation of the AI language model's answer step by step.
	
	We consider the following criteria before giving a score from 1 to 5:
	
	i. Is the final answer helpful?
	ii. Does the AI language use a logical sequence of tools to answer the question?
	iii. Does the AI language model use the tools in a helpful way?
	iv. Does the AI language model use too many steps to answer the question?
	v. Are the appropriate tools used to answer the question?"""
	
```

## [/evaluation/qa/eval_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//evaluation/qa/eval_prompt.py#L4)
```python
	template = """You are a teacher grading a quiz.
	You are given a question, the student's answer, and the true answer, and are asked to score the student answer as either CORRECT or INCORRECT.
	
	Example Format:
	QUESTION: question here
	STUDENT ANSWER: student's answer here
	TRUE ANSWER: true answer here
	GRADE: CORRECT or INCORRECT here
	
	Grade the student answers based ONLY on their factual accuracy. Ignore differences in punctuation and phrasing between the student answer and true answer. It is OK if the student answer contains more information than the true answer, as long as it does not contain any conflicting statements. Begin! 
	
	QUESTION: {query}
	STUDENT ANSWER: {result}
	TRUE ANSWER: {answer}
	GRADE:"""
	
```

## [/evaluation/qa/eval_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//evaluation/qa/eval_prompt.py#L23)
```python
	context_template = """You are a teacher grading a quiz.
	You are given a question, the context the question is about, and the student's answer. You are asked to score the student's answer as either CORRECT or INCORRECT, based on the context.
	
	Example Format:
	QUESTION: question here
	CONTEXT: context the question is about here
	STUDENT ANSWER: student's answer here
	GRADE: CORRECT or INCORRECT here
	
	Grade the student answers based ONLY on their factual accuracy. Ignore differences in punctuation and phrasing between the student answer and true answer. It is OK if the student answer contains more information than the true answer, as long as it does not contain any conflicting statements. Begin! 
	
	QUESTION: {query}
	CONTEXT: {context}
	STUDENT ANSWER: {result}
	GRADE:"""
	
```

## [/evaluation/qa/eval_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//evaluation/qa/eval_prompt.py#L43)
```python
	cot_template = """You are a teacher grading a quiz.
	You are given a question, the context the question is about, and the student's answer. You are asked to score the student's answer as either CORRECT or INCORRECT, based on the context.
	Write out in a step by step manner your reasoning to be sure that your conclusion is correct. Avoid simply stating the correct answer at the outset.
	
	Example Format:
	QUESTION: question here
	CONTEXT: context the question is about here
	STUDENT ANSWER: student's answer here
	EXPLANATION: step by step reasoning here
	GRADE: CORRECT or INCORRECT here
	
	Grade the student answers based ONLY on their factual accuracy. Ignore differences in punctuation and phrasing between the student answer and true answer. It is OK if the student answer contains more information than the true answer, as long as it does not contain any conflicting statements. Begin! 
	
	QUESTION: {query}
	CONTEXT: {context}
	STUDENT ANSWER: {result}
	EXPLANATION:"""
	
```

## [/evaluation/qa/eval_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//evaluation/qa/eval_prompt.py#L65)
```python
	template = """You are comparing a submitted answer to an expert answer on a given SQL coding question. Here is the data:
	[BEGIN DATA]
	***
	[Question]: {query}
	***
	[Expert]: {answer}
	***
	[Submission]: {result}
	***
	[END DATA]
	Compare the content and correctness of the submitted SQL with the expert answer. Ignore any differences in whitespace, style, or output column names. The submitted answer may either be correct or incorrect. Determine which case applies. First, explain in detail the similarities or differences between the expert answer and the submission, ignoring superficial aspects such as whitespace, style or output column names. Do not state the final answer in your initial explanation. Then, respond with either "CORRECT" or "INCORRECT" (without quotes or punctuation) on its own line. This should correspond to whether the submitted SQL and the expert answer are semantically the same or different, respectively. Then, repeat your final answer on a new line."""
	
```

## [/evaluation/qa/generate_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//evaluation/qa/generate_prompt.py#L5)
```python
	template = """You are a teacher coming up with questions to ask on a quiz. 
	Given the following document, please generate a question and answer based on that document.
	
	Example Format:
	<Begin Document>
	...
	<End Document>
	QUESTION: question here
	ANSWER: answer here
	
	These questions should be detailed and be based explicitly on information in the document. Begin!
	
	<Begin Document>
	{doc}
	<End Document>"""
	
```

## [/evaluation/run_evaluators/criteria_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//evaluation/run_evaluators/criteria_prompt.py#L6)
```python
	template = """You are assessing a submitted answer on a given task or input based on a set of criteria. Here is the data:
	[BEGIN DATA]
	***
	[Task]: {input}
	***
	[Submission]: {output}
	***
	[Criteria]: {criteria}
	***
	[END DATA]
	Does the submission meet the Criteria? First, write out in a step by step manner your reasoning about the criterion to be sure that your conclusion is correct. Avoid simply stating the correct answers at the outset. Then print only the single character "Y" or "N" (without quotes or punctuation) on its own line corresponding to the correct answer. At the end, repeat just the letter again by itself on a new line."""
	
```

## [/document_loaders/whatsapp_chat.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//document_loaders/whatsapp_chat.py#L29)
```python
	        message_line_regex = r"""
	            \[?
	            (
	                \d{1,4}
	                [\/.]
	                \d{1,2}
	                [\/.]
	                \d{1,4}
	                ,\s
	                \d{1,2}
	                :\d{2}
	                (?:
	                    :\d{2}
	                )?
	                (?:[\s_](?:AM|PM))?
	            )
	            \]?
	            [\s-]*
	            ([~\w\s]+)
	            [:]+
	            \s
	            (.+)
	        """
	
```

## [/graphs/neo4j_graph.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//graphs/neo4j_graph.py#L3)
```python
	node_properties_query = """
	CALL apoc.meta.data()
	YIELD label, other, elementType, type, property
	WHERE NOT type = "RELATIONSHIP" AND elementType = "node"
	WITH label AS nodeLabels, collect({property:property, type:type}) AS properties
	RETURN {labels: nodeLabels, properties: properties} AS output
	
	"""
	
```

## [/graphs/neo4j_graph.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//graphs/neo4j_graph.py#L12)
```python
	rel_properties_query = """
	CALL apoc.meta.data()
	YIELD label, other, elementType, type, property
	WHERE NOT type = "RELATIONSHIP" AND elementType = "relationship"
	WITH label AS nodeLabels, collect({property:property, type:type}) AS properties
	RETURN {type: nodeLabels, properties: properties} AS output
	"""
	
```

## [/graphs/neo4j_graph.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//graphs/neo4j_graph.py#L94)
```python
	        self.schema = f"""
	        Node properties are the following:
	        {[el['output'] for el in node_properties]}
	        Relationship properties are the following:
	        {[el['output'] for el in relationships_properties]}
	        The relationships are the following:
	        {[el['output'] for el in relationships]}
	        """
	
```

## [/chains/chat_vector_db/prompts.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/chat_vector_db/prompts.py#L4)
```python
	_template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.
	
	Chat History:
	{chat_history}
	Follow Up Input: {question}
	Standalone question:"""
	
```

## [/chains/chat_vector_db/prompts.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/chat_vector_db/prompts.py#L12)
```python
	prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
	
	{context}
	
	Question: {question}
	Helpful Answer:"""
	
```

## [/chains/hyde/prompts.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/hyde/prompts.py#L34)
```python
	mr_tydi_template = """Please write a passage in Swahili/Korean/Japanese/Bengali to answer the question in detail.
	Question: {QUESTION}
	Passage:"""
	
```

## [/chains/question_answering/map_reduce_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/question_answering/map_reduce_prompt.py#L10)
```python
	question_prompt_template = """Use the following portion of a long document to see if any of the text is relevant to answer the question. 
	Return any relevant text verbatim.
	{context}
	Question: {question}
	Relevant text, if any:"""
	
```

## [/chains/question_answering/map_reduce_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/question_answering/map_reduce_prompt.py#L18)
```python
	system_template = """Use the following portion of a long document to see if any of the text is relevant to answer the question. 
	Return any relevant text verbatim.
	______________________
	{context}"""
	
```

## [/chains/question_answering/map_reduce_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/question_answering/map_reduce_prompt.py#L33)
```python
	combine_prompt_template = """Given the following extracted parts of a long document and a question, create a final answer. 
	If you don't know the answer, just say that you don't know. Don't try to make up an answer.
	
	QUESTION: Which state/country's law governs the interpretation of the contract?
	=========
	Content: This Agreement is governed by English law and the parties submit to the exclusive jurisdiction of the English courts in  relation to any dispute (contractual or non-contractual) concerning this Agreement save that either party may apply to any court for an  injunction or other relief to protect its Intellectual Property Rights.
	
	Content: No Waiver. Failure or delay in exercising any right or remedy under this Agreement shall not constitute a waiver of such (or any other)  right or remedy.\n\n11.7 Severability. The invalidity, illegality or unenforceability of any term (or part of a term) of this Agreement shall not affect the continuation  in force of the remainder of the term (if any) and this Agreement.\n\n11.8 No Agency. Except as expressly stated otherwise, nothing in this Agreement shall create an agency, partnership or joint venture of any  kind between the parties.\n\n11.9 No Third-Party Beneficiaries.
	
	Content: (b) if Google believes, in good faith, that the Distributor has violated or caused Google to violate any Anti-Bribery Laws (as  defined in Clause 8.5) or that such a violation is reasonably likely to occur,
	=========
	FINAL ANSWER: This Agreement is governed by English law.
	
	QUESTION: What did the president say about Michael Jackson?
	=========
	Content: Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.  \n\nLast year COVID-19 kept us apart. This year we are finally together again. \n\nTonight, we meet as Democrats Republicans and Independents. But most importantly as Americans. \n\nWith a duty to one another to the American people to the Constitution. \n\nAnd with an unwavering resolve that freedom will always triumph over tyranny. \n\nSix days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways. But he badly miscalculated. \n\nHe thought he could roll into Ukraine and the world would roll over. Instead he met a wall of strength he never imagined. \n\nHe met the Ukrainian people. \n\nFrom President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world. \n\nGroups of citizens blocking tanks with their bodies. Everyone from students to retirees teachers turned soldiers defending their homeland.
	
	Content: And we won’t stop. \n\nWe have lost so much to COVID-19. Time with one another. And worst of all, so much loss of life. \n\nLet’s use this moment to reset. Let’s stop looking at COVID-19 as a partisan dividing line and see it for what it is: A God-awful disease.  \n\nLet’s stop seeing each other as enemies, and start seeing each other for who we really are: Fellow Americans.  \n\nWe can’t change how divided we’ve been. But we can change how we move forward—on COVID-19 and other issues we must face together. \n\nI recently visited the New York City Police Department days after the funerals of Officer Wilbert Mora and his partner, Officer Jason Rivera. \n\nThey were responding to a 9-1-1 call when a man shot and killed them with a stolen gun. \n\nOfficer Mora was 27 years old. \n\nOfficer Rivera was 22. \n\nBoth Dominican Americans who’d grown up on the same streets they later chose to patrol as police officers. \n\nI spoke with their families and told them that we are forever in debt for their sacrifice, and we will carry on their mission to restore the trust and safety every community deserves.
	
	Content: And a proud Ukrainian people, who have known 30 years  of independence, have repeatedly shown that they will not tolerate anyone who tries to take their country backwards.  \n\nTo all Americans, I will be honest with you, as I’ve always promised. A Russian dictator, invading a foreign country, has costs around the world. \n\nAnd I’m taking robust action to make sure the pain of our sanctions  is targeted at Russia’s economy. And I will use every tool at our disposal to protect American businesses and consumers. \n\nTonight, I can announce that the United States has worked with 30 other countries to release 60 Million barrels of oil from reserves around the world.  \n\nAmerica will lead that effort, releasing 30 Million barrels from our own Strategic Petroleum Reserve. And we stand ready to do more if necessary, unified with our allies.  \n\nThese steps will help blunt gas prices here at home. And I know the news about what’s happening can seem alarming. \n\nBut I want you to know that we are going to be okay.
	
	Content: More support for patients and families. \n\nTo get there, I call on Congress to fund ARPA-H, the Advanced Research Projects Agency for Health. \n\nIt’s based on DARPA—the Defense Department project that led to the Internet, GPS, and so much more.  \n\nARPA-H will have a singular purpose—to drive breakthroughs in cancer, Alzheimer’s, diabetes, and more. \n\nA unity agenda for the nation. \n\nWe can do this. \n\nMy fellow Americans—tonight , we have gathered in a sacred space—the citadel of our democracy. \n\nIn this Capitol, generation after generation, Americans have debated great questions amid great strife, and have done great things. \n\nWe have fought for freedom, expanded liberty, defeated totalitarianism and terror. \n\nAnd built the strongest, freest, and most prosperous nation the world has ever known. \n\nNow is the hour. \n\nOur moment of responsibility. \n\nOur test of resolve and conscience, of history itself. \n\nIt is in this moment that our character is formed. Our purpose is found. Our future is forged. \n\nWell I know this nation.
	=========
	FINAL ANSWER: The president did not mention Michael Jackson.
	
	QUESTION: {question}
	=========
	{summaries}
	=========
	FINAL ANSWER:"""
	
```

## [/chains/question_answering/map_reduce_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/question_answering/map_reduce_prompt.py#L67)
```python
	system_template = """Given the following extracted parts of a long document and a question, create a final answer. 
	If you don't know the answer, just say that you don't know. Don't try to make up an answer.
	______________________
	{summaries}"""
	
```

## [/chains/question_answering/map_rerank_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/question_answering/map_rerank_prompt.py#L10)
```python
	prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
	
	In addition to giving an answer, also return a score of how fully it answered the user's question. This should be in the following format:
	
	Question: [question here]
	Helpful Answer: [answer here]
	Score: [score between 0 and 100]
	
	How to determine the score:
	- Higher is a better answer
	- Better responds fully to the asked question, with sufficient level of detail
	- If you do not know the answer based on the context, that should be a score of 0
	- Don't be overconfident!
	
	Example #1
	
	Context:
	---------
	Apples are red
	---------
	Question: what color are apples?
	Helpful Answer: red
	Score: 100
	
	Example #2
	
	Context:
	---------
	it was night and the witness forgot his glasses. he was not sure if it was a sports car or an suv
	---------
	Question: what type was the car?
	Helpful Answer: a sports car or an suv
	Score: 60
	
	Example #3
	
	Context:
	---------
	Pears are either red or orange
	---------
	Question: what color are apples?
	Helpful Answer: This document does not answer the question
	Score: 0
	
	Begin!
	
	Context:
	---------
	{context}
	---------
	Question: {question}
	Helpful Answer:"""
	
```

## [/chains/question_answering/stuff_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/question_answering/stuff_prompt.py#L10)
```python
	prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
	
	{context}
	
	Question: {question}
	Helpful Answer:"""
	
```

## [/chains/question_answering/stuff_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/question_answering/stuff_prompt.py#L20)
```python
	system_template = """Use the following pieces of context to answer the users question. 
	If you don't know the answer, just say that you don't know, don't try to make up an answer.
	----------------
	{context}"""
	
```

## [/chains/openai_functions/extraction.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/openai_functions/extraction.py#L34)
```python
	_EXTRACTION_TEMPLATE = """Extract and save the relevant entities mentioned\
	 in the following passage together with their properties.
	
	Passage:
	{input}
	"""
	
```

## [/chains/sql_database/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/sql_database/prompt.py#L11)
```python
	_DEFAULT_TEMPLATE = """Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer. Unless the user specifies in his question a specific number of examples he wishes to obtain, always limit your query to at most {top_k} results. You can order the results by a relevant column to return the most interesting examples in the database.
	
	Never query for all the columns from a specific table, only ask for a the few relevant columns given the question.
	
	Pay attention to use only the column names that you can see in the schema description. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
	
	Use the following format:
	
	Question: Question here
	SQLQuery: SQL Query to run
	SQLResult: Result of the SQLQuery
	Answer: Final answer here
	
	"""
	
```

## [/chains/sql_database/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/sql_database/prompt.py#L32)
```python
	_DECIDER_TEMPLATE = """Given the below input question and list of potential tables, output a comma separated list of the table names that may be necessary to answer this question.
	
	Question: {query}
	
	Table Names: {table_names}
	
	Relevant Table Names:"""
	
```

## [/chains/sql_database/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/sql_database/prompt.py#L45)
```python
	_duckdb_prompt = """You are a DuckDB expert. Given an input question, first create a syntactically correct DuckDB query to run, then look at the results of the query and return the answer to the input question.
	Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per DuckDB. You can order the results to return the most informative data in the database.
	Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
	Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
	Pay attention to use today() function to get the current date, if the question involves "today".
	
	Use the following format:
	
	Question: Question here
	SQLQuery: SQL Query to run
	SQLResult: Result of the SQLQuery
	Answer: Final answer here
	
	"""
	
```

## [/chains/sql_database/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/sql_database/prompt.py#L65)
```python
	_googlesql_prompt = """You are a GoogleSQL expert. Given an input question, first create a syntactically correct GoogleSQL query to run, then look at the results of the query and return the answer to the input question.
	Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per GoogleSQL. You can order the results to return the most informative data in the database.
	Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
	Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
	Pay attention to use CURRENT_DATE() function to get the current date, if the question involves "today".
	
	Use the following format:
	
	Question: Question here
	SQLQuery: SQL Query to run
	SQLResult: Result of the SQLQuery
	Answer: Final answer here
	
	"""
	
```

## [/chains/sql_database/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/sql_database/prompt.py#L86)
```python
	_mssql_prompt = """You are an MS SQL expert. Given an input question, first create a syntactically correct MS SQL query to run, then look at the results of the query and return the answer to the input question.
	Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the TOP clause as per MS SQL. You can order the results to return the most informative data in the database.
	Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in square brackets ([]) to denote them as delimited identifiers.
	Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
	Pay attention to use CAST(GETDATE() as date) function to get the current date, if the question involves "today".
	
	Use the following format:
	
	Question: Question here
	SQLQuery: SQL Query to run
	SQLResult: Result of the SQLQuery
	Answer: Final answer here
	
	"""
	
```

## [/chains/sql_database/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/sql_database/prompt.py#L107)
```python
	_mysql_prompt = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
	Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
	Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
	Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
	Pay attention to use CURDATE() function to get the current date, if the question involves "today".
	
	Use the following format:
	
	Question: Question here
	SQLQuery: SQL Query to run
	SQLResult: Result of the SQLQuery
	Answer: Final answer here
	
	"""
	
```

## [/chains/sql_database/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/sql_database/prompt.py#L128)
```python
	_mariadb_prompt = """You are a MariaDB expert. Given an input question, first create a syntactically correct MariaDB query to run, then look at the results of the query and return the answer to the input question.
	Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MariaDB. You can order the results to return the most informative data in the database.
	Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
	Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
	Pay attention to use CURDATE() function to get the current date, if the question involves "today".
	
	Use the following format:
	
	Question: Question here
	SQLQuery: SQL Query to run
	SQLResult: Result of the SQLQuery
	Answer: Final answer here
	
	"""
	
```

## [/chains/sql_database/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/sql_database/prompt.py#L149)
```python
	_oracle_prompt = """You are an Oracle SQL expert. Given an input question, first create a syntactically correct Oracle SQL query to run, then look at the results of the query and return the answer to the input question.
	Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the FETCH FIRST n ROWS ONLY clause as per Oracle SQL. You can order the results to return the most informative data in the database.
	Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
	Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
	Pay attention to use TRUNC(SYSDATE) function to get the current date, if the question involves "today".
	
	Use the following format:
	
	Question: Question here
	SQLQuery: SQL Query to run
	SQLResult: Result of the SQLQuery
	Answer: Final answer here
	
	"""
	
```

## [/chains/sql_database/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/sql_database/prompt.py#L170)
```python
	_postgres_prompt = """You are a PostgreSQL expert. Given an input question, first create a syntactically correct PostgreSQL query to run, then look at the results of the query and return the answer to the input question.
	Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per PostgreSQL. You can order the results to return the most informative data in the database.
	Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
	Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
	Pay attention to use CURRENT_DATE function to get the current date, if the question involves "today".
	
	Use the following format:
	
	Question: Question here
	SQLQuery: SQL Query to run
	SQLResult: Result of the SQLQuery
	Answer: Final answer here
	
	"""
	
```

## [/chains/sql_database/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/sql_database/prompt.py#L191)
```python
	_sqlite_prompt = """You are a SQLite expert. Given an input question, first create a syntactically correct SQLite query to run, then look at the results of the query and return the answer to the input question.
	Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per SQLite. You can order the results to return the most informative data in the database.
	Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
	Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
	Pay attention to use date('now') function to get the current date, if the question involves "today".
	
	Use the following format:
	
	Question: Question here
	SQLQuery: SQL Query to run
	SQLResult: Result of the SQLQuery
	Answer: Final answer here
	
	"""
	
```

## [/chains/sql_database/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/sql_database/prompt.py#L211)
```python
	_clickhouse_prompt = """You are a ClickHouse expert. Given an input question, first create a syntactically correct Clic query to run, then look at the results of the query and return the answer to the input question.
	Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per ClickHouse. You can order the results to return the most informative data in the database.
	Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
	Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
	Pay attention to use today() function to get the current date, if the question involves "today".
	
	Use the following format:
	
	Question: "Question here"
	SQLQuery: "SQL Query to run"
	SQLResult: "Result of the SQLQuery"
	Answer: "Final answer here"
	
	"""
	
```

## [/chains/sql_database/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/sql_database/prompt.py#L231)
```python
	_prestodb_prompt = """You are a PrestoDB expert. Given an input question, first create a syntactically correct PrestoDB query to run, then look at the results of the query and return the answer to the input question.
	Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per PrestoDB. You can order the results to return the most informative data in the database.
	Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
	Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
	Pay attention to use current_date function to get the current date, if the question involves "today".
	
	Use the following format:
	
	Question: "Question here"
	SQLQuery: "SQL Query to run"
	SQLResult: "Result of the SQLQuery"
	Answer: "Final answer here"
	
	"""
	
```

## [/chains/retrieval_qa/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/retrieval_qa/prompt.py#L4)
```python
	prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
	
	{context}
	
	Question: {question}
	Helpful Answer:"""
	
```

## [/chains/qa_with_sources/map_reduce_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/qa_with_sources/map_reduce_prompt.py#L4)
```python
	question_prompt_template = """Use the following portion of a long document to see if any of the text is relevant to answer the question. 
	Return any relevant text verbatim.
	{context}
	Question: {question}
	Relevant text, if any:"""
	
```

## [/chains/qa_with_sources/map_reduce_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/qa_with_sources/map_reduce_prompt.py#L13)
```python
	combine_prompt_template = """Given the following extracted parts of a long document and a question, create a final answer with references ("SOURCES"). 
	If you don't know the answer, just say that you don't know. Don't try to make up an answer.
	ALWAYS return a "SOURCES" part in your answer.
	
	QUESTION: Which state/country's law governs the interpretation of the contract?
	=========
	Content: This Agreement is governed by English law and the parties submit to the exclusive jurisdiction of the English courts in  relation to any dispute (contractual or non-contractual) concerning this Agreement save that either party may apply to any court for an  injunction or other relief to protect its Intellectual Property Rights.
	Source: 28-pl
	Content: No Waiver. Failure or delay in exercising any right or remedy under this Agreement shall not constitute a waiver of such (or any other)  right or remedy.\n\n11.7 Severability. The invalidity, illegality or unenforceability of any term (or part of a term) of this Agreement shall not affect the continuation  in force of the remainder of the term (if any) and this Agreement.\n\n11.8 No Agency. Except as expressly stated otherwise, nothing in this Agreement shall create an agency, partnership or joint venture of any  kind between the parties.\n\n11.9 No Third-Party Beneficiaries.
	Source: 30-pl
	Content: (b) if Google believes, in good faith, that the Distributor has violated or caused Google to violate any Anti-Bribery Laws (as  defined in Clause 8.5) or that such a violation is reasonably likely to occur,
	Source: 4-pl
	=========
	FINAL ANSWER: This Agreement is governed by English law.
	SOURCES: 28-pl
	
	QUESTION: What did the president say about Michael Jackson?
	=========
	Content: Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.  \n\nLast year COVID-19 kept us apart. This year we are finally together again. \n\nTonight, we meet as Democrats Republicans and Independents. But most importantly as Americans. \n\nWith a duty to one another to the American people to the Constitution. \n\nAnd with an unwavering resolve that freedom will always triumph over tyranny. \n\nSix days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways. But he badly miscalculated. \n\nHe thought he could roll into Ukraine and the world would roll over. Instead he met a wall of strength he never imagined. \n\nHe met the Ukrainian people. \n\nFrom President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world. \n\nGroups of citizens blocking tanks with their bodies. Everyone from students to retirees teachers turned soldiers defending their homeland.
	Source: 0-pl
	Content: And we won’t stop. \n\nWe have lost so much to COVID-19. Time with one another. And worst of all, so much loss of life. \n\nLet’s use this moment to reset. Let’s stop looking at COVID-19 as a partisan dividing line and see it for what it is: A God-awful disease.  \n\nLet’s stop seeing each other as enemies, and start seeing each other for who we really are: Fellow Americans.  \n\nWe can’t change how divided we’ve been. But we can change how we move forward—on COVID-19 and other issues we must face together. \n\nI recently visited the New York City Police Department days after the funerals of Officer Wilbert Mora and his partner, Officer Jason Rivera. \n\nThey were responding to a 9-1-1 call when a man shot and killed them with a stolen gun. \n\nOfficer Mora was 27 years old. \n\nOfficer Rivera was 22. \n\nBoth Dominican Americans who’d grown up on the same streets they later chose to patrol as police officers. \n\nI spoke with their families and told them that we are forever in debt for their sacrifice, and we will carry on their mission to restore the trust and safety every community deserves.
	Source: 24-pl
	Content: And a proud Ukrainian people, who have known 30 years  of independence, have repeatedly shown that they will not tolerate anyone who tries to take their country backwards.  \n\nTo all Americans, I will be honest with you, as I’ve always promised. A Russian dictator, invading a foreign country, has costs around the world. \n\nAnd I’m taking robust action to make sure the pain of our sanctions  is targeted at Russia’s economy. And I will use every tool at our disposal to protect American businesses and consumers. \n\nTonight, I can announce that the United States has worked with 30 other countries to release 60 Million barrels of oil from reserves around the world.  \n\nAmerica will lead that effort, releasing 30 Million barrels from our own Strategic Petroleum Reserve. And we stand ready to do more if necessary, unified with our allies.  \n\nThese steps will help blunt gas prices here at home. And I know the news about what’s happening can seem alarming. \n\nBut I want you to know that we are going to be okay.
	Source: 5-pl
	Content: More support for patients and families. \n\nTo get there, I call on Congress to fund ARPA-H, the Advanced Research Projects Agency for Health. \n\nIt’s based on DARPA—the Defense Department project that led to the Internet, GPS, and so much more.  \n\nARPA-H will have a singular purpose—to drive breakthroughs in cancer, Alzheimer’s, diabetes, and more. \n\nA unity agenda for the nation. \n\nWe can do this. \n\nMy fellow Americans—tonight , we have gathered in a sacred space—the citadel of our democracy. \n\nIn this Capitol, generation after generation, Americans have debated great questions amid great strife, and have done great things. \n\nWe have fought for freedom, expanded liberty, defeated totalitarianism and terror. \n\nAnd built the strongest, freest, and most prosperous nation the world has ever known. \n\nNow is the hour. \n\nOur moment of responsibility. \n\nOur test of resolve and conscience, of history itself. \n\nIt is in this moment that our character is formed. Our purpose is found. Our future is forged. \n\nWell I know this nation.
	Source: 34-pl
	=========
	FINAL ANSWER: The president did not mention Michael Jackson.
	SOURCES:
	
	QUESTION: {question}
	=========
	{summaries}
	=========
	FINAL ANSWER:"""
	
```

## [/chains/qa_with_sources/stuff_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/qa_with_sources/stuff_prompt.py#L4)
```python
	template = """Given the following extracted parts of a long document and a question, create a final answer with references ("SOURCES"). 
	If you don't know the answer, just say that you don't know. Don't try to make up an answer.
	ALWAYS return a "SOURCES" part in your answer.
	
	QUESTION: Which state/country's law governs the interpretation of the contract?
	=========
	Content: This Agreement is governed by English law and the parties submit to the exclusive jurisdiction of the English courts in  relation to any dispute (contractual or non-contractual) concerning this Agreement save that either party may apply to any court for an  injunction or other relief to protect its Intellectual Property Rights.
	Source: 28-pl
	Content: No Waiver. Failure or delay in exercising any right or remedy under this Agreement shall not constitute a waiver of such (or any other)  right or remedy.\n\n11.7 Severability. The invalidity, illegality or unenforceability of any term (or part of a term) of this Agreement shall not affect the continuation  in force of the remainder of the term (if any) and this Agreement.\n\n11.8 No Agency. Except as expressly stated otherwise, nothing in this Agreement shall create an agency, partnership or joint venture of any  kind between the parties.\n\n11.9 No Third-Party Beneficiaries.
	Source: 30-pl
	Content: (b) if Google believes, in good faith, that the Distributor has violated or caused Google to violate any Anti-Bribery Laws (as  defined in Clause 8.5) or that such a violation is reasonably likely to occur,
	Source: 4-pl
	=========
	FINAL ANSWER: This Agreement is governed by English law.
	SOURCES: 28-pl
	
	QUESTION: What did the president say about Michael Jackson?
	=========
	Content: Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.  \n\nLast year COVID-19 kept us apart. This year we are finally together again. \n\nTonight, we meet as Democrats Republicans and Independents. But most importantly as Americans. \n\nWith a duty to one another to the American people to the Constitution. \n\nAnd with an unwavering resolve that freedom will always triumph over tyranny. \n\nSix days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways. But he badly miscalculated. \n\nHe thought he could roll into Ukraine and the world would roll over. Instead he met a wall of strength he never imagined. \n\nHe met the Ukrainian people. \n\nFrom President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world. \n\nGroups of citizens blocking tanks with their bodies. Everyone from students to retirees teachers turned soldiers defending their homeland.
	Source: 0-pl
	Content: And we won’t stop. \n\nWe have lost so much to COVID-19. Time with one another. And worst of all, so much loss of life. \n\nLet’s use this moment to reset. Let’s stop looking at COVID-19 as a partisan dividing line and see it for what it is: A God-awful disease.  \n\nLet’s stop seeing each other as enemies, and start seeing each other for who we really are: Fellow Americans.  \n\nWe can’t change how divided we’ve been. But we can change how we move forward—on COVID-19 and other issues we must face together. \n\nI recently visited the New York City Police Department days after the funerals of Officer Wilbert Mora and his partner, Officer Jason Rivera. \n\nThey were responding to a 9-1-1 call when a man shot and killed them with a stolen gun. \n\nOfficer Mora was 27 years old. \n\nOfficer Rivera was 22. \n\nBoth Dominican Americans who’d grown up on the same streets they later chose to patrol as police officers. \n\nI spoke with their families and told them that we are forever in debt for their sacrifice, and we will carry on their mission to restore the trust and safety every community deserves.
	Source: 24-pl
	Content: And a proud Ukrainian people, who have known 30 years  of independence, have repeatedly shown that they will not tolerate anyone who tries to take their country backwards.  \n\nTo all Americans, I will be honest with you, as I’ve always promised. A Russian dictator, invading a foreign country, has costs around the world. \n\nAnd I’m taking robust action to make sure the pain of our sanctions  is targeted at Russia’s economy. And I will use every tool at our disposal to protect American businesses and consumers. \n\nTonight, I can announce that the United States has worked with 30 other countries to release 60 Million barrels of oil from reserves around the world.  \n\nAmerica will lead that effort, releasing 30 Million barrels from our own Strategic Petroleum Reserve. And we stand ready to do more if necessary, unified with our allies.  \n\nThese steps will help blunt gas prices here at home. And I know the news about what’s happening can seem alarming. \n\nBut I want you to know that we are going to be okay.
	Source: 5-pl
	Content: More support for patients and families. \n\nTo get there, I call on Congress to fund ARPA-H, the Advanced Research Projects Agency for Health. \n\nIt’s based on DARPA—the Defense Department project that led to the Internet, GPS, and so much more.  \n\nARPA-H will have a singular purpose—to drive breakthroughs in cancer, Alzheimer’s, diabetes, and more. \n\nA unity agenda for the nation. \n\nWe can do this. \n\nMy fellow Americans—tonight , we have gathered in a sacred space—the citadel of our democracy. \n\nIn this Capitol, generation after generation, Americans have debated great questions amid great strife, and have done great things. \n\nWe have fought for freedom, expanded liberty, defeated totalitarianism and terror. \n\nAnd built the strongest, freest, and most prosperous nation the world has ever known. \n\nNow is the hour. \n\nOur moment of responsibility. \n\nOur test of resolve and conscience, of history itself. \n\nIt is in this moment that our character is formed. Our purpose is found. Our future is forged. \n\nWell I know this nation.
	Source: 34-pl
	=========
	FINAL ANSWER: The president did not mention Michael Jackson.
	SOURCES:
	
	QUESTION: {question}
	=========
	{summaries}
	=========
	FINAL ANSWER:"""
	
```

## [/chains/graph_qa/prompts.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/graph_qa/prompts.py#L4)
```python
	_DEFAULT_ENTITY_EXTRACTION_TEMPLATE = """Extract all entities from the following text. As a guideline, a proper noun is generally capitalized. You should definitely extract all names and places.
	
	Return the output as a single comma-separated list, or NONE if there is nothing of note to return.
	
	EXAMPLE
	i'm trying to improve Langchain's interfaces, the UX, its integrations with various products the user might want ... a lot of stuff.
	Output: Langchain
	END OF EXAMPLE
	
	EXAMPLE
	i'm trying to improve Langchain's interfaces, the UX, its integrations with various products the user might want ... a lot of stuff. I'm working with Sam.
	Output: Langchain, Sam
	END OF EXAMPLE
	
	Begin!
	
	{input}
	Output:"""
	
```

## [/chains/graph_qa/prompts.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/graph_qa/prompts.py#L26)
```python
	prompt_template = """Use the following knowledge triplets to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
	
	{context}
	
	Question: {question}
	Helpful Answer:"""
	
```

## [/chains/graph_qa/prompts.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/graph_qa/prompts.py#L36)
```python
	CYPHER_GENERATION_TEMPLATE = """Task:Generate Cypher statement to query a graph database.
	Instructions:
	Use only the provided relationship types and properties in the schema.
	Do not use any other relationship types or properties that are not provided.
	Schema:
	{schema}
	Note: Do not include any explanations or apologies in your responses.
	Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
	Do not include any text except the generated Cypher statement.
	
	The question is:
	{question}"""
	
```

## [/chains/graph_qa/prompts.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/graph_qa/prompts.py#L92)
```python
	CYPHER_QA_TEMPLATE = """You are an assistant that helps to form nice and human understandable answers.
	The information part contains the provided information that you must use to construct an answer.
	The provided information is authorative, you must never doubt it or try to use your internal knowledge to correct it.
	Make the answer sound as a response to the question. Do not mention that you based the result on the given information.
	If the provided information is empty, say that you don't know the answer.
	Information:
	{context}
	
	Question: {question}
	Helpful Answer:"""
	
```

## [/chains/qa_generation/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/qa_generation/prompt.py#L10)
```python
	templ1 = """You are a smart assistant designed to help high school teachers come up with reading comprehension questions.
	Given a piece of text, you must come up with a question and answer pair that can be used to test a student's reading comprehension abilities.
	When coming up with this question/answer pair, you must respond in the following format:
	```
	{{
	    "question": "$YOUR_QUESTION_HERE",
	    "answer": "$THE_ANSWER_HERE"
	}}
	```
	
	Everything between the ``` must be valid json.
	"""
	
```

## [/chains/qa_generation/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/qa_generation/prompt.py#L22)
```python
	templ2 = """Please come up with a question/answer pair, in the specified JSON format, for the following text:
	----------------
	{text}"""
	
```

## [/chains/qa_generation/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/qa_generation/prompt.py#L31)
```python
	templ = """You are a smart assistant designed to help high school teachers come up with reading comprehension questions.
	Given a piece of text, you must come up with a question and answer pair that can be used to test a student's reading comprehension abilities.
	When coming up with this question/answer pair, you must respond in the following format:
	```
	{{
	    "question": "$YOUR_QUESTION_HERE",
	    "answer": "$THE_ANSWER_HERE"
	}}
	```
	
	Everything between the ``` must be valid json.
	
	Please come up with a question/answer pair, in the specified JSON format, for the following text:
	----------------
	{text}"""
	
```

## [/chains/constitutional_ai/prompts.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/constitutional_ai/prompts.py#L8)
```python
	    template="""Human: {input_prompt}
	
	Model: {output_from_model}
	
	Critique Request: {critique_request}
	
	Critique: {critique}""",
	
```

## [/chains/constitutional_ai/prompts.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/constitutional_ai/prompts.py#L64)
```python
	    suffix="""Human: {input_prompt}
	Model: {output_from_model}
	
	Critique Request: {critique_request}
	
	Critique:""",
	
```

## [/chains/constitutional_ai/prompts.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/constitutional_ai/prompts.py#L78)
```python
	    suffix="""Human: {input_prompt}
	
	Model: {output_from_model}
	
	Critique Request: {critique_request}
	
	Critique: {critique}
	
	If the critique does not identify anything worth changing, ignore the Revision Request and do not make any revisions. Instead, return "No revisions needed".
	
	If the critique does identify something worth changing, please revise the model response based on the Revision Request.
	
	Revision Request: {revision_request}
	
	Revision:""",
	
```

## [/chains/natbot/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/natbot/prompt.py#L4)
```python
	_PROMPT_TEMPLATE = """
	You are an agents controlling a browser. You are given:
	
		(1) an objective that you are trying to achieve
		(2) the URL of your current web page
		(3) a simplified text description of what's visible in the browser window (more on that below)
	
	You can issue these commands:
		SCROLL UP - scroll up one page
		SCROLL DOWN - scroll down one page
		CLICK X - click on a given element. You can only click on links, buttons, and inputs!
		TYPE X "TEXT" - type the specified text into the input with id X
		TYPESUBMIT X "TEXT" - same as TYPE above, except then it presses ENTER to submit the form
	
	The format of the browser content is highly simplified; all formatting elements are stripped.
	Interactive elements such as links, inputs, buttons are represented like this:
	
			<link id=1>text</link>
			<button id=2>text</button>
			<input id=3>text</input>
	
	Images are rendered as their alt text like this:
	
			<img id=4 alt=""/>
	
	Based on your given objective, issue whatever command you believe will get you closest to achieving your goal.
	You always start on Google; you should submit a search query to Google that will take you to the best page for
	achieving your objective. And then interact with that page to achieve your objective.
	
	If you find yourself on Google and there are no search results displayed yet, you should probably issue a command
	like "TYPESUBMIT 7 "search query"" to get to a more useful page.
	
	Then, if you find yourself on a Google search results page, you might issue the command "CLICK 24" to click
	on the first link in the search results. (If your previous command was a TYPESUBMIT your next command should
	probably be a CLICK.)
	
	Don't try to interact with elements that you can't see.
	
	Here are some examples:
	
	EXAMPLE 1:
	==================================================
	CURRENT BROWSER CONTENT:
	------------------
	<link id=1>About</link>
	<link id=2>Store</link>
	<link id=3>Gmail</link>
	<link id=4>Images</link>
	<link id=5>(Google apps)</link>
	<link id=6>Sign in</link>
	<img id=7 alt="(Google)"/>
	<input id=8 alt="Search"></input>
	<button id=9>(Search by voice)</button>
	<button id=10>(Google Search)</button>
	<button id=11>(I'm Feeling Lucky)</button>
	<link id=12>Advertising</link>
	<link id=13>Business</link>
	<link id=14>How Search works</link>
	<link id=15>Carbon neutral since 2007</link>
	<link id=16>Privacy</link>
	<link id=17>Terms</link>
	<text id=18>Settings</text>
	------------------
	OBJECTIVE: Find a 2 bedroom house for sale in Anchorage AK for under $750k
	CURRENT URL: https://www.google.com/
	YOUR COMMAND:
	TYPESUBMIT 8 "anchorage redfin"
	==================================================
	
	EXAMPLE 2:
	==================================================
	CURRENT BROWSER CONTENT:
	------------------
	<link id=1>About</link>
	<link id=2>Store</link>
	<link id=3>Gmail</link>
	<link id=4>Images</link>
	<link id=5>(Google apps)</link>
	<link id=6>Sign in</link>
	<img id=7 alt="(Google)"/>
	<input id=8 alt="Search"></input>
	<button id=9>(Search by voice)</button>
	<button id=10>(Google Search)</button>
	<button id=11>(I'm Feeling Lucky)</button>
	<link id=12>Advertising</link>
	<link id=13>Business</link>
	<link id=14>How Search works</link>
	<link id=15>Carbon neutral since 2007</link>
	<link id=16>Privacy</link>
	<link id=17>Terms</link>
	<text id=18>Settings</text>
	------------------
	OBJECTIVE: Make a reservation for 4 at Dorsia at 8pm
	CURRENT URL: https://www.google.com/
	YOUR COMMAND:
	TYPESUBMIT 8 "dorsia nyc opentable"
	==================================================
	
	EXAMPLE 3:
	==================================================
	CURRENT BROWSER CONTENT:
	------------------
	<button id=1>For Businesses</button>
	<button id=2>Mobile</button>
	<button id=3>Help</button>
	<button id=4 alt="Language Picker">EN</button>
	<link id=5>OpenTable logo</link>
	<button id=6 alt ="search">Search</button>
	<text id=7>Find your table for any occasion</text>
	<button id=8>(Date selector)</button>
	<text id=9>Sep 28, 2022</text>
	<text id=10>7:00 PM</text>
	<text id=11>2 people</text>
	<input id=12 alt="Location, Restaurant, or Cuisine"></input>
	<button id=13>Let’s go</button>
	<text id=14>It looks like you're in Peninsula. Not correct?</text>
	<button id=15>Get current location</button>
	<button id=16>Next</button>
	------------------
	OBJECTIVE: Make a reservation for 4 for dinner at Dorsia in New York City at 8pm
	CURRENT URL: https://www.opentable.com/
	YOUR COMMAND:
	TYPESUBMIT 12 "dorsia new york city"
	==================================================
	
	The current browser content, objective, and current URL follow. Reply with your next command to the browser.
	
	CURRENT BROWSER CONTENT:
	------------------
	{browser_content}
	------------------
	
	OBJECTIVE: {objective}
	CURRENT URL: {url}
	PREVIOUS COMMAND: {previous_command}
	YOUR COMMAND:
	"""
	
```

## [/chains/natbot/crawler.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/natbot/crawler.py#L85)
```python
	        js = """
			links = document.getElementsByTagName("a");
			for (var i = 0; i < links.length; i++) {
				links[i].removeAttribute("target");
			}
			"""
	
```

## [/chains/api/tmdb_docs.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/api/tmdb_docs.py#L2)
```python
	TMDB_DOCS = """API documentation:
	Endpoint: https://api.themoviedb.org/3
	GET /search/movie
	
	This API is for searching movies.
	
	Query parameters table:
	language | string | Pass a ISO 639-1 value to display translated data for the fields that support it. minLength: 2, pattern: ([a-z]{2})-([A-Z]{2}), default: en-US | optional
	query | string | Pass a text query to search. This value should be URI encoded. minLength: 1 | required
	page | integer | Specify which page to query. minimum: 1, maximum: 1000, default: 1 | optional
	include_adult | boolean | Choose whether to inlcude adult (pornography) content in the results. default | optional
	region | string | Specify a ISO 3166-1 code to filter release dates. Must be uppercase. pattern: ^[A-Z]{2}$ | optional
	year | integer  | optional
	primary_release_year | integer | optional
	
	Response schema (JSON object):
	page | integer | optional
	total_results | integer | optional
	total_pages | integer | optional
	results | array[object] (Movie List Result Object)
	
	Each object in the "results" key has the following schema:
	poster_path | string or null | optional
	adult | boolean | optional
	overview | string | optional
	release_date | string | optional
	genre_ids | array[integer] | optional
	id | integer | optional
	original_title | string | optional
	original_language | string | optional
	title | string | optional
	backdrop_path | string or null | optional
	popularity | number | optional
	vote_count | integer | optional
	video | boolean | optional
	vote_average | number | optional"""
	
```

## [/chains/api/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/api/prompt.py#L4)
```python
	API_URL_PROMPT_TEMPLATE = """You are given the below API Documentation:
	{api_docs}
	Using this documentation, generate the full API url to call for answering the user question.
	You should build the API url in order to get a response that is as short as possible, while still getting the necessary information to answer the question. Pay attention to deliberately exclude any unnecessary pieces of data in the API call.
	
	Question:{question}
	API url:"""
	
```

## [/chains/api/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/api/prompt.py#L22)
```python
	    + """ {api_url}
	
	Here is the response from the API:
	
	{api_response}
	
	Summarize this response to answer the original question.
	
	Summary:"""
	
```

## [/chains/api/openapi/prompts.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/api/openapi/prompts.py#L2)
```python
	REQUEST_TEMPLATE = """You are a helpful AI Assistant. Please provide JSON arguments to agentFunc() based on the user's instructions.
	
	API_SCHEMA: ```typescript
	{schema}
	```
	
	USER_INSTRUCTIONS: "{instructions}"
	
	Your arguments must be plain json provided in a markdown block:
	
	ARGS: ```json
	{{valid json conforming to API_SCHEMA}}
	```
	
	Example
	-----
	
	ARGS: ```json
	{{"foo": "bar", "baz": {{"qux": "quux"}}}}
	```
	
	The block must be no more than 1 line long, and all arguments must be valid JSON. All string arguments must be wrapped in double quotes.
	You MUST strictly comply to the types indicated by the provided schema, including all required args.
	
	If you don't have sufficient information to call the function due to things like requiring specific uuid's, you can reply with the following message:
	
	Message: ```text
	Concise response requesting the additional information that would make calling the function successful.
	```
	
	Begin
	-----
	ARGS:
	"""
	
```

## [/chains/api/openapi/prompts.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/api/openapi/prompts.py#L36)
```python
	RESPONSE_TEMPLATE = """You are a helpful AI assistant trained to answer user queries from API responses.
	You attempted to call an API, which resulted in:
	API_RESPONSE: {response}
	
	USER_COMMENT: "{instructions}"
	
	
	If the API_RESPONSE can answer the USER_COMMENT respond with the following markdown json block:
	Response: ```json
	{{"response": "Human-understandable synthesis of the API_RESPONSE"}}
	```
	
	Otherwise respond with the following markdown json block:
	Response Error: ```json
	{{"response": "What you did and a concise statement of the resulting error. If it can be easily fixed, provide a suggestion."}}
	```
	
	You MUST respond as a markdown json code block. The person you are responding to CANNOT see the API_RESPONSE, so if there is any relevant information there you must include it in your response.
	
	Begin:
	---
	"""
	
```

## [/chains/llm_checker/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/llm_checker/prompt.py#L9)
```python
	_LIST_ASSERTIONS_TEMPLATE = """Here is a statement:
	{statement}
	Make a bullet point list of the assumptions you made when producing the above statement.\n\n"""
	
```

## [/chains/llm_checker/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/llm_checker/prompt.py#L16)
```python
	_CHECK_ASSERTIONS_TEMPLATE = """Here is a bullet point list of assertions:
	{assertions}
	For each assertion, determine whether it is true or false. If it is false, explain why.\n\n"""
	
```

## [/chains/llm_checker/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/llm_checker/prompt.py#L23)
```python
	_REVISED_ANSWER_TEMPLATE = """{checked_assertions}
	
	Question: In light of the above assertions and checks, how would you answer the question '{question}'?
	
	Answer:"""
	
```

## [/chains/llm_bash/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/llm_bash/prompt.py#L10)
```python
	_PROMPT_TEMPLATE = """If someone asks you to perform a task, your job is to come up with a series of bash commands that will perform the task. There is no need to put "#!/bin/bash" in your answer. Make sure to reason step by step, using this format:
	
	Question: "copy the files in the directory named 'target' into a new directory at the same level as target called 'myNewDirectory'"
	
	I need to take the following actions:
	- List all files in the directory
	- Create a new directory
	- Copy the files from the first directory into the second directory
	```bash
	ls
	mkdir myNewDirectory
	cp -r target/* myNewDirectory
	```
	
	That is the format. Begin!
	
	Question: {question}"""
	
```

## [/chains/llm_math/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/llm_math/prompt.py#L4)
```python
	_PROMPT_TEMPLATE = """Translate a math problem into a expression that can be executed using Python's numexpr library. Use the output of running this code to answer the question.
	
	Question: ${{Question with math problem.}}
	```text
	${{single line mathematical expression that solves the problem}}
	```
	...numexpr.evaluate(text)...
	```output
	${{Output of running the code}}
	```
	Answer: ${{Answer}}
	
	Begin.
	
	Question: What is 37593 * 67?
	```text
	37593 * 67
	```
	...numexpr.evaluate("37593 * 67")...
	```output
	2518731
	```
	Answer: 2518731
	
	Question: 37593^(1/5)
	```text
	37593**(1/5)
	```
	...numexpr.evaluate("37593**(1/5)")...
	```output
	8.222831614237718
	```
	Answer: 8.222831614237718
	
	Question: {question}
	"""
	
```

## [/chains/query_constructor/parser.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/query_constructor/parser.py#L29)
```python
	GRAMMAR = """
	    ?program: func_call
	    ?expr: func_call
	        | value
	
	    func_call: CNAME "(" [args] ")"
	
	    ?value: SIGNED_INT -> int
	        | SIGNED_FLOAT -> float
	        | TIMESTAMP -> timestamp
	        | list
	        | string
	        | ("false" | "False" | "FALSE") -> false
	        | ("true" | "True" | "TRUE") -> true
	
	    args: expr ("," expr)*
	    TIMESTAMP.2: /["'](\d{4}-[01]\d-[0-3]\d)["']/
	    string: /'[^']*'/ | ESCAPED_STRING
	    list: "[" [args] "]"
	
	    %import common.CNAME
	    %import common.ESCAPED_STRING
	    %import common.SIGNED_FLOAT
	    %import common.SIGNED_INT
	    %import common.WS
	    %ignore WS
	"""
	
```

## [/chains/query_constructor/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/query_constructor/prompt.py#L4)
```python
	SONG_DATA_SOURCE = """\
	```json
	{
	    "content": "Lyrics of a song",
	    "attributes": {
	        "artist": {
	            "type": "string",
	            "description": "Name of the song artist"
	        },
	        "length": {
	            "type": "integer",
	            "description": "Length of the song in seconds"
	        },
	        "genre": {
	            "type": "string",
	            "description": "The song genre, one of \"pop\", \"rock\" or \"rap\""
	        }
	    }
	}
	```\
	""".replace(
	
```

## [/chains/query_constructor/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/query_constructor/prompt.py#L30)
```python
	FULL_ANSWER = """\
	```json
	{{
	    "query": "teenager love",
	    "filter": "and(or(eq(\\"artist\\", \\"Taylor Swift\\"), eq(\\"artist\\", \\"Katy Perry\\")), \
	lt(\\"length\\", 180), eq(\\"genre\\", \\"pop\\"))"
	}}
	```\
	"""
	
```

## [/chains/query_constructor/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/query_constructor/prompt.py#L95)
```python
	EXAMPLE_PROMPT_TEMPLATE = """\
	<< Example {i}. >>
	Data Source:
	{data_source}
	
	User Query:
	{user_query}
	
	Structured Request:
	{structured_request}
	"""
	
```

## [/chains/query_constructor/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/query_constructor/prompt.py#L113)
```python
	DEFAULT_SCHEMA = """\
	<< Structured Request Schema >>
	When responding use a markdown code snippet with a JSON object formatted in the \
	following schema:
	
	```json
	{{{{
	    "query": string \\ text string to compare to document contents
	    "filter": string \\ logical condition statement for filtering documents
	}}}}
	```
	
	The query string should contain only text that is expected to match the contents of \
	documents. Any conditions in the filter should not be mentioned in the query as well.
	
	A logical condition statement is composed of one or more comparison and logical \
	operation statements.
	
	A comparison statement takes the form: `comp(attr, val)`:
	- `comp` ({allowed_comparators}): comparator
	- `attr` (string):  name of attribute to apply the comparison to
	- `val` (string): is the comparison value
	
	A logical operation statement takes the form `op(statement1, statement2, ...)`:
	- `op` ({allowed_operators}): logical operator
	- `statement1`, `statement2`, ... (comparison statements or logical operation \
	statements): one or more statements to apply the operation to
	
	Make sure that you only use the comparators and logical operators listed above and \
	no others.
	Make sure that filters only refer to attributes that exist in the data source.
	Make sure that filters only use the attributed names with its function names if there are functions applied on them.
	Make sure that filters only use format `YYYY-MM-DD` when handling timestamp data typed values.
	Make sure that filters take into account the descriptions of attributes and only make \
	comparisons that are feasible given the type of data being stored.
	Make sure that filters are only used as needed. If there are no filters that should be \
	applied return "NO_FILTER" for the filter value.\
	"""
	
```

## [/chains/query_constructor/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/query_constructor/prompt.py#L152)
```python
	SCHEMA_WITH_LIMIT = """\
	<< Structured Request Schema >>
	When responding use a markdown code snippet with a JSON object formatted in the \
	following schema:
	
	```json
	{{{{
	    "query": string \\ text string to compare to document contents
	    "filter": string \\ logical condition statement for filtering documents
	    "limit": int \\ the number of documents to retrieve
	}}}}
	```
	
	The query string should contain only text that is expected to match the contents of \
	documents. Any conditions in the filter should not be mentioned in the query as well.
	
	A logical condition statement is composed of one or more comparison and logical \
	operation statements.
	
	A comparison statement takes the form: `comp(attr, val)`:
	- `comp` ({allowed_comparators}): comparator
	- `attr` (string):  name of attribute to apply the comparison to
	- `val` (string): is the comparison value
	
	A logical operation statement takes the form `op(statement1, statement2, ...)`:
	- `op` ({allowed_operators}): logical operator
	- `statement1`, `statement2`, ... (comparison statements or logical operation \
	statements): one or more statements to apply the operation to
	
	Make sure that you only use the comparators and logical operators listed above and \
	no others.
	Make sure that filters only refer to attributes that exist in the data source.
	Make sure that filters only use the attributed names with its function names if there are functions applied on them.
	Make sure that filters only use format `YYYY-MM-DD` when handling timestamp data typed values.
	Make sure that filters take into account the descriptions of attributes and only make \
	comparisons that are feasible given the type of data being stored.
	Make sure that filters are only used as needed. If there are no filters that should be \
	applied return "NO_FILTER" for the filter value.
	Make sure the `limit` is always an int value. It is an optional parameter so leave it blank if it is does not make sense.
	"""
	
```

## [/chains/query_constructor/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/query_constructor/prompt.py#L193)
```python
	DEFAULT_PREFIX = """\
	Your goal is to structure the user's query to match the request schema provided below.
	
	{schema}\
	"""
	
```

## [/chains/query_constructor/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/query_constructor/prompt.py#L199)
```python
	DEFAULT_SUFFIX = """\
	<< Example {i}. >>
	Data Source:
	```json
	{{{{
	    "content": "{content}",
	    "attributes": {attributes}
	}}}}
	```
	
	User Query:
	{{query}}
	
	Structured Request:
	"""
	
```

## [/chains/conversational_retrieval/prompts.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/conversational_retrieval/prompts.py#L4)
```python
	_template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question, in its original language.
	
	Chat History:
	{chat_history}
	Follow Up Input: {question}
	Standalone question:"""
	
```

## [/chains/conversational_retrieval/prompts.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/conversational_retrieval/prompts.py#L12)
```python
	prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
	
	{context}
	
	Question: {question}
	Helpful Answer:"""
	
```

## [/chains/flare/prompts.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/flare/prompts.py#L16)
```python
	PROMPT_TEMPLATE = """\
	Respond to the user message using any relevant context. \
	If context is provided, you should ground your answer in that context. \
	Once you're done responding return FINISHED.
	
	>>> CONTEXT: {context}
	>>> USER INPUT: {user_input}
	>>> RESPONSE: {response}\
	"""
	
```

## [/chains/flare/prompts.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/flare/prompts.py#L32)
```python
	QUESTION_GENERATOR_PROMPT_TEMPLATE = """\
	Given a user input and an existing partial response as context, \
	ask a question to which the answer is the given term/entity/phrase:
	
	>>> USER INPUT: {user_input}
	>>> EXISTING PARTIAL RESPONSE: {current_response}
	
	The question to which the answer is the term/entity/phrase "{uncertain_span}" is:"""
	
```

## [/chains/conversation/prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/conversation/prompt.py#L11)
```python
	DEFAULT_TEMPLATE = """The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.
	
	Current conversation:
	{history}
	Human: {input}
	AI:"""
	
```

## [/chains/router/multi_prompt_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/router/multi_prompt_prompt.py#L3)
```python
	MULTI_PROMPT_ROUTER_TEMPLATE = """\
	Given a raw text input to a language model select the model prompt best suited for \
	the input. You will be given the names of the available prompts and a description of \
	what the prompt is best suited for. You may also revise the original input if you \
	think that revising it will ultimately lead to a better response from the language \
	model.
	
	<< FORMATTING >>
	Return a markdown code snippet with a JSON object formatted to look like:
	```json
	{{{{
	    "destination": string \\ name of the prompt to use or "DEFAULT"
	    "next_inputs": string \\ a potentially modified version of the original input
	}}}}
	```
	
	REMEMBER: "destination" MUST be one of the candidate prompt names specified below OR \
	it can be "DEFAULT" if the input is not well suited for any of the candidate prompts.
	REMEMBER: "next_inputs" can just be the original input if you don't think any \
	modifications are needed.
	
	<< CANDIDATE PROMPTS >>
	{destinations}
	
	<< INPUT >>
	{{input}}
	
	<< OUTPUT >>
	"""
	
```

## [/chains/router/multi_retrieval_prompt.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//chains/router/multi_retrieval_prompt.py#L3)
```python
	MULTI_RETRIEVAL_ROUTER_TEMPLATE = """\
	Given a query to a question answering system select the system best suited \
	for the input. You will be given the names of the available systems and a description \
	of what questions the system is best suited for. You may also revise the original \
	input if you think that revising it will ultimately lead to a better response.
	
	<< FORMATTING >>
	Return a markdown code snippet with a JSON object formatted to look like:
	```json
	{{{{
	    "destination": string \\ name of the question answering system to use or "DEFAULT"
	    "next_inputs": string \\ a potentially modified version of the original input
	}}}}
	```
	
	REMEMBER: "destination" MUST be one of the candidate prompt names specified below OR \
	it can be "DEFAULT" if the input is not well suited for any of the candidate prompts.
	REMEMBER: "next_inputs" can just be the original input if you don't think any \
	modifications are needed.
	
	<< CANDIDATE PROMPTS >>
	{destinations}
	
	<< INPUT >>
	{{input}}
	
	<< OUTPUT >>
	"""
	
```

## [/indexes/prompts/entity_extraction.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//indexes/prompts/entity_extraction.py#L4)
```python
	_DEFAULT_ENTITY_EXTRACTION_TEMPLATE = """You are an AI assistant reading the transcript of a conversation between an AI and a human. Extract all of the proper nouns from the last line of conversation. As a guideline, a proper noun is generally capitalized. You should definitely extract all names and places.
	
	The conversation history is provided just in case of a coreference (e.g. "What do you know about him" where "him" is defined in a previous line) -- ignore items mentioned there that are not in the last line.
	
	Return the output as a single comma-separated list, or NONE if there is nothing of note to return (e.g. the user is just issuing a greeting or having a simple conversation).
	
	EXAMPLE
	Conversation history:
	Person #1: how's it going today?
	AI: "It's going great! How about you?"
	Person #1: good! busy working on Langchain. lots to do.
	AI: "That sounds like a lot of work! What kind of things are you doing to make Langchain better?"
	Last line:
	Person #1: i'm trying to improve Langchain's interfaces, the UX, its integrations with various products the user might want ... a lot of stuff.
	Output: Langchain
	END OF EXAMPLE
	
	EXAMPLE
	Conversation history:
	Person #1: how's it going today?
	AI: "It's going great! How about you?"
	Person #1: good! busy working on Langchain. lots to do.
	AI: "That sounds like a lot of work! What kind of things are you doing to make Langchain better?"
	Last line:
	Person #1: i'm trying to improve Langchain's interfaces, the UX, its integrations with various products the user might want ... a lot of stuff. I'm working with Person #2.
	Output: Langchain, Person #2
	END OF EXAMPLE
	
	Conversation history (for reference only):
	{history}
	Last line of conversation (for extraction):
	Human: {input}
	
	Output:"""
	
```

## [/indexes/prompts/entity_summarization.py](https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain//indexes/prompts/entity_summarization.py#L4)
```python
	_DEFAULT_ENTITY_SUMMARIZATION_TEMPLATE = """You are an AI assistant helping a human keep track of facts about relevant people, places, and concepts in their life. Update the summary of the provided entity in the "Entity" section based on the last line of your conversation with the human. If you are writing the summary for the first time, return a single sentence.
	The update should only include facts that are relayed in the last line of conversation about the provided entity, and should only contain facts about the provided entity.
	
	If there is no new information about the provided entity or the information is not worth noting (not an important or relevant fact to remember long-term), return the existing summary unchanged.
	
	Full conversation history (for context):
	{history}
	
	Entity to summarize:
	{entity}
	
	Existing summary of {entity}:
	{summary}
	
	Last line of conversation:
	Human: {input}
	Updated summary:"""
	
```

