import gradio as gr

# ------------------------------
# Function to update UI when personality changes
# ------------------------------
def update_ui(selected_personality):
    """
    This function updates:
    1. The round image in sidebar
    2. The chatbot avatar image
    3. The dynamic title
    """

    image = personalities[selected_personality]["image"]

    # Update title text dynamically
    new_title = f"# ChatBot of {selected_personality}"

    # Update chatbot avatar (assistant side only)
    return image, gr.Chatbot(avatar_images=(None, image)), new_title


# ------------------------------
# BUILD CHATGPT-STYLE UI
# ------------------------------
with gr.Blocks(
    title="Great Minds AI",
    theme=gr.themes.Base(),
    css="""
    /* Overall dark background */
    body {
        background-color: #0f172a;
    }

    .gradio-container {
        background-color: #0f172a !important;
    }

    /* Sidebar styling */
    .sidebar {
        background-color: #111827;
        padding: 20px;
        height: 100vh;
        border-right: 1px solid #1f2937;
    }

    /* Make avatar images circular */
    .chatbot img {
        border-radius: 50% !important;
        width: 40px !important;
        height: 40px !important;
    }

    /* Chat area styling */
    .chat-area {
        padding: 20px;
    }

    textarea {
        background-color: #1f2937 !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 12px !important;
    }

    label {
        color: #9ca3af !important;
    }
    """
) as page:

    # Create horizontal layout (Sidebar + Chat Area)
    with gr.Row():

        # ------------------------------
        # LEFT SIDEBAR
        # ------------------------------
        with gr.Column(scale=1, elem_classes="sidebar"):

            # Dynamic Title (Changes when personality changes)
            title = gr.Markdown("# ChatBot of Isaac Newton")

            # Round profile image display
            selected_image = gr.Image(
                value=personalities["Isaac Newton"]["image"],
                show_label=False,
                interactive=False,
                height=200
            )

            # Personality selection dropdown
            personality = gr.Dropdown(
                choices=list(personalities.keys()),
                value="Isaac Newton",
                label="Choose Personality"
            )

            # Creativity slider (controls temperature)
            creativity = gr.Slider(
                minimum=0,
                maximum=1,
                value=0.5,
                step=0.1,
                label="Creativity Level"
            )

        # ------------------------------
        # RIGHT CHAT SECTION
        # ------------------------------
        with gr.Column(scale=3, elem_classes="chat-area"):

            # Chatbot component with assistant avatar
            chatbot = gr.Chatbot(
                show_label=False,
                avatar_images=(
                    None,  # User avatar (default)
                    personalities["Isaac Newton"]["image"]  # Assistant avatar
                ),
                elem_classes="chatbot"
            )

            # Message input box
            msg = gr.Textbox(
                show_label=False,
                placeholder="Ask anything..."
            )

            # When user presses Enter
            msg.submit(
                chat,  # Your existing chat function
                inputs=[msg, chatbot, personality, creativity],
                outputs=[msg, chatbot]
            )

            # Clear button to reset conversation
            gr.ClearButton([chatbot, msg])

        # ------------------------------
        # UPDATE UI WHEN PERSONALITY CHANGES
        # ------------------------------
        personality.change(
            update_ui,
            inputs=personality,
            outputs=[selected_image, chatbot, title]
        )

# ------------------------------
# Launch the app
# ------------------------------
page.launch()