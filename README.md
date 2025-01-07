# internet_archive

A script for fetching metadata from internet archive.

## TOC
- [Installation](#installation)
- [Quickstart](#quickstart)
    - [Running the Script](#running-the-script)
    - [Customizing the Script](#customizing-the-script)

## Installation

1. Download and install python if you don't have it.
    - [Download Python](https://www.python.org/downloads/)

2. Verify python and pip (pip install packages) are in your PATH variables.

    ```powershell
    PS C:> python --version
    Python X.X.X
    PS C:> python -m pip --version
    pip Y.Y.Y. from path/to/pip (python X.X.X)
    ```

3. Download the files from the github repo to where you want the script to live on your local computer.
    - [Lindsay's Internet Archive Repo](https://github.com/laboord/internet_archive)

4. Navigate to that folder in your CLI.

    ```powershell
    PS C:> cd path/to/root/project/folder
    ```

5. Create a python virtual environment (venv).

    ```powershell
    PS C:> python -m venv venv
    ```

6. Turn on venv.

    ```powershell
    PS C:> venv/Scripts/activate
    ```

    - You should see `(venv)` at the beggining of the command line

7. Install python internet archive package.

    ```powershell
    (venv) PS C:> pip install internetarchive
    ```

    - [Internet Archive Python Library Docs](https://archive.org/developers/internetarchive/index.html)

8. Signup for an Internet Archive account (free).

9. Configure the python library settings.

    ```powershell
    (venv) PS C:> ia configure
    Enter your archive.org credentials below to configure 'ia'.

    Email address: user@example.com
    Password:

    Config saved to: /home/user/.config/ia.ini
    ```

    - [Configuring Docs](https://archive.org/developers/internetarchive/quickstart.html#configuring)


## Quickstart

### Running the script

1. Navigate to the project root folder in your CLI.

    ```powershell
    PS C:> cd path/to/root/project/folder
    ```

2. Turn on venv.

    ```powershell
    PS C:> venv/Scripts/activate
    ```

    - You should see `(venv)` at the beggining of the command line

3. Run the script as is.

    ```powershell
    (venv) PS C:> python main.py
    ```

### Customizing the script

#### search_items()

- [search_items() docs](https://archive.org/developers/internetarchive/api.html#internetarchive.search_items)

#### Change Collection

- Update the `COLLECTIONS` list inside `main.py`.
- Collection name can be found in the URL: archive.org/details/\<collection_id>
- You can add multiple collections in the list or just leave it at one.
- Each collection will add its own json and csv file output.

#### Available Search Fields

> [!IMPORTANT]
> The description field will eat up runtime. Other fields not already in the script may as well, but I didn't test them.

- Update the `FIELDS` list inside `main.py`.

![Screenshot of available search fields](/docs/images/available_search_fields.png)
