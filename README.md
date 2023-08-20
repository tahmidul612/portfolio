# Personal Portfolio Website

The source code for my personal [tahmidul612.com](https://tahmidul612.com) homepage. Built with Hugo with the Congo theme.

## Getting Started

### Prerequisites

Install Hugo, Yarn and NodeJS

> On Windows

```console
winget install OpenJS.NodeJS
winget install Yarn.Yarn
winget install Hugo.Hugo.Extended
```

### Setup project

Clone the repo and change to the project directory

```console
git clone https://github.com/tahmidul612/portfolio.git
cd portfolio
```

Install project dependencies

```console
yarn
```

> Installs prettier and prettier-plugin-go-template

Install recommended vscode extensions

```console
(Get-Content -Path .\.vscode\extensions.json | ConvertFrom-Json).recommendations | Foreach -Process {code --install-extension $_ --force} | Select-String -Pattern "\[lua\]*" -NotMatch
```

> Run this command in powershell to install the recommended extensions
>
> Or, install the recommended extensions from the vscode prompt

Hit `F5` to launch the project in a browser window (refreshes when source is edited) or `Ctrl + Shift + B` to build static files

> Or, Run `hugo server` to serve project or `hugo` to build static files
