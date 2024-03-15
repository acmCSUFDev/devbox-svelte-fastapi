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
`process-compose.yml` file. You can navigate through the services with the arrow
keys or click on them with the mouse.
