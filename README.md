# devbox-svelte-fastapi

Svelte + FastAPI example project using Devbox to bootstrap the development
environment.

## Goal

This repository was created to demonstrate Devbox's capabilities to bootstrap a
development environment for a Svelte + FastAPI project. It serves as a more
advanced example for ACM at CSUF's Devbox Workshop.

## Prerequisite

Before you start, you will need to install Devbox. You can refer to their
[Installing Devbox](https://www.jetpack.io/devbox/docs/installing_devbox/) guide,
but the following command should work for most users:

```sh
curl -fsSL https://get.jetpack.io/devbox | bash
```

If you already have Nix, simply enter a Nix shell with the `devbox` package.

## Developing

To start developing this project, simply run the following command:

```sh
devbox shell
```

This will drop you into a subshell with all the runtime dependencies, Python
dependencies and Node.js dependencies installed. From here, you can start
running the FastAPI server and the Svelte development server.

## Running

Devbox provides a service manager to start and stop services. These are
declared in the `process-compose.yml` file. In this project, the file defines
a service for `uvicorn` (FastAPI) and `vite` (Svelte).

To start the services, run the following command:

```sh
devbox services up
```

This will open up a terminal UI that lists all the services defined in the
`process-compose.yml` file:

<div align="center">
  <img alt="image" width="800" src="https://github.com/acmCSUFDev/devbox-svelte-fastapi/assets/8463786/54600456-2a15-4968-af7c-20f6a4c4c89e" />
</div>

You can navigate through the services with the arrow
keys or click on them with the mouse.

To exit the UI, simply press <kbd>Ctrl</kbd> + <kbd>C</kbd> as you would normally.

## Into Devbox

This section is a brief introduction to Devbox. It will cover the basics of
Devbox, such as adding packages and starting a shell.

### How is this compared to Nix?

Keen observers might notice that Devbox uses Nix under the hood. The main
advantage with using Devbox over Nix Shell/Flake is that **Devbox does not
require you to know Nix, nor does it require any Nix files**.

You get all the benefits of Nix, such as reproducibility and isolation, without
needing to learn Nix. This makes Devbox a great tool for teams that aren't
interested in getting into Nix or simply want to get up and running quickly.

### Adding Packages

Within the Devbox shell, we get access to the `devbox` CLI, which provides us
with 2 very convenient commands: `devbox search` and `devbox add`.

First, we can use `devbox search` to search for a package. For example, if we
run `devbox search httpie`, we will see a list of packages that match the
search term:

```
―❤―▶ devbox search httpie
Found 9+ results for "httpie":

* httpie  (3.2.2, 3.2.1, 3.1.0, 3.0.2, 2.6.0, 2.5.0, 2.4.0, 2.2.0, 2.1.0)
* python39Packages.httpie  (3.2.1)
* python310Packages.httpie  (3.2.2, 3.2.1)
* python311Packages.httpie  (3.2.2, 3.2.1)
* python312Packages.httpie  (3.2.2)
* python39Packages.httpie-ntlm  (1.0.2)
* python310Packages.httpie-ntlm  (1.0.2)
* python311Packages.httpie-ntlm  (1.0.2)
* python312Packages.httpie-ntlm  (1.0.2)
```

We can then use `devbox add` to add the package to our environment:

```
―❤―▶ devbox add httpie
Info: Adding package "httpie@latest" to devbox.json
[1/5] python310
[1/5] python310: Success
[2/5] python310Packages.pip
[2/5] python310Packages.pip: Success
[3/5] nodejs_21
[3/5] nodejs_21: Success
[4/5] pyright
[4/5] pyright: Success
[5/5] httpie
[5/5] httpie: Success
✓ Computed the Devbox environment.
Warning: Your shell environment may be out of date. Run `refresh` to update it.
```

Then, we can run `refresh` to update our environment. This will install the
`httpie` package into our current environment. Future `devbox shell`
invocations will have `httpie` available.

> [!TIP]
> If you look at the `git diff`, you'll see that our `devbox` tool has modified
> its JSON file to remember this:
>
> ```diff
> diff --git a/devbox.json b/devbox.json
> index be556ec..bf72391 100644
> --- a/devbox.json
> +++ b/devbox.json
> @@ -3,7 +3,8 @@
>      "python@3.10",
>      "python310Packages.pip",
>      "nodejs@latest",
> -    "pyright@latest"
> +    "pyright@latest",
> +    "httpie@latest"
>    ],
>    "shell": {
>      "init_hook": [
> ```
>
> This is how Devbox remembers the state of your environment for future
> invocations.

> [!NOTE]
> Devbox's [Quickstart](https://www.jetpack.io/devbox/docs/quickstart/) guide
> goes into more detail about this.
