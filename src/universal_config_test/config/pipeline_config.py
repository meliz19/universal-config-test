from krausening.properties import PropertyManager
import os

class PipelineConfig:
    """
    Configurations for this pipeline, read from the pipeline properties file.
    """

    def __init__(self):
        self.properties = PropertyManager.get_instance().get_properties("properties.properties")

    @property
    def auth_token(self) -> str:
        auth_token = self.properties["auth.token"]
        environ_override = os.getenv("AUTH_TOKEN")
        auth_token = environ_override if environ_override else auth_token
        return auth_token.strip()
