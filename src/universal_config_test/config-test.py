
from config.pipeline_config import PipelineConfig

config = PipelineConfig()

if __name__ == '__main__':
    import os
    os.environ["KRAUSENING_BASE"] = "./src/universal_config_test/krausening/base/"

    print(config.auth_token)
