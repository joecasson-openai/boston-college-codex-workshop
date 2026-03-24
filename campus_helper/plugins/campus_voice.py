from campus_helper.plugins.base import BasePlugin


class CampusVoicePlugin(BasePlugin):
    plugin_id = "campus_voice"
    name = "Campus Voice Plugin"
    description = "Adds a visible wrap-up section so outputs feel more polished."

    def apply(self, content: str, skill, inputs: dict, services: dict) -> str:
        return f"""
> Campus Helper polish layer enabled for **{skill.name}**

{content}

### Quick share-out
- What part feels ready to demo?
- What would your team improve next with Codex?
""".strip()
