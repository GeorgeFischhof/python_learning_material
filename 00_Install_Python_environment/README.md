# How To set up the development / learning environment

## Installing Python and other required packages

### Install `uv` project manager

`uv` is a quiet new Python project manager. It manages Python versions, project dependencies,
virtual environments and tools

1. Install `uv`  dependency manager <br/>
   1. **Doc:** https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2 <br/>
   2. **PowerShell Command:** `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
   3. **Start new** powershell or commandline (CMD) window after install, to check the installation: `uv --version`

### Install Python and required packages

1. Create a new project directory (you can do this in Windows file manager)
    don't use:
   - space
   - accented or special characters

<details>
<summary>If you <b>don't know</b> how to use git</summary>

2. download and unzip the repo from [George Python learning material](https://github.com/GeorgeFischhof/python_learning_material)
   push the green <>Code button, and from the dropdown menu push "Download ZIP"
</details>

<details open>
<summary>If you <b>know</b> how to use Git</summary>

2. install git from the official git-scm.com
   1. in the terminal go to the created directory
   2. `git clone https://github.com/GeorgeFischhof/python_learning_material.git`
   3. this will open the git credential manager. You have to log in.
</details>

3. Install Python and required packages (everything can be found in `pyproject.toml` file) <br/>
   **Command:** `uv sync` <br/>
   Notes
   1. Astral (the creator of uv) maintains a Python repository, and uv will install Python form that repository
   2. uv can install different versions of Python according to needs because of this repo
   3. Python is installed into the virtual environment

## Install and setup IDE (Integrated Development Environment)

1. Download and install PyCharm <br/>
   URL: https://www.jetbrains.com/pycharm/download/?section=windows
   During the installation, there is a checkbox "Add bin folder to the path", **check it in** <br/>
   it will be good for example to call the diff form command line
2. After install select "Open" and select the folder where you have the Python learning stuff (the content of the repo)



