import streamlit as st
import openai
import base64
import os
from dotenv import load_dotenv

# Load .env file if present (for local development)
load_dotenv()

def main():
    st.title("🖼️ DALL·E 3 Image Generator")

    # Get the OpenAI API key from environment
    api_key = os.getenv("OPENAI_API_KEY")

    # Prompt input
    prompt = st.text_area("Enter your image prompt:")

    if st.button("Generate Image"):
        if not api_key:
            st.error("❌ OpenAI API key not found. Please set OPENAI_API_KEY as an environment variable.")
            return
        if not prompt:
            st.warning("⚠️ Please enter a prompt.")
            return

        client = openai.OpenAI(api_key=api_key)

        with st.spinner("🎨 Generating image..."):
            try:
                result = client.images.generate(
                    model="gpt-image-1",
                    prompt=prompt,
                    size="1024x1024",
                    quality="high",
                    n=1
                )
                image_base64 = result.data[0].b64_json
                image_bytes = base64.b64decode(image_base64)
                st.image(image_bytes, caption="Generated Image", use_container_width=True)
            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
