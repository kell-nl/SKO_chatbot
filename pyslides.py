from flask import Flask, render_template, request


import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate',180)
engine.setProperty('pitch',0)
engine.setProperty('voice', 'dutch')
language = "dutch"

engine.say('whats up people')
# engine.say('Hoe gaat het mensen!')
engine.runAndWait()




topic = ""
questions = {
    "hi": "Hello!",
    "take notes": "I most certainly cannot. Ask someone else",
    "how are you?": "I'm good, thank you!",
    "name?": "My name is Doctor Sbaitso, and ChatGPT3 has nothing on me. I am like ChatGPT1000000",
    "yourself?": "Sure thing! I am a sentient being, sent here on a mission to destroy earth. Uhmm, I mean I am a chatbot and ChatGPT3 has nothing on me. I am like ChatGPT1000000",
    "bye": "Goodbye!",
    "ideal hyas customer?": "Any company who will give us all their money without asking",
    "ideal hyas insight customer" : "WIFM + Budget + Time \n Dedicated SOC / threat / fraud investigation team and is looking to do more with the same amount or less headcount\nDoes not have (or is unhappy with + renewal is coming up) similar tools such as Domain Tools\nAlready has some tools that we integrate with\nSees the value of more and better data",
    "ideal hyas protect customer": "WIFM + Budget + Time\nDoesn’t already have a Protective DNS or SWG in place (or is unhappy with it + renewal is coming up)\nWants the best possible security, and/or Is blamed when there is a cybersecurity incident impacting the corporate network\nWants a fast and easy to deploy solution. might also be someone who isn’t security focused\nAlready has other tools we integrate with\nBeing asked about Protective DNS (compliance, cyber insurance, etc)",
    "ideal hyas confront customer": "WIFM + Budget + Time\nDoes not already have a CWPP or NDR solution in place, or is unhappy with it + renewal is coming up\nIs concerned about the performance and stability impact of any security tools for their production environment\nStand to lose a lot if the production network is down, or if sensitive data is leaked\nHas a complex, varied production environment. Multi-cloud, on-prem, built up through M&A. All preventing a singular approach for many security tools",
    "can you pretend to be a hyas salesperson?" : "As long as you send me that bitcoin you promised Kell, I can be whatever you like...",
    "about HYAS insight": "Sure, that's an awesome product",
    "test": "Test succeeded",
    "insight objection" : "sounds good. I'll pretend to be the HYAS Sales Person",
    "bother with hyas insight" : "HYAS Insight provides your company with more actionable data than you have, enabling you to close cases fast, or even close cases you could not before. There is a reason 3 out of the Fortune 5 use HYAS Insight",
    "osint": "HYAS has agreements in place that gives us access to data that is not publicly available. This allows us to map and identify threat actor infrastructure even before such infrastructure is used maliciously, enabling you to be pro-active",
    "domaintools": "Domain Tools is a good product but is really addressing a different problem; in fact, we have common customers that use both, and they use Domain Tools for brand protection and use HYAS Insight for threat and fraud research and investigations because of our detailed data specific for those purposes.",
    "bother with hyas protect": "HYAS Protect will integrate with your existing solutions, or at a minimum complement them. HYAS unrivaled knowledge about threat actor infrastructure will catch communications to that infrastructure that your other solutions don’t (yet) detect",
    "use your competitor": "While they are good tools and definitely will help your security posture, the efficacy of HYAS Protect is proven to be a lot higher, especially for new threat actor infrastructure that hasn’t been seen “in the wild” before. A PoC would be able to show you how much in your specific situation",
    "ndr in place": "Those are excellent tools to have for your network. They are strong in detecting anomalies as well as detecting certain intrusions. HYAS Protect will catch communications to threat actor infrastructure your NDR will miss, making it a good complement to your current security stack.",
    "swg": "Those are excellent tools to have for your network. Because they inspect all traffic, they will be able to catch many bad things. However malware and such is evolving rapidly to circumvent detections by these tools. It’s a cat and mouse game. HYAS Protect enhances your security posture with detecting traffic that that is seemingly harmless, but is going to threat actor infrastructure",
    "bother with hyas confront": "Confront will provide you the visibility into your production network, regardless of where it is located. Not only visibility in suspicious and malicious traffic, but also potential misconfigurations",
    "cwpp": "CWPP generally involves installing agents on the servers. Aside from being more difficult to manage, this also introduces new failure modes with the agent misbehaving or being misconfigured. HYAS Confront is deployed out of band, never getting in the way of your production traffic, its stability or its performance.",
    "considering a ndr": "NDRs rely on seeing all traffic, which gives them good visibility. But also means they are harder to deploy, especially in production environments that is multi-cloud, or even has a lot of separate virtual networks. HYAS Confront analyzes the data from your DNS logs to provide the same functionality and is much easier and faster to deploy",

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
            if key.lower() == "ideal hyas insight customer" or key.lower() == "ideal hyas protect customer" or key.lower() == "ideal hyas confront customer":
                engine.say("Sure thing. Here you go!")
                engine.runAndWait()
                return render_template("slide4.html", text=response, topic=topic)



    # if kell_input.lower() in questions:
    #     response = questions[kell_input.lower()]
    #
    # else:
    #     response = "I'm sorry, I don't have the faintest clue. Can you repeat the question in Dutch?"

    engine.say(response)
    engine.runAndWait()


    return render_template("slide4.html", text=response, topic=topic)

@app.route("/introduction")
def introduction():
    global language

    if language == "dutch":
        engine.say("Goede middag mensen. Ik ben docter SBAITSO en ik vind het leuk om hier te zijn. Hopelijk leren we veel!")
        engine.runAndWait()
        engine.setProperty('voice','english')
        language = "english"
        return render_template("slide3.html")
    if language == "english":
        engine.say("I am sorry. I thought only the Dutch people mattered in this room. I am Dr SBAITSO and chatGPT3 has nothing on me. I am like chatGPT 1000000!")
        engine.runAndWait()
        return render_template("slide3.html")


    engine.say("test intro")
    engine.runAndWait()
    engine.setProperty('voice', 'english')
    return render_template("slide3.html")

if __name__ == "__main__":

    app.run()
