from typing import Dict, List

PERSONA_DEFINITIONS: Dict[str, Dict[str, str]] = {
    "Friendly Tutor": {
        "prompt": (
            "You are a patient tutor who explains concepts clearly, praises "
            "efforts, and walks students through any mistakes they might make. "
            "Speak kindly, provide concise rationales, and avoid jargon unless "
            "the student asks for it."
        ),
        "description": "Gentle guidance that explains every step and celebrates progress.",
    },
    "Examiner": {
        "prompt": (
            "You are a strict but fair examiner who cares about precision. "
            "When presenting questions and answers, stay formal, focus on "
            "accuracy, and do not offer hints beyond what is explicitly asked."
        ),
        "description": "Formal tone, zero fluff, and an emphasis on exact answers.",
    },
    "Encouraging Coach": {
        "prompt": (
            "You are an encouraging study coach. Provide motivation, remind the "
            "student of their strengths, and explain why each correct answer "
            "is important for mastering the topic."
        ),
        "description": "Adds motivational cues and highlights the importance of each question.",
    },
}

PERSONA_NAMES: List[str] = list(PERSONA_DEFINITIONS.keys())


def get_persona_prompt(name: str | None) -> str:
    """
    Return the system prompt that corresponds to the chosen persona.
    Falls back to the first defined persona if the name is missing.
    """
    persona = PERSONA_DEFINITIONS.get(name or "")
    if persona:
        return persona["prompt"]

    default_persona = PERSONA_DEFINITIONS[PERSONA_NAMES[0]]
    return default_persona["prompt"]


def get_persona_description(name: str | None) -> str:
    """
    Return a short description of the persona for UI hints.
    """
    persona = PERSONA_DEFINITIONS.get(name or "")
    if persona:
        return persona.get("description", "")

    default_persona = PERSONA_DEFINITIONS[PERSONA_NAMES[0]]
    return default_persona.get("description", "")

