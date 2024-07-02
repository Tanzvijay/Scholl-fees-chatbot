import streamlit as st


class SchoolFeeBot:
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    # Define the random questions and corresponding responses
    random_questions_responses = {
        "hi": "Hello! How can I assist you with your school fee queries today?",
        "how to pay school fees?": "You can pay your school fees online through the school's payment portal, by visiting the school's finance office, or via bank transfer. Please refer to your school's official communication for specific details.",
        "payment deadline for school fees?": "The payment deadlines for school fees vary by institution. Please check the academic calendar or contact the school's finance office for exact dates.",
        "late fee for school fees?": "Most schools charge a late fee for overdue payments. The amount varies, so please consult your school's fee policy or finance office for details.",
        "installment plans for school fees?": "Some schools offer installment plans to help manage school fee payments. Check with your school's finance office to see if this option is available and to learn about the terms and conditions.",
        "scholarship options?": "Many schools offer scholarships based on academic performance, financial need, or other criteria. Visit the school's scholarship office or website for more information and application procedures.",
        "financial aid for school fees?": "Financial aid is available at many institutions to assist with school fees. Contact the financial aid office to learn about available programs, eligibility criteria, and application processes.",
        "refund policy for school fees?": "The refund policy for school fees depends on the school's regulations. Generally, partial refunds may be available if you withdraw within a certain period. Check your school's refund policy for specific details.",
        "payment methods for school fees?": "School fees can typically be paid via credit card, debit card, bank transfer, or in person with cash or check. Confirm the accepted payment methods with your school's finance office.",
        "sponsored students": "If you are a sponsored student, ensure that your sponsor makes the payment by the due date. You may need to provide proof of sponsorship to the school's finance office.",
        "ty": "Is there anything else I can help you with?",
        "thank you": "You're welcome! Is there anything else I can assist you with?",
        "no thanks": "I'm happy to help. Have a wonderful day!"
    }

    def __init__(self):
        self.greeted = False  # To check if the user is already greeted

    def get_response(self, user_input):
        if user_input.lower() in self.exit_commands:
            return "Goodbye! Have a nice day.", True  # Return True to indicate the conversation is over

        for question, response in self.random_questions_responses.items():
            if question in user_input.lower():
                return response, False

        if user_input.lower() in self.negative_responses:
            return "Sorry , How can I assist you further?", False
        else:
            return "I'm not sure how to respond to that. Could you ask something else?", False

    def start_chat(self):
        if not self.greeted:
            st.write("Hi, I'm the SchoolFeesBot. I can help you with your school fee queries. Ask me a question!")
            self.greeted = True


# Create an instance of SchoolFeeBot
school_fee_bot = SchoolFeeBot()


# Streamlit app
def main():
    st.title("School Fee Bot")
    school_fee_bot.start_chat()

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You: ")
    if user_input:
        response, exit_chat = school_fee_bot.get_response(user_input)

        # Append user input and bot response to the chat history
        st.session_state.chat_history.append(f"You: {user_input}")
        st.session_state.chat_history.append(f"Bot: {response}")

        if exit_chat:
            st.session_state.chat_history.append("Bot: The chat has ended. Refresh the page to start a new chat.")

        # Display the chat history
        for chat in st.session_state.chat_history:
            st.write(chat)


if __name__ == "__main__":
    main()
