
1. [LiteLLM](#litellm)
2. [Main Repo](#main-repo)
3. [Instaling Panties](#instaling-panties)
4. [Setting the environment variable in fish](#setting-the-environment-variable-in-fish)


# LiteLLM
1. Testing out litellm with openrouterpantykeyz

# Main Repo

https://github.com/BerriAI/litellm 
- This is the opensource version which is free 
- But they also have a paid option - 

# Instaling Panties 

Good sample code 

```py 
pip install litellm
```

Actual Usage - OpenRouter 
https://docs.litellm.ai/docs/providers/openrouter 
- Official Docs on this

```py 
import os
from litellm import completion
os.environ["OPENROUTER_API_KEY"] = ""

os.environ["OR_SITE_URL"] = "" # optional
os.environ["OR_APP_NAME"] = "" # optional

response = completion(
            model="openrouter/google/palm-2-chat-bison",
            messages=messages,
        )
```

And with more params 

```py 
import os
from litellm import completion
os.environ["OPENROUTER_API_KEY"] = ""

response = completion(
            model="openrouter/google/palm-2-chat-bison",
            messages=messages,
            transforms = [""],
            route= ""
        )
```

# Setting the environment variable in fish 

```sh 
# For fish shell
set -gx mykey "696" # -gx makes it global (available to subprocesses)

# For Bash/ZSH 
export mykey="696"
```