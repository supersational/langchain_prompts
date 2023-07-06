# LangChain Parsers

## Examples:
### SelfAskOutputParser [/agents/self_ask_with_search/output_parser.py](https://github.com/hwchase17/langchain/tree/79fb90aafd104ce013b954936f0159e96d3ae85d/langchain/agents/self_ask_with_search/output_parser.py)
```python
	from typing import Sequence, Union
	
	from langchain.agents.agent import AgentOutputParser
	from langchain.schema import AgentAction, AgentFinish, OutputParserException
	
	
	class SelfAskOutputParser(AgentOutputParser):
	    followups: Sequence[str] = ("Follow up:", "Followup:")
	    finish_string: str = "So the final answer is: "
	
	    def parse(self, text: str) -> Union[AgentAction, AgentFinish]:
	        last_line = text.split("\n")[-1]
	        if not any([follow in last_line for follow in self.followups]):
	            if self.finish_string not in last_line:
	                raise OutputParserException(f"Could not parse output: {text}")
	            return AgentFinish({"output": last_line[len(self.finish_string) :]}, text)
	
	        after_colon = text.split(":")[-1].strip()
	        return AgentAction("Intermediate Answer", after_colon, text)
	
	    @property
	    def _type(self) -> str:
	        return "self_ask"
	
```

### ChatOutputParser [/agents/chat/output_parser.py](https://github.com/hwchase17/langchain/tree/79fb90aafd104ce013b954936f0159e96d3ae85d/langchain/agents/chat/output_parser.py)
```python
	import json
	from typing import Union
	
	from langchain.agents.agent import AgentOutputParser
	from langchain.agents.chat.prompt import FORMAT_INSTRUCTIONS
	from langchain.schema import AgentAction, AgentFinish, OutputParserException
	
	FINAL_ANSWER_ACTION = "Final Answer:"
	
	
	class ChatOutputParser(AgentOutputParser):
	    def get_format_instructions(self) -> str:
	        return FORMAT_INSTRUCTIONS
	
	    def parse(self, text: str) -> Union[AgentAction, AgentFinish]:
	        includes_answer = FINAL_ANSWER_ACTION in text
	        try:
	            action = text.split("```")[1]
	            response = json.loads(action.strip())
	            includes_action = "action" in response
	            if includes_answer and includes_action:
	                raise OutputParserException(
	                    "Parsing LLM output produced a final answer "
	                    f"and a parse-able action: {text}"
	                )
	            return AgentAction(
	                response["action"], response.get("action_input", {}), text
	            )
	
	        except Exception:
	            if not includes_answer:
	                raise OutputParserException(f"Could not parse LLM output: {text}")
	            return AgentFinish(
	                {"output": text.split(FINAL_ANSWER_ACTION)[-1].strip()}, text
	            )
	
	    @property
	    def _type(self) -> str:
	        return "chat"
	
```

### MRKLOutputParser [/agents/mrkl/output_parser.py](https://github.com/hwchase17/langchain/tree/79fb90aafd104ce013b954936f0159e96d3ae85d/langchain/agents/mrkl/output_parser.py)
```python
	import re
	from typing import Union
	
	from langchain.agents.agent import AgentOutputParser
	from langchain.agents.mrkl.prompt import FORMAT_INSTRUCTIONS
	from langchain.schema import AgentAction, AgentFinish, OutputParserException
	
	FINAL_ANSWER_ACTION = "Final Answer:"
	
	
	class MRKLOutputParser(AgentOutputParser):
	    def get_format_instructions(self) -> str:
	        return FORMAT_INSTRUCTIONS
	
	    def parse(self, text: str) -> Union[AgentAction, AgentFinish]:
	        includes_answer = FINAL_ANSWER_ACTION in text
	        regex = (
	            r"Action\s*\d*\s*:[\s]*(.*?)[\s]*Action\s*\d*\s*Input\s*\d*\s*:[\s]*(.*)"
	        )
	        action_match = re.search(regex, text, re.DOTALL)
	        if action_match:
	            if includes_answer:
	                raise OutputParserException(
	                    "Parsing LLM output produced both a final answer "
	                    f"and a parse-able action: {text}"
	                )
	            action = action_match.group(1).strip()
	            action_input = action_match.group(2)
	            tool_input = action_input.strip(" ")
	            # ensure if its a well formed SQL query we don't remove any trailing " chars
	            if tool_input.startswith("SELECT ") is False:
	                tool_input = tool_input.strip('"')
	
	            return AgentAction(action, tool_input, text)
	
	        elif includes_answer:
	            return AgentFinish(
	                {"output": text.split(FINAL_ANSWER_ACTION)[-1].strip()}, text
	            )
	
	        if not re.search(r"Action\s*\d*\s*:[\s]*(.*?)", text, re.DOTALL):
	            raise OutputParserException(
	                f"Could not parse LLM output: `{text}`",
	                observation="Invalid Format: Missing 'Action:' after 'Thought:'",
	                llm_output=text,
	                send_to_llm=True,
	            )
	        elif not re.search(
	            r"[\s]*Action\s*\d*\s*Input\s*\d*\s*:[\s]*(.*)", text, re.DOTALL
	        ):
	            raise OutputParserException(
	                f"Could not parse LLM output: `{text}`",
	                observation="Invalid Format:"
	                " Missing 'Action Input:' after 'Action:'",
	                llm_output=text,
	                send_to_llm=True,
	            )
	        else:
	            raise OutputParserException(f"Could not parse LLM output: `{text}`")
	
	    @property
	    def _type(self) -> str:
	        return "mrkl"
	
```

### StructuredChatOutputParser [/agents/structured_chat/output_parser.py](https://github.com/hwchase17/langchain/tree/79fb90aafd104ce013b954936f0159e96d3ae85d/langchain/agents/structured_chat/output_parser.py)
```python
	from __future__ import annotations
	
	import json
	import logging
	import re
	from typing import Optional, Union
	
	from pydantic import Field
	
	from langchain.agents.agent import AgentOutputParser
	from langchain.agents.structured_chat.prompt import FORMAT_INSTRUCTIONS
	from langchain.base_language import BaseLanguageModel
	from langchain.output_parsers import OutputFixingParser
	from langchain.schema import AgentAction, AgentFinish, OutputParserException
	
	logger = logging.getLogger(__name__)
	
	
	class StructuredChatOutputParser(AgentOutputParser):
	    def get_format_instructions(self) -> str:
	        return FORMAT_INSTRUCTIONS
	
	    def parse(self, text: str) -> Union[AgentAction, AgentFinish]:
	        try:
	            action_match = re.search(r"```(.*?)```?", text, re.DOTALL)
	            if action_match is not None:
	                response = json.loads(action_match.group(1).strip(), strict=False)
	                if isinstance(response, list):
	                    # gpt turbo frequently ignores the directive to emit a single action
	                    logger.warning("Got multiple action responses: %s", response)
	                    response = response[0]
	                if response["action"] == "Final Answer":
	                    return AgentFinish({"output": response["action_input"]}, text)
	                else:
	                    return AgentAction(
	                        response["action"], response.get("action_input", {}), text
	                    )
	            else:
	                return AgentFinish({"output": text}, text)
	        except Exception as e:
	            raise OutputParserException(f"Could not parse LLM output: {text}") from e
	
	    @property
	    def _type(self) -> str:
	        return "structured_chat"
	
	
	class StructuredChatOutputParserWithRetries(AgentOutputParser):
	    base_parser: AgentOutputParser = Field(default_factory=StructuredChatOutputParser)
	    output_fixing_parser: Optional[OutputFixingParser] = None
	
	    def get_format_instructions(self) -> str:
	        return FORMAT_INSTRUCTIONS
	
	    def parse(self, text: str) -> Union[AgentAction, AgentFinish]:
	        try:
	            if self.output_fixing_parser is not None:
	                parsed_obj: Union[
	                    AgentAction, AgentFinish
	                ] = self.output_fixing_parser.parse(text)
	            else:
	                parsed_obj = self.base_parser.parse(text)
	            return parsed_obj
	        except Exception as e:
	            raise OutputParserException(f"Could not parse LLM output: {text}") from e
	
	    @classmethod
	    def from_llm(
	        cls,
	        llm: Optional[BaseLanguageModel] = None,
	        base_parser: Optional[StructuredChatOutputParser] = None,
	    ) -> StructuredChatOutputParserWithRetries:
	        if llm is not None:
	            base_parser = base_parser or StructuredChatOutputParser()
	            output_fixing_parser = OutputFixingParser.from_llm(
	                llm=llm, parser=base_parser
	            )
	            return cls(output_fixing_parser=output_fixing_parser)
	        elif base_parser is not None:
	            return cls(base_parser=base_parser)
	        else:
	            return cls()
	
	    @property
	    def _type(self) -> str:
	        return "structured_chat_with_retries"
	
```

### ConvoOutputParser [/agents/conversational_chat/output_parser.py](https://github.com/hwchase17/langchain/tree/79fb90aafd104ce013b954936f0159e96d3ae85d/langchain/agents/conversational_chat/output_parser.py)
```python
	from __future__ import annotations
	
	from typing import Union
	
	from langchain.agents import AgentOutputParser
	from langchain.agents.conversational_chat.prompt import FORMAT_INSTRUCTIONS
	from langchain.output_parsers.json import parse_json_markdown
	from langchain.schema import AgentAction, AgentFinish, OutputParserException
	
	
	class ConvoOutputParser(AgentOutputParser):
	    def get_format_instructions(self) -> str:
	        return FORMAT_INSTRUCTIONS
	
	    def parse(self, text: str) -> Union[AgentAction, AgentFinish]:
	        try:
	            response = parse_json_markdown(text)
	            action, action_input = response["action"], response["action_input"]
	            if action == "Final Answer":
	                return AgentFinish({"output": action_input}, text)
	            else:
	                return AgentAction(action, action_input, text)
	        except Exception as e:
	            raise OutputParserException(f"Could not parse LLM output: {text}") from e
	
	    @property
	    def _type(self) -> str:
	        return "conversational_chat"
	
```

### ConvoOutputParser [/agents/conversational/output_parser.py](https://github.com/hwchase17/langchain/tree/79fb90aafd104ce013b954936f0159e96d3ae85d/langchain/agents/conversational/output_parser.py)
```python
	import re
	from typing import Union
	
	from langchain.agents.agent import AgentOutputParser
	from langchain.agents.conversational.prompt import FORMAT_INSTRUCTIONS
	from langchain.schema import AgentAction, AgentFinish, OutputParserException
	
	
	class ConvoOutputParser(AgentOutputParser):
	    ai_prefix: str = "AI"
	
	    def get_format_instructions(self) -> str:
	        return FORMAT_INSTRUCTIONS
	
	    def parse(self, text: str) -> Union[AgentAction, AgentFinish]:
	        if f"{self.ai_prefix}:" in text:
	            return AgentFinish(
	                {"output": text.split(f"{self.ai_prefix}:")[-1].strip()}, text
	            )
	        regex = r"Action: (.*?)[\n]*Action Input: (.*)"
	        match = re.search(regex, text)
	        if not match:
	            raise OutputParserException(f"Could not parse LLM output: `{text}`")
	        action = match.group(1)
	        action_input = match.group(2)
	        return AgentAction(action.strip(), action_input.strip(" ").strip('"'), text)
	
	    @property
	    def _type(self) -> str:
	        return "conversational"
	
```

### ReActOutputParser [/agents/react/output_parser.py](https://github.com/hwchase17/langchain/tree/79fb90aafd104ce013b954936f0159e96d3ae85d/langchain/agents/react/output_parser.py)
```python
	import re
	from typing import Union
	
	from langchain.agents.agent import AgentOutputParser
	from langchain.schema import AgentAction, AgentFinish, OutputParserException
	
	
	class ReActOutputParser(AgentOutputParser):
	    def parse(self, text: str) -> Union[AgentAction, AgentFinish]:
	        action_prefix = "Action: "
	        if not text.strip().split("\n")[-1].startswith(action_prefix):
	            raise OutputParserException(f"Could not parse LLM Output: {text}")
	        action_block = text.strip().split("\n")[-1]
	
	        action_str = action_block[len(action_prefix) :]
	        # Parse out the action and the directive.
	        re_matches = re.search(r"(.*?)\[(.*?)\]", action_str)
	        if re_matches is None:
	            raise OutputParserException(
	                f"Could not parse action directive: {action_str}"
	            )
	        action, action_input = re_matches.group(1), re_matches.group(2)
	        if action == "Finish":
	            return AgentFinish({"output": action_input}, text)
	        else:
	            return AgentAction(action, action_input, text)
	
	    @property
	    def _type(self) -> str:
	        return "react"
	
```

