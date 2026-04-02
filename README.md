# Real-Time Analytics - Course Repository

## Task 1.1
python3 --version
pip --version
Python 3.13.12
pip 26.0.1 from /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/pip (python 3.13)

## Task 1.2
source rta_env/bin/activate                
pip install --upgrade pip
pip install jupyterlab pandas numpy matplotlib scikit-learn requests
Requirement already satisfied: pip in ./rta_env/lib/python3.13/site-packages (25.3)
Collecting pip
  Using cached pip-26.0.1-py3-none-any.whl.metadata (4.7 kB)
Using cached pip-26.0.1-py3-none-any.whl (1.8 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 25.3
    Uninstalling pip-25.3:
      Successfully uninstalled pip-25.3
Successfully installed pip-26.0.1
Collecting jupyterlab
  Using cached jupyterlab-4.5.6-py3-none-any.whl.metadata (16 kB)
Collecting pandas
  Downloading pandas-3.0.2-cp313-cp313-macosx_11_0_arm64.whl.metadata (79 kB)
Collecting numpy
  Downloading numpy-2.4.4-cp313-cp313-macosx_14_0_arm64.whl.metadata (6.6 kB)
Collecting matplotlib
  Using cached matplotlib-3.10.8-cp313-cp313-macosx_11_0_arm64.whl.metadata (52 kB)
Collecting scikit-learn
  Using cached scikit_learn-1.8.0-cp313-cp313-macosx_12_0_arm64.whl.metadata (11 kB)
Collecting requests
  Downloading requests-2.33.1-py3-none-any.whl.metadata (4.8 kB)
Collecting async-lru>=1.0.0 (from jupyterlab)
  Using cached async_lru-2.3.0-py3-none-any.whl.metadata (7.6 kB)
Collecting httpx<1,>=0.25.0 (from jupyterlab)
  Using cached httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting ipykernel!=6.30.0,>=6.5.0 (from jupyterlab)
  Using cached ipykernel-7.2.0-py3-none-any.whl.metadata (4.5 kB)
Collecting jinja2>=3.0.3 (from jupyterlab)
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting jupyter-core (from jupyterlab)
  Using cached jupyter_core-5.9.1-py3-none-any.whl.metadata (1.5 kB)
Collecting jupyter-lsp>=2.0.0 (from jupyterlab)
  Downloading jupyter_lsp-2.3.1-py3-none-any.whl.metadata (1.8 kB)
Collecting jupyter-server<3,>=2.4.0 (from jupyterlab)
  Using cached jupyter_server-2.17.0-py3-none-any.whl.metadata (8.5 kB)
Collecting jupyterlab-server<3,>=2.28.0 (from jupyterlab)
  Using cached jupyterlab_server-2.28.0-py3-none-any.whl.metadata (5.9 kB)
Collecting notebook-shim>=0.2 (from jupyterlab)
  Using cached notebook_shim-0.2.4-py3-none-any.whl.metadata (4.0 kB)
Collecting packaging (from jupyterlab)
  Using cached packaging-26.0-py3-none-any.whl.metadata (3.3 kB)
Collecting setuptools>=41.1.0 (from jupyterlab)
  Using cached setuptools-82.0.1-py3-none-any.whl.metadata (6.5 kB)
Collecting tornado>=6.2.0 (from jupyterlab)
  Using cached tornado-6.5.5-cp39-abi3-macosx_10_9_universal2.whl.metadata (2.8 kB)
Collecting traitlets (from jupyterlab)
  Using cached traitlets-5.14.3-py3-none-any.whl.metadata (10 kB)
Collecting anyio (from httpx<1,>=0.25.0->jupyterlab)
  Using cached anyio-4.13.0-py3-none-any.whl.metadata (4.5 kB)
Collecting certifi (from httpx<1,>=0.25.0->jupyterlab)
  Using cached certifi-2026.2.25-py3-none-any.whl.metadata (2.5 kB)
Collecting httpcore==1.* (from httpx<1,>=0.25.0->jupyterlab)
  Using cached httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Collecting idna (from httpx<1,>=0.25.0->jupyterlab)
  Using cached idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting h11>=0.16 (from httpcore==1.*->httpx<1,>=0.25.0->jupyterlab)
  Using cached h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting argon2-cffi>=21.1 (from jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached argon2_cffi-25.1.0-py3-none-any.whl.metadata (4.1 kB)
Collecting jupyter-client>=7.4.4 (from jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached jupyter_client-8.8.0-py3-none-any.whl.metadata (8.4 kB)
Collecting jupyter-events>=0.11.0 (from jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached jupyter_events-0.12.0-py3-none-any.whl.metadata (5.8 kB)
Collecting jupyter-server-terminals>=0.4.4 (from jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached jupyter_server_terminals-0.5.4-py3-none-any.whl.metadata (5.9 kB)
Collecting nbconvert>=6.4.4 (from jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached nbconvert-7.17.0-py3-none-any.whl.metadata (8.4 kB)
Collecting nbformat>=5.3.0 (from jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached nbformat-5.10.4-py3-none-any.whl.metadata (3.6 kB)
Collecting prometheus-client>=0.9 (from jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached prometheus_client-0.24.1-py3-none-any.whl.metadata (2.1 kB)
Collecting pyzmq>=24 (from jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached pyzmq-27.1.0-cp312-abi3-macosx_10_15_universal2.whl.metadata (6.0 kB)
Collecting send2trash>=1.8.2 (from jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached send2trash-2.1.0-py3-none-any.whl.metadata (4.1 kB)
Collecting terminado>=0.8.3 (from jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached terminado-0.18.1-py3-none-any.whl.metadata (5.8 kB)
Collecting websocket-client>=1.7 (from jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached websocket_client-1.9.0-py3-none-any.whl.metadata (8.3 kB)
Collecting babel>=2.10 (from jupyterlab-server<3,>=2.28.0->jupyterlab)
  Using cached babel-2.18.0-py3-none-any.whl.metadata (2.2 kB)
Collecting json5>=0.9.0 (from jupyterlab-server<3,>=2.28.0->jupyterlab)
  Downloading json5-0.14.0-py3-none-any.whl.metadata (36 kB)
Collecting jsonschema>=4.18.0 (from jupyterlab-server<3,>=2.28.0->jupyterlab)
  Using cached jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting python-dateutil>=2.8.2 (from pandas)
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting contourpy>=1.0.1 (from matplotlib)
  Using cached contourpy-1.3.3-cp313-cp313-macosx_11_0_arm64.whl.metadata (5.5 kB)
Collecting cycler>=0.10 (from matplotlib)
  Using cached cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting fonttools>=4.22.0 (from matplotlib)
  Using cached fonttools-4.62.1-cp313-cp313-macosx_10_13_universal2.whl.metadata (117 kB)
Collecting kiwisolver>=1.3.1 (from matplotlib)
  Using cached kiwisolver-1.5.0-cp313-cp313-macosx_11_0_arm64.whl.metadata (5.1 kB)
Collecting pillow>=8 (from matplotlib)
  Downloading pillow-12.2.0-cp313-cp313-macosx_11_0_arm64.whl.metadata (8.8 kB)
Collecting pyparsing>=3 (from matplotlib)
  Using cached pyparsing-3.3.2-py3-none-any.whl.metadata (5.8 kB)
Collecting scipy>=1.10.0 (from scikit-learn)
  Using cached scipy-1.17.1-cp313-cp313-macosx_14_0_arm64.whl.metadata (62 kB)
Collecting joblib>=1.3.0 (from scikit-learn)
  Using cached joblib-1.5.3-py3-none-any.whl.metadata (5.5 kB)
Collecting threadpoolctl>=3.2.0 (from scikit-learn)
  Using cached threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)
Collecting charset_normalizer<4,>=2 (from requests)
  Downloading charset_normalizer-3.4.7-cp313-cp313-macosx_10_13_universal2.whl.metadata (40 kB)
Collecting urllib3<3,>=1.26 (from requests)
  Using cached urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting argon2-cffi-bindings (from argon2-cffi>=21.1->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached argon2_cffi_bindings-25.1.0-cp39-abi3-macosx_11_0_arm64.whl.metadata (7.4 kB)
Collecting appnope>=0.1.2 (from ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Using cached appnope-0.1.4-py2.py3-none-any.whl.metadata (908 bytes)
Collecting comm>=0.1.1 (from ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Using cached comm-0.2.3-py3-none-any.whl.metadata (3.7 kB)
Collecting debugpy>=1.6.5 (from ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Using cached debugpy-1.8.20-cp313-cp313-macosx_15_0_universal2.whl.metadata (1.4 kB)
Collecting ipython>=7.23.1 (from ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Downloading ipython-9.12.0-py3-none-any.whl.metadata (4.5 kB)
Collecting matplotlib-inline>=0.1 (from ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Using cached matplotlib_inline-0.2.1-py3-none-any.whl.metadata (2.3 kB)
Collecting nest-asyncio>=1.4 (from ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Using cached nest_asyncio-1.6.0-py3-none-any.whl.metadata (2.8 kB)
Collecting psutil>=5.7 (from ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Using cached psutil-7.2.2-cp36-abi3-macosx_11_0_arm64.whl.metadata (22 kB)
Collecting decorator>=5.1.0 (from ipython>=7.23.1->ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Using cached decorator-5.2.1-py3-none-any.whl.metadata (3.9 kB)
Collecting ipython-pygments-lexers>=1.0.0 (from ipython>=7.23.1->ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Using cached ipython_pygments_lexers-1.1.1-py3-none-any.whl.metadata (1.1 kB)
Collecting jedi>=0.18.2 (from ipython>=7.23.1->ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Using cached jedi-0.19.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting pexpect>4.6 (from ipython>=7.23.1->ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Using cached pexpect-4.9.0-py2.py3-none-any.whl.metadata (2.5 kB)
Collecting prompt_toolkit<3.1.0,>=3.0.41 (from ipython>=7.23.1->ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Using cached prompt_toolkit-3.0.52-py3-none-any.whl.metadata (6.4 kB)
Collecting pygments>=2.14.0 (from ipython>=7.23.1->ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Downloading pygments-2.20.0-py3-none-any.whl.metadata (2.5 kB)
Collecting stack_data>=0.6.0 (from ipython>=7.23.1->ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Using cached stack_data-0.6.3-py3-none-any.whl.metadata (18 kB)
Collecting wcwidth (from prompt_toolkit<3.1.0,>=3.0.41->ipython>=7.23.1->ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Using cached wcwidth-0.6.0-py3-none-any.whl.metadata (30 kB)
Collecting parso<0.9.0,>=0.8.4 (from jedi>=0.18.2->ipython>=7.23.1->ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Using cached parso-0.8.6-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting MarkupSafe>=2.0 (from jinja2>=3.0.3->jupyterlab)
  Using cached markupsafe-3.0.3-cp313-cp313-macosx_11_0_arm64.whl.metadata (2.7 kB)
Collecting attrs>=22.2.0 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.28.0->jupyterlab)
  Using cached attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.28.0->jupyterlab)
  Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.28.0->jupyterlab)
  Using cached referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.25.0 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.28.0->jupyterlab)
  Using cached rpds_py-0.30.0-cp313-cp313-macosx_11_0_arm64.whl.metadata (4.1 kB)
Collecting platformdirs>=2.5 (from jupyter-core->jupyterlab)
  Using cached platformdirs-4.9.4-py3-none-any.whl.metadata (4.7 kB)
Collecting python-json-logger>=2.0.4 (from jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab)
  Downloading python_json_logger-4.1.0-py3-none-any.whl.metadata (3.7 kB)
Collecting pyyaml>=5.3 (from jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached pyyaml-6.0.3-cp313-cp313-macosx_11_0_arm64.whl.metadata (2.4 kB)
Collecting rfc3339-validator (from jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached rfc3339_validator-0.1.4-py2.py3-none-any.whl.metadata (1.5 kB)
Collecting rfc3986-validator>=0.1.1 (from jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached rfc3986_validator-0.1.1-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting fqdn (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached fqdn-1.5.1-py3-none-any.whl.metadata (1.4 kB)
Collecting isoduration (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached isoduration-20.11.0-py3-none-any.whl.metadata (5.7 kB)
Collecting jsonpointer>1.13 (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached jsonpointer-3.1.1-py3-none-any.whl.metadata (2.4 kB)
Collecting rfc3987-syntax>=1.1.0 (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached rfc3987_syntax-1.1.0-py3-none-any.whl.metadata (7.7 kB)
Collecting uri-template (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached uri_template-1.3.0-py3-none-any.whl.metadata (8.8 kB)
Collecting webcolors>=24.6.0 (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached webcolors-25.10.0-py3-none-any.whl.metadata (2.2 kB)
Collecting beautifulsoup4 (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached beautifulsoup4-4.14.3-py3-none-any.whl.metadata (3.8 kB)
Collecting bleach!=5.0.0 (from bleach[css]!=5.0.0->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached bleach-6.3.0-py3-none-any.whl.metadata (31 kB)
Collecting defusedxml (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached defusedxml-0.7.1-py2.py3-none-any.whl.metadata (32 kB)
Collecting jupyterlab-pygments (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached jupyterlab_pygments-0.3.0-py3-none-any.whl.metadata (4.4 kB)
Collecting mistune<4,>=2.0.3 (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached mistune-3.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting nbclient>=0.5.0 (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached nbclient-0.10.4-py3-none-any.whl.metadata (8.3 kB)
Collecting pandocfilters>=1.4.1 (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached pandocfilters-1.5.1-py2.py3-none-any.whl.metadata (9.0 kB)
Collecting webencodings (from bleach!=5.0.0->bleach[css]!=5.0.0->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached webencodings-0.5.1-py2.py3-none-any.whl.metadata (2.1 kB)
Collecting tinycss2<1.5,>=1.1.0 (from bleach[css]!=5.0.0->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached tinycss2-1.4.0-py3-none-any.whl.metadata (3.0 kB)
Collecting fastjsonschema>=2.15 (from nbformat>=5.3.0->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached fastjsonschema-2.21.2-py3-none-any.whl.metadata (2.3 kB)
Collecting ptyprocess>=0.5 (from pexpect>4.6->ipython>=7.23.1->ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Using cached ptyprocess-0.7.0-py2.py3-none-any.whl.metadata (1.3 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas)
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting lark>=1.2.2 (from rfc3987-syntax>=1.1.0->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached lark-1.3.1-py3-none-any.whl.metadata (1.8 kB)
Collecting executing>=1.2.0 (from stack_data>=0.6.0->ipython>=7.23.1->ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Using cached executing-2.2.1-py2.py3-none-any.whl.metadata (8.9 kB)
Collecting asttokens>=2.1.0 (from stack_data>=0.6.0->ipython>=7.23.1->ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Using cached asttokens-3.0.1-py3-none-any.whl.metadata (4.9 kB)
Collecting pure-eval (from stack_data>=0.6.0->ipython>=7.23.1->ipykernel!=6.30.0,>=6.5.0->jupyterlab)
  Using cached pure_eval-0.2.3-py3-none-any.whl.metadata (6.3 kB)
Collecting cffi>=1.0.1 (from argon2-cffi-bindings->argon2-cffi>=21.1->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached cffi-2.0.0-cp313-cp313-macosx_11_0_arm64.whl.metadata (2.6 kB)
Collecting pycparser (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi>=21.1->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
Collecting soupsieve>=1.6.1 (from beautifulsoup4->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached soupsieve-2.8.3-py3-none-any.whl.metadata (4.6 kB)
Collecting typing-extensions>=4.0.0 (from beautifulsoup4->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting arrow>=0.15.0 (from isoduration->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached arrow-1.4.0-py3-none-any.whl.metadata (7.7 kB)
Collecting tzdata (from arrow>=0.15.0->isoduration->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab)
  Using cached tzdata-2025.3-py2.py3-none-any.whl.metadata (1.4 kB)
Using cached jupyterlab-4.5.6-py3-none-any.whl (12.4 MB)
Using cached httpx-0.28.1-py3-none-any.whl (73 kB)
Using cached httpcore-1.0.9-py3-none-any.whl (78 kB)
Using cached jupyter_server-2.17.0-py3-none-any.whl (388 kB)
Using cached jupyterlab_server-2.28.0-py3-none-any.whl (59 kB)
Downloading pandas-3.0.2-cp313-cp313-macosx_11_0_arm64.whl (9.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.9/9.9 MB 4.4 MB/s  0:00:02
Downloading numpy-2.4.4-cp313-cp313-macosx_14_0_arm64.whl (5.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.2/5.2 MB 7.2 MB/s  0:00:00
Using cached matplotlib-3.10.8-cp313-cp313-macosx_11_0_arm64.whl (8.1 MB)
Using cached scikit_learn-1.8.0-cp313-cp313-macosx_12_0_arm64.whl (8.0 MB)
Downloading requests-2.33.1-py3-none-any.whl (64 kB)
Downloading charset_normalizer-3.4.7-cp313-cp313-macosx_10_13_universal2.whl (309 kB)
Using cached idna-3.11-py3-none-any.whl (71 kB)
Using cached urllib3-2.6.3-py3-none-any.whl (131 kB)
Using cached anyio-4.13.0-py3-none-any.whl (114 kB)
Using cached argon2_cffi-25.1.0-py3-none-any.whl (14 kB)
Using cached async_lru-2.3.0-py3-none-any.whl (8.4 kB)
Using cached babel-2.18.0-py3-none-any.whl (10.2 MB)
Using cached certifi-2026.2.25-py3-none-any.whl (153 kB)
Using cached contourpy-1.3.3-cp313-cp313-macosx_11_0_arm64.whl (274 kB)
Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)
Using cached fonttools-4.62.1-cp313-cp313-macosx_10_13_universal2.whl (2.9 MB)
Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Using cached ipykernel-7.2.0-py3-none-any.whl (118 kB)
Using cached appnope-0.1.4-py2.py3-none-any.whl (4.3 kB)
Using cached comm-0.2.3-py3-none-any.whl (7.3 kB)
Using cached debugpy-1.8.20-cp313-cp313-macosx_15_0_universal2.whl (2.5 MB)
Downloading ipython-9.12.0-py3-none-any.whl (625 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 625.7/625.7 kB 3.7 MB/s  0:00:00
Using cached prompt_toolkit-3.0.52-py3-none-any.whl (391 kB)
Using cached decorator-5.2.1-py3-none-any.whl (9.2 kB)
Using cached ipython_pygments_lexers-1.1.1-py3-none-any.whl (8.1 kB)
Using cached jedi-0.19.2-py2.py3-none-any.whl (1.6 MB)
Using cached parso-0.8.6-py2.py3-none-any.whl (106 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached joblib-1.5.3-py3-none-any.whl (309 kB)
Downloading json5-0.14.0-py3-none-any.whl (36 kB)
Using cached jsonschema-4.26.0-py3-none-any.whl (90 kB)
Using cached attrs-26.1.0-py3-none-any.whl (67 kB)
Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Using cached jupyter_client-8.8.0-py3-none-any.whl (107 kB)
Using cached jupyter_core-5.9.1-py3-none-any.whl (29 kB)
Using cached jupyter_events-0.12.0-py3-none-any.whl (19 kB)
Using cached jsonpointer-3.1.1-py3-none-any.whl (7.7 kB)
Downloading jupyter_lsp-2.3.1-py3-none-any.whl (77 kB)
Using cached jupyter_server_terminals-0.5.4-py3-none-any.whl (13 kB)
Using cached kiwisolver-1.5.0-cp313-cp313-macosx_11_0_arm64.whl (64 kB)
Using cached markupsafe-3.0.3-cp313-cp313-macosx_11_0_arm64.whl (12 kB)
Using cached matplotlib_inline-0.2.1-py3-none-any.whl (9.5 kB)
Using cached nbconvert-7.17.0-py3-none-any.whl (261 kB)
Using cached mistune-3.2.0-py3-none-any.whl (53 kB)
Using cached bleach-6.3.0-py3-none-any.whl (164 kB)
Using cached tinycss2-1.4.0-py3-none-any.whl (26 kB)
Using cached nbclient-0.10.4-py3-none-any.whl (25 kB)
Using cached nbformat-5.10.4-py3-none-any.whl (78 kB)
Using cached fastjsonschema-2.21.2-py3-none-any.whl (24 kB)
Using cached nest_asyncio-1.6.0-py3-none-any.whl (5.2 kB)
Using cached notebook_shim-0.2.4-py3-none-any.whl (13 kB)
Using cached packaging-26.0-py3-none-any.whl (74 kB)
Using cached pandocfilters-1.5.1-py2.py3-none-any.whl (8.7 kB)
Using cached pexpect-4.9.0-py2.py3-none-any.whl (63 kB)
Downloading pillow-12.2.0-cp313-cp313-macosx_11_0_arm64.whl (4.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.7/4.7 MB 8.8 MB/s  0:00:00
Using cached platformdirs-4.9.4-py3-none-any.whl (21 kB)
Using cached prometheus_client-0.24.1-py3-none-any.whl (64 kB)
Using cached psutil-7.2.2-cp36-abi3-macosx_11_0_arm64.whl (129 kB)
Using cached ptyprocess-0.7.0-py2.py3-none-any.whl (13 kB)
Downloading pygments-2.20.0-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 4.8 MB/s  0:00:00
Using cached pyparsing-3.3.2-py3-none-any.whl (122 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading python_json_logger-4.1.0-py3-none-any.whl (15 kB)
Using cached pyyaml-6.0.3-cp313-cp313-macosx_11_0_arm64.whl (173 kB)
Using cached pyzmq-27.1.0-cp312-abi3-macosx_10_15_universal2.whl (1.3 MB)
Using cached referencing-0.37.0-py3-none-any.whl (26 kB)
Using cached rfc3986_validator-0.1.1-py2.py3-none-any.whl (4.2 kB)
Using cached rfc3987_syntax-1.1.0-py3-none-any.whl (8.0 kB)
Using cached lark-1.3.1-py3-none-any.whl (113 kB)
Using cached rpds_py-0.30.0-cp313-cp313-macosx_11_0_arm64.whl (358 kB)
Using cached scipy-1.17.1-cp313-cp313-macosx_14_0_arm64.whl (20.3 MB)
Using cached send2trash-2.1.0-py3-none-any.whl (17 kB)
Using cached setuptools-82.0.1-py3-none-any.whl (1.0 MB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached stack_data-0.6.3-py3-none-any.whl (24 kB)
Using cached asttokens-3.0.1-py3-none-any.whl (27 kB)
Using cached executing-2.2.1-py2.py3-none-any.whl (28 kB)
Using cached terminado-0.18.1-py3-none-any.whl (14 kB)
Using cached threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
Using cached tornado-6.5.5-cp39-abi3-macosx_10_9_universal2.whl (445 kB)
Using cached traitlets-5.14.3-py3-none-any.whl (85 kB)
Using cached webcolors-25.10.0-py3-none-any.whl (14 kB)
Using cached webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Using cached websocket_client-1.9.0-py3-none-any.whl (82 kB)
Using cached argon2_cffi_bindings-25.1.0-cp39-abi3-macosx_11_0_arm64.whl (31 kB)
Using cached cffi-2.0.0-cp313-cp313-macosx_11_0_arm64.whl (181 kB)
Using cached beautifulsoup4-4.14.3-py3-none-any.whl (107 kB)
Using cached soupsieve-2.8.3-py3-none-any.whl (37 kB)
Using cached typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Using cached defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
Using cached fqdn-1.5.1-py3-none-any.whl (9.1 kB)
Using cached isoduration-20.11.0-py3-none-any.whl (11 kB)
Using cached arrow-1.4.0-py3-none-any.whl (68 kB)
Using cached jupyterlab_pygments-0.3.0-py3-none-any.whl (15 kB)
Using cached pure_eval-0.2.3-py3-none-any.whl (11 kB)
Using cached pycparser-3.0-py3-none-any.whl (48 kB)
Using cached rfc3339_validator-0.1.4-py2.py3-none-any.whl (3.5 kB)
Using cached tzdata-2025.3-py2.py3-none-any.whl (348 kB)
Using cached uri_template-1.3.0-py3-none-any.whl (11 kB)
Using cached wcwidth-0.6.0-py3-none-any.whl (94 kB)
Installing collected packages: webencodings, pure-eval, ptyprocess, fastjsonschema, websocket-client, webcolors, wcwidth, urllib3, uri-template, tzdata, typing-extensions, traitlets, tornado, tinycss2, threadpoolctl, soupsieve, six, setuptools, send2trash, rpds-py, rfc3986-validator, pyzmq, pyyaml, python-json-logger, pyparsing, pygments, pycparser, psutil, prometheus-client, platformdirs, pillow, pexpect, parso, pandocfilters, packaging, numpy, nest-asyncio, mistune, MarkupSafe, lark, kiwisolver, jupyterlab-pygments, jsonpointer, json5, joblib, idna, h11, fqdn, fonttools, executing, defusedxml, decorator, debugpy, cycler, comm, charset_normalizer, certifi, bleach, babel, attrs, async-lru, asttokens, appnope, terminado, stack_data, scipy, rfc3987-syntax, rfc3339-validator, requests, referencing, python-dateutil, prompt_toolkit, matplotlib-inline, jupyter-core, jinja2, jedi, ipython-pygments-lexers, httpcore, contourpy, cffi, beautifulsoup4, anyio, scikit-learn, pandas, matplotlib, jupyter-server-terminals, jupyter-client, jsonschema-specifications, ipython, httpx, arrow, argon2-cffi-bindings, jsonschema, isoduration, ipykernel, argon2-cffi, nbformat, nbclient, jupyter-events, nbconvert, jupyter-server, notebook-shim, jupyterlab-server, jupyter-lsp, jupyterlab
Successfully installed MarkupSafe-3.0.3 anyio-4.13.0 appnope-0.1.4 argon2-cffi-25.1.0 argon2-cffi-bindings-25.1.0 arrow-1.4.0 asttokens-3.0.1 async-lru-2.3.0 attrs-26.1.0 babel-2.18.0 beautifulsoup4-4.14.3 bleach-6.3.0 certifi-2026.2.25 cffi-2.0.0 charset_normalizer-3.4.7 comm-0.2.3 contourpy-1.3.3 cycler-0.12.1 debugpy-1.8.20 decorator-5.2.1 defusedxml-0.7.1 executing-2.2.1 fastjsonschema-2.21.2 fonttools-4.62.1 fqdn-1.5.1 h11-0.16.0 httpcore-1.0.9 httpx-0.28.1 idna-3.11 ipykernel-7.2.0 ipython-9.12.0 ipython-pygments-lexers-1.1.1 isoduration-20.11.0 jedi-0.19.2 jinja2-3.1.6 joblib-1.5.3 json5-0.14.0 jsonpointer-3.1.1 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 jupyter-client-8.8.0 jupyter-core-5.9.1 jupyter-events-0.12.0 jupyter-lsp-2.3.1 jupyter-server-2.17.0 jupyter-server-terminals-0.5.4 jupyterlab-4.5.6 jupyterlab-pygments-0.3.0 jupyterlab-server-2.28.0 kiwisolver-1.5.0 lark-1.3.1 matplotlib-3.10.8 matplotlib-inline-0.2.1 mistune-3.2.0 nbclient-0.10.4 nbconvert-7.17.0 nbformat-5.10.4 nest-asyncio-1.6.0 notebook-shim-0.2.4 numpy-2.4.4 packaging-26.0 pandas-3.0.2 pandocfilters-1.5.1 parso-0.8.6 pexpect-4.9.0 pillow-12.2.0 platformdirs-4.9.4 prometheus-client-0.24.1 prompt_toolkit-3.0.52 psutil-7.2.2 ptyprocess-0.7.0 pure-eval-0.2.3 pycparser-3.0 pygments-2.20.0 pyparsing-3.3.2 python-dateutil-2.9.0.post0 python-json-logger-4.1.0 pyyaml-6.0.3 pyzmq-27.1.0 referencing-0.37.0 requests-2.33.1 rfc3339-validator-0.1.4 rfc3986-validator-0.1.1 rfc3987-syntax-1.1.0 rpds-py-0.30.0 scikit-learn-1.8.0 scipy-1.17.1 send2trash-2.1.0 setuptools-82.0.1 six-1.17.0 soupsieve-2.8.3 stack_data-0.6.3 terminado-0.18.1 threadpoolctl-3.6.0 tinycss2-1.4.0 tornado-6.5.5 traitlets-5.14.3 typing-extensions-4.15.0 tzdata-2025.3 uri-template-1.3.0 urllib3-2.6.3 wcwidth-0.6.0 webcolors-25.10.0 webencodings-0.5.1 websocket-client-1.9.0

## Task 1.3
pandas:  3.0.2
numpy:   2.4.4
sklearn: 1.8.0

All good! Your Python environment is ready.

## Task 2.1
git --version
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git version 2.50.1 (Apple Git-155)

## Task 2.3
git clone https://github.com/hubertusyt/RTA_HP.git   
cd RTA_HP            
Cloning into 'RTA_HP'...
remote: Enumerating objects: 14, done.
remote: Counting objects: 100% (14/14), done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 14 (delta 1), reused 11 (delta 1), pack-reused 0 (from 0)
Receiving objects: 100% (14/14), done.
Resolving deltas: 100% (1/1), done.

## Task 3
 docker --version
docker compose version
docker run hello-world
Docker version 29.3.0, build 5927d80
Docker Compose version v5.1.0

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

hubert@Huberts-MacBook-Pro ~ % docker run -it python:3.11-slim python -c "print('Hello from Docker!')"
Hello from Docker!

## Task 4.1 and 4.2
git clone -b 2026Redis https://github.com/sebkaz/jupyterlab-project.git
cd jupyterlab-project
Cloning into 'jupyterlab-project'...
remote: Enumerating objects: 221, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 221 (delta 1), reused 3 (delta 0), pack-reused 215 (from 1)
Receiving objects: 100% (221/221), 36.30 KiB | 489.00 KiB/s, done.
Resolving deltas: 100% (122/122), done.
hubert@Huberts-MacBook-Pro jupyterlab-project % docker compose up -d
[+] up 4/4
 ✔ Network jupyterlab-project_default Created                                                                       0.0s
 ✔ Container redis                    Started                                                                       0.3s
 ✔ Container broker                   Started                                                                       0.3s
 ✔ Container jupyter                  Started                                                                       0.4s
hubert@Huberts-MacBook-Pro jupyterlab-project % docker compose ps
NAME      IMAGE                         COMMAND                  SERVICE   CREATED          STATUS                    PORTS
broker    confluentinc/cp-kafka:7.8.0   "/etc/confluent/dock…"   broker    11 seconds ago   Up 10 seconds             0.0.0.0:29092->29092/tcp, [::]:29092->29092/tcp
jupyter   jupyterlab-project-jupyter    "tini -g -- start.sh…"   jupyter   11 seconds ago   Up 10 seconds (healthy)   0.0.0.0:4040->4040/tcp, [::]:4040->4040/tcp, 0.0.0.0:8999->8888/tcp, [::]:8999->8888/tcp
redis     redis:7.2-alpine              "docker-entrypoint.s…"   redis     11 seconds ago   Up 10 seconds             0.0.0.0:6379->6379/tcp, [::]:6379->6379/tcp

## Task 4.3

Python: 3.11.10 | packaged by conda-forge | (main, Oct 16 2024, 01:19:04) [GCC 13.3.0]
Running inside: /opt/conda
Course environment is ready!

## Task 4.4
(base) jovyan@42f4aedab3ac:~/notebooks$ kafka-topics.sh --list --bootstrap-server broker:9092

(base) jovyan@42f4aedab3ac:~/notebooks$ 

## Task 4.5
docker compose down
[+] down 4/4
 ✔ Container jupyter                  Removed                                                                       0.6s
 ✔ Container redis                    Removed                                                                       0.2s
 ✔ Container broker                   Removed                                                                       0.8s
 ✔ Network jupyterlab-project_default Removed   
