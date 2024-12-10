import os
import time
from PIL import ImageGrab
import applescript


actions = [
    {
        "type": "open_iterm",
        "delay_after": 5,
    },
    {
        "type": "set_iterm_window_size",
        "columns": 125,
        "rows": 29,
        "delay_after": 1/2,
    },
    {
        "type": "command",
        "command": "export DISABLE_AUTO_TITLE=true",
        "delay_after": 1/2,
    },
    {
        "type": "command",
        "command": r"echo -e '\033]50;SetProfile=Cockpit-Catppuccin-Frappe\007'",
        "delay_after": 1/2,
    },
    {
        "type": "set_palette",
        "palette": "default",
        "delay_after": 1,
    },
    {
        "type": "command",
        "command": r"echo -e '\033]0;Starship Cockpit Demo\007'",
        "delay_after": 1/2,
    },
    {
        "type": "command_list",
        "commands": [
            f"cd {os.getcwd()}",
            "git clone https://github.com/smithumble/starship-cockpit.git",
            "mv starship-cockpit starship-cockpit-demo",
            "cd starship-cockpit-demo",
            "touch docker-compose.yml",
            "export DOCKER_CONTEXT=dev",
        ],
        "command_delay": 1,
        "delay_after": 1/2,
    },
    {
        "type": "command",
        "command": "clear",
        "delay_after": 1/2,
    },
    {
        "type": "command_list",
        "commands": [
            "git reset --hard HEAD~1 -q",
            "echo 'Hello, World!' > NEW_FILE.md",
            "git add NEW_FILE.md",
            "git commit -m 'Add NEW_FILE.md' -q",
            "rm NEW_FILE.md",
            "echo 'Hello, World!' > README.md",
        ],
        "command_delay": 1,
        "delay_after": 1/2,
    },
    {
        "type": "command",
        "command": 'sleep 2',
        "delay_after": 3,
    },
    {
        "type": "command",
        "command": "test",
        "delay_after": 1/2,
    },
    {
        "type": "screenshot",
        "filepath": "assets/demo.png",
        "delay_before": 2,
        "delay_after": 1/2,
    },
    {
        "type": "set_iterm_window_size",
        "columns": 125,
        "rows": 5,
        "delay_after": 1/2,
    },
    {
        "type": "command",
        "command": "clear",
        "delay_after": 1/2,
    },
    {
        "type": "screenshot",
        "filepath": "assets/palettes/default.png",
        "delay_before": 2,
        "delay_after": 1/2,
    },
    {
        "type": "command",
        "command": r"echo -e '\033]50;SetProfile=Cockpit-Gruvbox-Dark\007'",
        "delay_after": 1/2,
    },
    {
        "type": "set_palette",
        "palette": "gruvbox_dark",
        "delay_after": 1,
    },
    {
        "type": "command",
        "command": r"echo -e '\033]0;Starship Cockpit Demo\007'",
        "delay_after": 1/2,
    },
    {
        "type": "command",
        "command": "clear",
        "delay_after": 1/2,
    },
    {
        "type": "screenshot",
        "filepath": "assets/palettes/gruvbox_dark.png",
        "delay_before": 2,
        "delay_after": 1/2,
    },
    {
        "type": "command",
        "command": r"echo -e '\033]50;SetProfile=Cockpit-Gruvbox-Light\007'",
        "delay_after": 1/2,
    },
    {
        "type": "set_palette",
        "palette": "gruvbox_light",
        "delay_after": 1,
    },
    {
        "type": "command",
        "command": r"echo -e '\033]0;Starship Cockpit Demo\007'",
        "delay_after": 1/2,
    },
    {
        "type": "command",
        "command": "clear",
        "delay_after": 1/2,
    },
    {
        "type": "screenshot",
        "filepath": "assets/palettes/gruvbox_light.png",
        "delay_before": 2,
        "delay_after": 1/2,
    },
    {
        "type": "command_list",
        "commands": [
            "cd ..",
            "rm -rf starship-cockpit-demo",
        ],
        "command_delay": 1,
        "delay_after": 1/2,
    },
    {
        "type": "set_palette",
        "palette": "default",
        "delay_after": 1,
    },
    {
        "type": "close_iterm",
        "delay_after": 2,
    },
]

def run_applescript(script, action_name="Unknown action"):
    try:
        result = applescript.run(script)
        if result.err:
            print(f"AppleScript Error in {action_name}: {result.err}")
            return None
        return result
    except Exception as e:
        print(f"Failed to execute {action_name}: {e}")
        return None

def format_action_details(action):
    return ' '.join(f'{k}="{v}"' for k, v in action.items())

def escape_command(command):
    command = command.replace('\\', '\\\\')
    return command

def run_actions():
    for action in actions:
        print(f"Running action: {format_action_details(action)}")
        
        delay_before = action.get("delay_before", 0)
        delay_after = action.get("delay_after", 0)

        time.sleep(delay_before)

        if action["type"] == "open_iterm":
            script = '''
            tell application "iTerm2"
                create window with default profile
            end tell
            '''
            run_applescript(script, "open_iterm")

        elif action["type"] == "set_iterm_window_size":
            script = f"""
            tell application "iTerm2"
                tell current window
                    tell current session
                        set columns to {action["columns"]}
                        set rows to {action["rows"]}
                    end tell
                end tell
            end tell
            """
            run_applescript(script, "set_iterm_window_size")

        elif action["type"] == "command":
            escaped_command = escape_command(action['command'])
            cmd_script = f"""
            tell application "iTerm2"
                tell current window
                    tell current session
                        write text "{escaped_command}"
                    end tell
                end tell
            end tell
            """
            run_applescript(cmd_script, f"command: {action['command']}")

        elif action["type"] == "command_list":
            for cmd in action["commands"]:
                escaped_command = escape_command(cmd)
                cmd_script = f"""
                tell application "iTerm2"
                    tell current window
                        tell current session
                            write text "{escaped_command}"
                        end tell
                    end tell
                end tell
                """
                run_applescript(cmd_script, f"command: {cmd}")
                time.sleep(action.get("command_delay", 0.5))  # Optional delay between commands

        elif action["type"] == "screenshot":
            bounds_script = """
            tell application "iTerm2"
                get bounds of window 1
            end tell
            """
            bounds = run_applescript(bounds_script, "get_bounds")
            if bounds:
                x, y, width, height = bounds.out.strip("{}").split(",")
                x, y, width, height = map(int, [x, y, width, height])

                screenshot = ImageGrab.grab(bbox=(x, y, width, height))
                screenshot.save(action["filepath"])

        elif action["type"] == "set_palette":
            palette_name = action["palette"]
            starship_config = "starship.toml"
            
            with open(starship_config, 'r') as file:
                content = file.readlines()
            
            for i, line in enumerate(content):
                if line.startswith("palette = "):
                    content[i] = f"palette = '{palette_name}'\n"
                    break
            
            with open(starship_config, 'w') as file:
                file.writelines(content)

        elif action["type"] == "close_iterm":
            script = """
            tell application "iTerm2"
                close window 1
            end tell
            """
            run_applescript(script, "close_iterm")

        time.sleep(delay_after)


if __name__ == "__main__":
    run_actions()
