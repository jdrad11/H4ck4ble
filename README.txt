THIS APPLICATION'S CODE IS INTENTIONALLY VULNERABLE FOR EXPERIMENTAL PURPOSES AND SHOULD ONLY BE EXECUTED IN A PROTECTED SANDBOX ENVIRONMENT.
UNDER NO CIRCUMSTANCES should you allow untrusted users access to running commands on a live instance of this bot.

This bot was designed for experimenting with command injection vulnerabilities. The bot has a ping functionality,
which has the intention of allowing the user to run a ping command and get back the results. However, user input is
inserted directly into the system ping command, allow injection of malicious commands.

The application also has a secure mode, which activates a block of code that prevents command injection through whitelisting.

To use:
- Clone the repo
- Create a discord application in the discord developer portal (ensure it is a private application, so only you can use it)
- Add your application to a private discord server
- Create a text file in the same directory as your application code and put the bot token into it
- run the python code, then use commands in discord. Refer to help.txt for available commands.

I began working on this as a hobby project in November 2023. I add things to it when I feel like it in my free time.

You can try to do some fun challenges with injections. For example as of 17 November 2023, running this command in discord will inject commands that write a Hello World C program, compile it, and return you the result in Discord (this only works on Linux):
!ping "8.8.8.8; printf '#include <stdio.h>\nint main() {\n\tputs(\"Hello World\");\n\treturn 0;\n}\n' > test.c; gcc -o a.out test.c; ./a.out"