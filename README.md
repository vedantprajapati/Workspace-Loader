# Workspace Loader

Application that automatically loads specified apps all at once, to let user start work as soon as they can

## Usage

Clone this repository and simply modify save.txt to links to shortcuts that you intend to launch.

### Save.txt:
```
C:/app1.exe,C:/app2.exe,C:/folder1
```

### Libraries needed:
```python
pip install tkinter 
pip install os

import tkinter as tk
from tkinter import filedialog, Text
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
