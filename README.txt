THIS APPLICATION'S CODE IS INTENTIONALLY VULNERABLE FOR EXPERIMENTAL PURPOSES AND SHOULD ONLY BE EXECUTED IN A PROTECTED SANDBOX ENVIRONMENT.
UNDER NO CIRCUMSTANCES should you allow untrusted users access to running commands on a live instance of this bot.

This bot was designed for experimenting with command injection vulnerabilities. The bot has a ping functionality, which has the intention of allowing the user to run a ping command and get back the results. However, user input is inserted directly into the system ping command, allowing injection of malicious commands.

The application also has a secure mode, which activates a block of code that prevents command injection through whitelisting. This is only for experimenting with protection against command injection, and does not actually make the bot more secure, as it can be turned off at any time by anyone able to run commands on the bot.

This code utilizes Python's os.system() function to run operating system commands. The commands currently in the code are for Windows's cmd.exe. If you are running the bot using a different command line, you will need to change the system commands in the code accordingly.

To use:
- Clone the repo
- Create a discord application in the discord developer portal (ensure it is a private application, so only you can use it)
- Add your application to a private discord server
- Create a text file named token.txt in the same directory as the application code and put the bot token into it
- Run the python code, then use commands in discord. Refer to help.txt for available commands.

I began working on this as a hobby project in November 2023. I add things to it when I feel like it in my free time.

You can try to do some fun challenges with injections. For example as of 17 November 2023, running this command in discord will inject commands that write a Hello World C program, compile it, and return you the result in Discord (this only works on Linux):
!ping "8.8.8.8; printf '#include <stdio.h>\nint main() {\n\tputs(\"Hello World\");\n\treturn 0;\n}\n' > test.c; gcc -o a.out test.c; ./a.out"