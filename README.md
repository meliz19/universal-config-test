This is a simple example of how to implement [Krausening](https://github.com/TechnologyBrewery/krausening) within a docker container.

# Layout
- `./config` stores the `pipeline_config.py`, which Krausening requires to read in the property files. Each property must be defined within this file. This file can be located anywhere within your project. You just need to reference it from within your source files.
- `./krausening/base` stores the `.properties` file. This file can be stored anywhere, but make sure to update the `KRAUSENING_BASE` environment variable within your local environment, or, in this case, the `docker/Dockerfile`.

