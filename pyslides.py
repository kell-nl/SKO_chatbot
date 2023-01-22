from flask import Flask, render_template, request


import pyttsx3

engine = pyttsx3.init()

# engine.say('whats up')
# engine.runAndWait()

topic = ""

questions = {
    "hi": "Hello!",
    "how are you?": "I'm good, thank you!",
    "name?": "My name is Doctor Sbaitso, and ChatGPT3 has nothing on me. I am like ChatGPT1000000",
    "yourself?": "Sure thing! I am a sentient being, sent here on a mission to destroy earth. Uhmm, I mean I am a chatbot and ChatGPT3 has nothing on me. I am like ChatGPT1000000",
    "bye": "Goodbye!",
    "ideal hyas customer?": "Any company who will give us all their money without asking",
    "ideal hyas insight customer" : "WIFM + Budget + Time \n Dedicated SOC / threat / fraud investigation team and is looking to do more with the same amount or less headcount\nDoes not have (or is unhappy with + renewal is coming up) similar tools such as Domain Tools\nAlready has some tools that we integrate with\nSees the value of more and better data",
    "can you pretend to be a hyas salesperson?" : "As long as you send me that bitcoin you promised Kell, I can be whatever you like...",
    "why should i bother with insight?" : "HYAS Insight provides your company with more actionable data than you currently have, enabling you to close cases faster, or even close cases you couldn't before",
    "about HYAS insight": "Sure, that's an awesome product",
    "test": "Test succeeded",
    "insight objection" : "sounds good. I'll pretend to be the HYAS Sales Person",
    "bother with hyas insight" : "HYAS Insight provides your company with more actionable data than you have, enabling you to close cases fast, or even close cases you could not before. There is a reason 3 out of the Fortune 5 use HYAS Insight",
    "osint": "HYAS has agreements in place that gives us access to data that is not publicly available. This allows us to map and identify threat actor infrastructure even before such infrastructure is used maliciously, enabling you to be pro-active",
    "domaintools": "Domain Tools is a good product but is really addressing a different problem; in fact, we have common customers that use both, and they use Domain Tools for brand protection and use HYAS Insight for threat and fraud research and investigations because of our detailed data specific for those purposes.",



}

app = Flask(__name__, static_folder='static')

slides = ["slide1.html", "slide2.html", "slide3.html"]
current_slide = 0

@app.route("/")
def index():
    return render_template("slide1.html")

@app.route("/slide2")
def slide2():
    return render_template("slide2.html")

@app.route("/slide3")
def slide3():
    return render_template("slide3.html")

@app.route("/slide4")
def slide4():

    return render_template("slide4.html", text='')


@app.route("/input_text", methods=["POST"])
def input_text():
    global topic
    kell_input = request.form["text"]
    response = "I have no clue what you are talking about. Can you repeat the question in Dutch?"
    for key, value in questions.items():
        if key.lower() in kell_input.lower():
            response = value
            if key.lower() == "about hyas insight":
                topic = "HYAS Insight"


    # if kell_input.lower() in questions:
    #     response = questions[kell_input.lower()]
    #
    # else:
    #     response = "I'm sorry, I don't have the faintest clue. Can you repeat the question in Dutch?"

    # engine.say(response)
    engine.runAndWait()


    return render_template("slide4.html", text=response, topic=topic)

@app.route("/introduction")
def introduction():
    engine.say("test intro")
    engine.runAndWait()

    return render_template("slide3.html")

if __name__ == "__main__":

    app.run()
