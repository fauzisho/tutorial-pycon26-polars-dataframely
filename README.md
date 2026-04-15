# Polars + Dataframely tutorial at PyCon / PyData 2026

Welcome to the polars + dataframely tutorial!

## Preparation: Setup your machine before the tutorial

### Required

We use the `pixi` package manager, which is backed by the `conda-forge` ecosystem. Please install it as described [here](https://pixi.prefix.dev/latest/installation/). For most people, this boils down to one of:

```bash
# Mac via brew
brew install pixi

# Mac / Linux
curl -fsSL https://pixi.sh/install.sh | sh
```

For windows, refer to the link above.

You can then install the local environment, as well as the local code:

```bash
pixi run postinstall
```

And validate your setup by executing a simple code example:

```bash
pixi run hello-world
```

Whenever you want to run any code in this tutorial, use `pixi run python your_code.py`.

### Optional but useful

If you want to be able to have polars draw pretty query graphs for you, install graphviz:

```bash
brew install graphviz
```

(or see https://graphviz.org/download/ for other systems)