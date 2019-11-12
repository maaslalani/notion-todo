# Notion Todo

Notion Todo is a command line interface tool that allows you to write, edit, remove todos right from the command line.

### How it works
Notion doesn't have an official API yet, but I use an [Unoffical Python API client.](https://github.com/jamalex/notion-py)

The CLI simply allows you to interact with a page and syncs it with notion so any edits you make on notion are reflected in the CLI and vice-versa

### Demonstration
![](demonstration.gif)

### Usage
The notion-todo-cli has a few commands

Listing todos
```
ntodo
ntodo list
```
These command will list out all your current todos for you to view them. Here you can check or uncheck the todos using the left and right arrow keys. Navigate using the up and down arrow keys.

Adding todos
```
ntodo add [Do something]
```
The `add` command allows you to add a todo to your notion page. You can quickly jot the todo down by simply following the command with the todo or simply write `ntodo add` (without anything following it) which will open your `$EDITOR` where you can write your todo. Once you save and exit the todo will be added.

Editing todos
```
ntodo edit
```
Typing this command will show you all of you todos to easily select one of them. Once you select one, it will appear in your `$EDITOR` for editing. Once you save and exit the todo will be updated.

Removing todos
```
ntodo remove
```
Typing this command will show you all of the todos where you can select one of them. After selecting one, it will confirm that you want to delete it. if you press `y` it will be deleted from your notion page.

### Setup
To set notion-todo to work with your notion setup you'll need to do 2 things.

1. Setup your `NOTION_TOKEN`
To setup your `NOTION_TOKEN` you need to go to [notion.so](https://www.notion.so) on your browser. Then, go into developer tools through inspect element and press the Application tab. In the sidebar you should see cookies, look for `token_v2` copy and paste that value into your environment variables as such. The python script will read the token from the environment.

```
export NOTION_TOKEN=your_token_v2_value_its_pretty_long
```

2. Setup your `NOTION_PAGE`
For this all you need to do is create a page (or use an existing one) as your todos page. All you need to do is copy the link to your page and export it as an environment variable, which the python script will read.

```
export NOTION_PAGE=https://www.notion.so/username/c1f350b7dfe0b7f8849e3f740e64520
```

You can use this tool by running the python script or bundling it into an executable file.
