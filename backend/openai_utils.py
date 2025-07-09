import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_code(code: str) -> str:
    """
    Uses OpenAI GPT to explain what the code does.
    """
    prompt = f"""
    Explain this Python code in simple terms.

    Code:
    {code[:3000]}  # Limit length for token safety
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a helpful Python assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error summarizing: {e}"
