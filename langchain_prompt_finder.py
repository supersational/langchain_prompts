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

    github_url = "https://github.com/hwchase17/langchain/blob/master/langchain/"
    directory = os.path.dirname(langchain.__file__)
    search_files(directory)
    print(f"found {len(results)} strings over 100 chars long with a {{ in them")

    # could use gh release list -R hwchase17/langchain to find associated commit
    # for now hard code to  0.216
    github_url = "https://github.com/hwchase17/langchain/tree/d1bcc58beb8fcc5157ddb7cd03b7acf8615f9f5d/langchain/"

    script_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_dir,'README.md'),'w') as f:
        f.write("""# LangChain Prompts

Some examples of prompts from the [LangChain](https://github.com/hwchase17/langchain) codebase.
Note: Not comprehensive, and may contain truncated strings where the string concatenated with a `+`.
""")
        for file_path, lineno, line, tokstr in results:
            link = file_path.replace(directory, github_url) + "#L" + str(lineno)
            file_path = file_path.replace(directory, "")
            line = line.replace('\n','\n\t')
            f.write(f"## [{file_path}]({link.strip()})\n```python\n\t{line}\n```\n\n")
    print("done")