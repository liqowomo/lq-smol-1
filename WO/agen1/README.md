
1. [Using Autogen Studio](#using-autogen-studio)
2. [Install and Usage](#install-and-usage)
3. [Running with `panty.py`](#running-with-pantypy)
4. [Regarding the Autogen Studio](#regarding-the-autogen-studio)


# Using Autogen Studio

1. Testing out autogen studio
2. https://autogen-studio.com/autogen-studio-ui - Just following this tutorial 

# Install and Usage

1. Startup a new uv prject 
2. Install Autogen 

```sh 
uv add autogenstudio
uv run autogenstudio ui
```

# Running with `panty.py`

1. Check the `panty.py` file
2. Python script to run the file using sub process, we are also waiting on the process during shutdown

# Regarding the Autogen Studio 

1. It is not recommended to use it in production.
2. It is better to use the `panty.py` file, and write out the agents python files manually, and then execute