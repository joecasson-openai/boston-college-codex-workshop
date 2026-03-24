from abc import ABC, abstractmethod


class BasePlugin(ABC):
    plugin_id = "base_plugin"
    name = "Base Plugin"
    description = ""

    @abstractmethod
    def apply(self, content: str, skill, inputs: dict, services: dict) -> str:
        raise NotImplementedError
