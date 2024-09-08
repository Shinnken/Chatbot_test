import logging
from openai import OpenAIError, BadRequestError, OpenAI, completions

api_key = ""


class OpenAIBot:
    def __init__(self, engine):
        # Initialize conversation with a system message
        self.conversation = [{"role": "system", "content": "You are a helpful assistant."}]
        self.engine = engine
        self.client = OpenAI()
        self.client.api_key = api_key

    def add_message(self, role, content):
        # Adds a message to the conversation.
        self.conversation.append({"role": role, "content": content})

    def generate_response(self, prompt):
        # Add user prompt to conversation
        self.add_message("user", prompt)
        try:
            conversation_str = "\n".join([f"{msg['role']}: {msg['content']}" for msg in self.conversation])

            # Make a request to the API using the chat-based endpoint with conversation context
            response = self.client.chat.completions.create(
                model=self.engine,
                messages=self.conversation)         # Extract the response
            message = completions.choices[0].message.content 
            assistant_response = response.choices[0].text.strip()
            # Add assistant response to conversation
            self.add_message("assistant", assistant_response)
            # Return the response
            return message
        except BadRequestError as e:
            logging.error(f"OpenAI API error: {e}")
        except OpenAIError as e:
            logging.error(f"General OpenAI error: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
        return "Error Generating Response!"