from abc import ABC, abstractmethod


class BaseSkill(ABC):
    skill_id = "base"
    name = "Base Skill"
    description = ""
    next_prompt_hint = "Ask Codex to improve this skill."
    input_fields = []

    @abstractmethod
    def run(self, inputs: dict, services: dict) -> str:
        raise NotImplementedError
