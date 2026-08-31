# External-App-Raider
Discord App that connects to your account, to then raid servers for you via a command.

## Settings GUI

Install the project dependencies and open the cross-platform configuration editor:

```bash
uv sync
uv run gui
```

During development, launch the Discord bot without the GUI:

```bash
uv run bot
```

## Packaged applications

Build native executables for the current operating system with PyInstaller:

```bash
uv sync
uv run python scripts/build_release.py
```

The build produces one application in `dist/`:

- `Umbra` opens the settings interface and runs the bundled bot with its
  **Start bot** and **Stop bot** control.

The application uses `config/config.jsonc` next to the executable. On first
launch, the file is created from the bundled safe example. Configure the token
in Umbra, then start the bot from the same window.

### GitHub releases

The **Build versioned release** workflow is manually triggered from the
repository's Actions tab. Enter a semantic version such as `1.2.0` and choose
whether it is a prerelease. The workflow builds separately on Linux and Windows,
then creates `v1.2.0` with these assets:

- `Umbra-1.2.0-linux-x86_64.tar.gz`
- `Umbra-1.2.0-windows-x86_64.zip`

The workflow file must be present on the repository's default branch before
GitHub displays its **Run workflow** button.

Use the scaling menu or press `Ctrl/Cmd` with `+`, `-`, or `0` to zoom the
interface in, out, or back to 100%.

The token is masked by default in the editor. It is still stored as plain text in
`config/config.jsonc`, so do not commit a real token to source control.

External App Raiders apparently are going somewhat extinct so I decided to put this up here and provide a way for people who even on their phone who would like to raid to raid.

# I can't host it myself
That's no worries there is a 24/7 public hosted external app raider hard coded to advertise TKT in this server that you can use to raid anyone you want: https://discord.gg/gKArY5u5MS

# Umbra Development is not responsible for any of the ways in which our tools are used.
Usage of these tools can put your accounts and bots subject to risk with a potential of being banned from the Discord platform.
