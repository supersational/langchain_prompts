import requests
import os
import tokenize
import langchain

results = []

def search_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                search_file(os.path.join(root, file))

def search_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:

        for toktype, tokstr, (lineno, _), (end_lineno, _), line in tokenize.generate_tokens(file.readline):
            if toktype == tokenize.STRING:
                if len(tokstr) > 100:
                        if line.strip()[0] in '\'"' or line.strip()[:2] in ('r"', 'r\'', 'u"', 'u\'', 'f"', 'f\''):
                            continue
                        if '{' not in tokstr:
                            continue
                        results.append((file_path, lineno, line, tokstr))

                        ## prints start and end lines
                        # print('='*80)
                        # lsplit = line.split('\n')
                        # print(lsplit[0])
                        # if len(lsplit) > 1:
                        #     for i in reversed(range(1, len(lsplit))):
                        #         if lsplit[i].strip():
                        #             print(lsplit[i])
                        #             break
                        
        

if __name__ == "__main__":
    print(f'running for langchain version {langchain.__version__}')

    # load commit hash from github api
    url = f"https://api.github.com/repos/hwchase17/langchain/git/ref/tags/v{langchain.__version__}"
    r = requests.get(url)
    commit_sha = r.json()['object']['sha']
    print('found corresponding release commit: ', commit_sha)

    github_url = "https://github.com/hwchase17/langchain/blob/master/langchain/"
    directory = os.path.dirname(langchain.__file__)
    search_files(directory)
    print(f"found {len(results)} strings over 100 chars long with a {{ in them")

    # could use gh release list -R hwchase17/langchain to find associated commit
    # for now hard code to  0.216
    github_url = f"https://github.com/hwchase17/langchain/tree/{commit_sha}/langchain/"

    script_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_dir,'README.md'),'w') as f:
        f.write("""# LangChain Prompts

Some examples of prompts from the [LangChain](https://github.com/hwchase17/langchain) codebase.

- I find viewing these makes it much easier to see what each chain is doing under the hood - and find new useful tools within the codebase.
- You can also see some great examples of prompt engineering.
- Inputs to the prompts are represented by e.g. `{user_input}`.

Note: Simple heuristics were used to find prompt-like strings, so this will miss any shorter prompts and contains false positives. 
Due to the way we extract strings, this may contain only the first part of any strings where the original source string was concatenated with a `+`.

## Examples:
""")
        for file_path, lineno, line, tokstr in results:
            link = file_path.replace(directory, github_url) + "#L" + str(lineno)
            file_path = file_path.replace(directory, "")
            line = line.replace('\n','\n\t')
            f.write(f"### [{file_path}]({link.strip()})\n```python\n\t{line}\n```\n\n")
    print("done")