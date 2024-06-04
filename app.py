from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Sample quotes
quotes = {
    "programming": [
        "Programs must be written for people to read, and only incidentally for machines to execute.",
        "The most disastrous thing that you can ever learn is your first programming language.",
        "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
        "Programming isn't about what you know; it's about what you can figure out.",
        "The art of programming is the skill of controlling complexity.",
        "The best thing about a boolean is even if you are wrong, you are only off by a bit.",
        "Walking on water and developing software from a specification are easy if both are frozen.",
        "Programming is like sex. One mistake and you have to support it for the rest of your life.",
        "Debugging is like hunting elephants. You rarely ever do it on the first shot.",
        "In software, the only numbers that matter are 0, 1, and infinity.",
        "The code you write makes you a programmer. The code you delete makes you a good one.",
        "There are only two hard things in computer science: cache invalidation and naming things.",
        "The best code is no code at all.",
        "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live.",
        "Programming is not about typing, it's about thinking.",
        "The most important property of a program is whether it accomplishes the intention of its user.",
        "Optimism is an occupational hazard of programming: feedback is the treatment.",
        "Programming today is a race between software engineers striving to build bigger and better idiot-proof programs, and the Universe trying to produce bigger and better idiots. So far, the Universe is winning.",
        "If debugging is the process of removing software bugs, then programming must be the process of putting them in.",
        "Computer science education cannot make anybody an expert programmer any more than studying brushes and pigment can make somebody an expert painter."
        "Without requirements or design, programming is the art of adding bugs to an empty text file.",
        "Software is like sex: it's better when it's free.",
        "Documentation is like sex; when it's good, it's very good, and when it's bad, it's better than nothing.",
        "Code never lies, comments sometimes do.",
        "Programming is thinking, not typing.",
        "Real programmers can write assembly code in any language.",
        "The only way to learn a new programming language is by writing programs in it.",
        "Good code is its own best documentation. As you're about to add a comment, ask yourself, 'How can I improve the code so that this comment isn't needed?'",
        "The most important skill for a programmer is not knowledge of specific programming languages, but the ability to effectively learn new ones.",
        "The three most dangerous things in the world are a programmer with a soldering iron, a hardware engineer with a software patch, and a user with an idea."
    ],
    "love": [
        "Love all, trust a few, do wrong to none.",
        "You call it madness, but I call it love.",
        "We are shaped and fashioned by what we love.",
        "Love is composed of a single soul inhabiting two bodies.",
        "The best thing to hold onto in life is each other.",
        "Love is friendship that has caught fire.",
        "The greatest happiness of life is the conviction that we are loved; loved for ourselves, or rather, loved in spite of ourselves.",
        "Love is like the wind, you can't see it but you can feel it.",
        "You know you're in love when you can't fall asleep because reality is finally better than your dreams.",
        "Love isn't something you find. Love is something that finds you.",
        "A successful marriage requires falling in love many times, always with the same person.",
        "The best and most beautiful things in this world cannot be seen or even heard, but must be felt with the heart.",
        "Love is when the other person's happiness is more important than your own.",
        "Being deeply loved by someone gives you strength, while loving someone deeply gives you courage.",
        "Love is an irresistible desire to be irresistibly desired.",
        "I have found the paradox, that if you love until it hurts, there can be no more hurt, only more love.",
        "To love and be loved is to feel the sun from both sides.",
        "Love is a game that two can play and both win.",
        "Love cures people—both the ones who give it and the ones who receive it.",
        "Love is an endless act of forgiveness. Forgiveness is the key to action and freedom.",
        "Love is like war: easy to begin but very hard to stop.",
        "Love is when you meet someone who tells you something new about yourself.",
        "Love is not finding someone to live with. It's finding someone you can't live without."
    ],
    "life": [
        "Life is what happens when you're busy making other plans.",
        "The purpose of our lives is to be happy.",
        "Get busy living or get busy dying.",
        "The purpose of our lives is to be happy.",
        "In three words I can sum up everything I've learned about life: it goes on.",
        "Life is 10% what happens to us and 90 left is how we react to it.",
        "Life is a journey that must be traveled no matter how bad the roads and accommodations.",
        "Life is what happens when you're busy making other plans.",
        "Life is short, and it's up to you to make it sweet.",
        "Life is really simple, but we insist on making it complicated.",
        "The biggest adventure you can take is to live the life of your dreams.",
        "Life is not measured by the number of breaths we take, but by the moments that take our breath away.",
        "Life is not about waiting for the storms to pass, but learning how to dance in the rain.",
        "Life is a series of natural and spontaneous changes. Don't resist them; that only creates sorrow. Let reality be reality. Let things flow naturally forward in whatever way they like.",
        "The purpose of our lives is to be happy.",
        "The only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle.",
        "Life is either a daring adventure or nothing at all.",
        "Life is like riding a bicycle. To keep your balance, you must keep moving.",
        "Life is short, and it's up to you to make it sweet.",
        "The only impossible journey is the one you never begin.",
        "Life is what we make it, always has been, always will be.",
        "The greatest glory in living lies not in never falling, but in rising every time we fall.",
        "Life is a journey, not a destination.",
    ],
    "joke": [
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "Why did the scarecrow win an award? Because he was outstanding in his field.",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "I'm on a whiskey diet. I've lost three days already.",
        "What do you call fake spaghetti? An impasta!",
        "Why don’t some couples go to the gym? Because some relationships don’t work out.",
        "I used to play piano by ear, but now I use my hands.",
        "Why did the bicycle fall over? Because it was two-tired.",
        "I told my computer I needed a break and now it won't stop giving me pop-up ads for vacations.",
        "I'm trying to organize a hide and seek tournament, but good players are really hard to find.",
        "I'm on a whiskey diet. I've lost three days already.",
        "Why don’t some couples go to the gym? Because some relationships don’t work out.",
        "Why did the bicycle fall over? Because it was two-tired.",
        "I told my computer I needed a break and now it won't stop giving me pop-up ads for vacations.",
        "I'm trying to organize a hide and seek tournament, but good players are really hard to find.",
        "I used to play piano by ear, but now I use my hands.",
        "What do you call a bear with no teeth? A gummy bear, of course!"
    ]
}

@app.route('/api/quote', methods=['GET'])
def get_quote():
    category = request.args.get('category', 'life').lower()
    if category not in quotes:
        return jsonify({"error": "Category not found"}), 404
    quote = random.choice(quotes[category])
    return jsonify({"quote": quote})

if __name__ == '__main__':
    app.run(debug=True)
