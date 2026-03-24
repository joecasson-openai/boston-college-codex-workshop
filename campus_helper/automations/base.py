from abc import ABC, abstractmethod


class BaseAutomation(ABC):
    automation_id = "base_automation"
    name = "Base Automation"
    description = ""
    input_fields = []

    @abstractmethod
    def run(self, inputs: dict, services: dict) -> str:
        raise NotImplementedError
