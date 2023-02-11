# install openai package
import openai


def print_hi():
    message = '''Hey There..
    I'm Jarvesh. Your personal assistant.
    Ask me anything. and if you want to stop, than just type "exit"'''
    print(message)

    openai.api_key = "YOUR API KEY"
    model_engine = "text-davinci-003"
    while True:
        prompt = input(': ')
        if prompt == "exit":
            break

        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completion.choices[0].text
        print(response)


if __name__ == '__main__':
    print_hi()
