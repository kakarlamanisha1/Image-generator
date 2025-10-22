import streamlit as st
import openai
import base64
import os
from openai import OpenAI

def main():
    st.title("DALL·E 3 Image Generator")

    # api_key = st.text_input("Enter your OpenAI API key:", type="password")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    prompt = st.text_area("Enter your image prompt:")

    if st.button("Generate Image") and api_key and prompt:
        client = openai.OpenAI(api_key=api_key)
        with st.spinner("Generating image..."):
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