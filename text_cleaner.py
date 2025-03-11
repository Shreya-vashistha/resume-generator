# utils/text_cleaner.py

def clean_resume_text(text):
    """
    Replace generic placeholders in the resume text with personalized prompts.
    """
    replacements = {
        "[Add Email Address]": "[Your Email Address]",
        "[Add Phone Number]": "[Your Phone Number]",
        "[Add LinkedIn Profile URL (optional)]": "[Your LinkedIn URL (optional)]",
        "[University Name]": "[Your University Name]",
        "[Graduation Year]": "[Your Graduation Year]",
    }
    for placeholder, prompt in replacements.items():
        text = text.replace(placeholder, prompt)
    return text
