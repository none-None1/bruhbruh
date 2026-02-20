This is an interpreter for the esolang [bruh():bruh()](https://esolangs.org/wiki/Bruh():bruh()).

It uses the `bruh2py` function to translate bruh():bruh() to Python, and then executes the Python code via the `exec` function.

Built-in functions are implemented in `bruhlib.py`, so make sure it can be imported when running code.

This interpreter does **NOT** implement syntax errors, so **beware of untrusted bruh():bruh() programs (Any Python code can be injected)**. Therefore, you have to confirm before executing a program, the original and translated code will be shown.

There are also some examples which can be found on [the page on esolangs.org](https://esolangs.org/wiki/Bruh():bruh()) as well. There's also an example `inject.br` which demonstrates how easy it is to inject Python code in this interpreter 