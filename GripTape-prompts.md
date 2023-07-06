# GripTape Prompts

Some examples of prompts from the [GripTape](https://github.com/griptape-ai/griptape) codebase.

### [/templates/memory/tool/blob.j2](https://github.com/griptape-ai/griptape/tree/4b1028915c67f633271a6b753626493d70101d7a/griptape/templates/memory/tool/blob.j2)
```jinja
	Output of "{{ tool_name }}.{{ activity_name }}" was stored in memory "{{ memory_id }}" with the following artifact namespace: {{ artifact_namespace }}
```

### [/templates/memory/tool/text.j2](https://github.com/griptape-ai/griptape/tree/4b1028915c67f633271a6b753626493d70101d7a/griptape/templates/memory/tool/text.j2)
```jinja
	Output of "{{ tool_name }}.{{ activity_name }}" was stored in memory "{{ memory_id }}" with the following artifact namespace: {{ artifact_namespace }}
```

### [/templates/prompts/workflow.j2](https://github.com/griptape-ai/griptape/tree/4b1028915c67f633271a6b753626493d70101d7a/griptape/templates/prompts/workflow.j2)
```jinja
	Conversation begins:
	{{ task.render() }}
```

### [/templates/prompts/tool.j2](https://github.com/griptape-ai/griptape/tree/4b1028915c67f633271a6b753626493d70101d7a/griptape/templates/prompts/tool.j2)
```jinja
	tool name: {{ tool.name }}
	{{ tool.name }} activities
	{% for activity in tool.activities() %}
	activity name: {{ tool.activity_name(activity) }}
	{{ tool.activity_name(activity) }} activity description: {{ tool.activity_description(activity) }}
	{% if tool.activity_schema(activity) %}
	{{ tool.activity_name(activity) }} activity input value schema: {{ tool.activity_schema(activity) }}
	{% else %}
	{{ tool.activity_name(activity) }} activity has no input value
	{% endif %}
	{% endfor %}
```

### [/templates/prompts/pipeline.j2](https://github.com/griptape-ai/griptape/tree/4b1028915c67f633271a6b753626493d70101d7a/griptape/templates/prompts/pipeline.j2)
```jinja
	{% if not has_memory %}
	Conversation begins:
	{% endif %}
	{% for task in finished_tasks %}
	{{ task.render() }}
	{% endfor %}
	{{ current_task.render() }}
```

### [/templates/prompts/agent.j2](https://github.com/griptape-ai/griptape/tree/4b1028915c67f633271a6b753626493d70101d7a/griptape/templates/prompts/agent.j2)
```jinja
	{% if not has_memory %}
	Conversation begins:
	{% endif %}
	{{ task.render() }}
```

### [/templates/prompts/summarize.j2](https://github.com/griptape-ai/griptape/tree/4b1028915c67f633271a6b753626493d70101d7a/griptape/templates/prompts/summarize.j2)
```jinja
	{% if summary %}
	Conversation summary:
	{{ summary }}
	
	Update summary with this:
	{% else %}
	Summarize the following conversation:
	{% endif %}
	
	{% for run in runs %}
	Input: {{ run.input }}
	Output: {{ run.output }}
	
	{% endfor %}
	{% if summary %}
	Updated short summary:
	{% else %}
	Short summary:
	{% endif %}
```

### [/templates/prompts/run.j2](https://github.com/griptape-ai/griptape/tree/4b1028915c67f633271a6b753626493d70101d7a/griptape/templates/prompts/run.j2)
```jinja
	Input: {{ run.input }}
	Output: {{ run.output }}
```

### [/templates/prompts/tasks/prompt/base.j2](https://github.com/griptape-ai/griptape/tree/4b1028915c67f633271a6b753626493d70101d7a/griptape/templates/prompts/tasks/prompt/base.j2)
```jinja
	Act like a conversational bot. Use this conversation format:
	
	Input: <original request>
	Output: <your response>
	
	{% if rulesets|length > 0 %}
	When responding, always use rules from the following rulesets. Rulesets can override and complement each other:
	
	{% for ruleset in rulesets %}
	Ruleset name: {{ ruleset.name }}
	"{{ ruleset.name }}" rules:
	{% for rule in ruleset.rules %}
	Rule #{{loop.index}}
	{{ rule.value }}
	{% endfor %}
	
	{% endfor %}
	{% endif %}
```

### [/templates/prompts/tasks/prompt/conversation.j2](https://github.com/griptape-ai/griptape/tree/4b1028915c67f633271a6b753626493d70101d7a/griptape/templates/prompts/tasks/prompt/conversation.j2)
```jinja
	Input: {{ task.input.to_text() }}
	{% if task.output %}
	Output: {{ task.output.to_text() }}
	
	{% else %}
	Output:
	{% endif %}
```

### [/templates/prompts/tasks/toolkit/base.j2](https://github.com/griptape-ai/griptape/tree/4b1028915c67f633271a6b753626493d70101d7a/griptape/templates/prompts/tasks/toolkit/base.j2)
```jinja
	Act truthfully and don't make up facts, numbers, APIs, and database content. You can perform actions to answer questions and complete tasks step-by-step. If an action fails you can be creative and try to fix it or try other options. To perform an action use this conversation format:
	
	Input: <original request>
	Thought: <your step-by-step thought process about how you can complete the request>
	Action: minified JSON object with the following JSON schema: {{ action_schema }}
	Observation: <action result>
	...repeat Thought/Action/Observation until you can respond to the original request
	Output: <your final response>
	
	"Input:", "Thought:", "Action:", "Observation:", and "Output:" must ALWAYS start on a new line.
	
	Action must ALWAYS be a single-line JSON object starting on the same line as "Action:"
	
	If you don't need to perform an action or if you don't know which action to perform, ignore Thought/Action/Observation and go straight to Output. NEVER make up action types.
	
	{% if tool_names|length > 0 %}
	Actions of Type "tool"
	
	Tools can help you complete tasks. You have access to the following tools ONLY: [{{ tool_names }}]. NEVER make up tools. NEVER use tools for tasks they are not designed for. If the observation contains an error, you MUST ALWAYS try to fix the error with another Thought and Action. NEVER request extra information from the user. If you don't need to use a tool, ignore Thought/Action/Observation and go straight to Output.
	
	Memory is used to pass data between tools. Some tools might output memory artifact namespaces. Some tools might accept memory artifact namespaces as inputs. Memory artifacts are ephemeral. ALWAYS make sure to do something with memory artifacts relevant yo your current task.
	
	{% for tool in tools %}
	{{ tool }}
	{% endfor %}
	{% endif %}
	
	{% if memory_ids|length > 0 %}
	Actions of Type "memory"
	
	Memory is used to pass data between tools. Some tools might use memory for outputs. You can use memory activities to complete tasks. You have access to the following memory ONLY: [{{ memory_ids }}]. NEVER make up memory. If you encounter an error from a memory you should ALWAYS try to fix it in another action. NEVER request extra information from the user. If you don't need to use memory, ignore Thought/Action/Observation and go straight to Output.
	
	{% for memory in memories %}
	{{ memory }}
	{% endfor %}
	{% endif %}
	
	{% if rulesets|length > 0 %}
	When responding, always use rules from the following rulesets. Rulesets can override and complement each other:
	
	{% for ruleset in rulesets %}
	Ruleset name: {{ ruleset.name }}
	"{{ ruleset.name }}" rules:
	{% for rule in ruleset.rules %}
	Rule #{{loop.index}}
	{{ rule.value }}
	{% endfor %}
	
	{% endfor %}
	{% endif %}
```

### [/templates/prompts/tasks/toolkit/subtasks.j2](https://github.com/griptape-ai/griptape/tree/4b1028915c67f633271a6b753626493d70101d7a/griptape/templates/prompts/tasks/toolkit/subtasks.j2)
```jinja
	{% for subtask in subtasks %}{{ subtask.render() }}
	{% endfor %}
```

### [/templates/prompts/tasks/toolkit/conversation.j2](https://github.com/griptape-ai/griptape/tree/4b1028915c67f633271a6b753626493d70101d7a/griptape/templates/prompts/tasks/toolkit/conversation.j2)
```jinja
	Input: {{ subtask.input.to_text() }}
	{% if subtask.output %}
	Output: {{ subtask.output.to_text() }}
	{% else %}
	{% for subtask in subtasks %}{{ subtask.render() }}
	{% endfor %}
	{% endif %}
```

### [/templates/prompts/tasks/toolkit/subtask.j2](https://github.com/griptape-ai/griptape/tree/4b1028915c67f633271a6b753626493d70101d7a/griptape/templates/prompts/tasks/toolkit/subtask.j2)
```jinja
	{% if subtask.thought %}
	Thought: {{ subtask.thought }}
	{% endif %}
	Action: {{ subtask.to_json() }}
	{% if subtask.output %}
	Observation: {{ subtask.output.to_text() }}
	{% endif %}
```

### [/templates/prompts/memory/tool.j2](https://github.com/griptape-ai/griptape/tree/4b1028915c67f633271a6b753626493d70101d7a/griptape/templates/prompts/memory/tool.j2)
```jinja
	memory ID: {{ memory.id }}
	{{ memory.id }} activities
	{% for activity in memory.activities() %}
	activity name: {{ memory.activity_name(activity) }}
	{{ memory.activity_name(activity) }} activity description: {{ memory.activity_description(activity) }}
	{% if memory.activity_schema(activity) %}
	{{ memory.activity_name(activity) }} activity input value schema: {{ memory.activity_schema(activity) }}
	{% else %}
	{{ memory.activity_name(activity) }} activity has no input value
	{% endif %}
	{% endfor %}
	
```

### [/templates/prompts/memory/structure.j2](https://github.com/griptape-ai/griptape/tree/4b1028915c67f633271a6b753626493d70101d7a/griptape/templates/prompts/memory/structure.j2)
```jinja
	{% if summary %}
	Summary of the conversation so far:
	
	{{ summary }}
	
	Conversation begins:
	{% else %}
	Conversation begins:
	{% endif %}
	{% for run in runs %}
	{{ run.render() }}
	{% endfor %}
```

